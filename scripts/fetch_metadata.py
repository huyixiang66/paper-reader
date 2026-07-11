import urllib.request
import urllib.parse
import json
import sys
import re
import os
import tempfile
import time

ARXIV_API = "http://export.arxiv.org/api/query"
S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

def http_get(url, retries=2):
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            if attempt < retries:
                time.sleep(1 * (attempt + 1))
            else:
                raise e

def extract_arxiv_id(raw):
    raw = raw.strip()
    m = re.search(r'(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?', raw)
    if m:
        return m.group(1)
    m = re.match(r'^(\d{4}\.\d{4,5})(?:v\d+)?$', raw)
    if m:
        return m.group(1)
    return None

def fetch_arxiv_xml(arxiv_id):
    url = ARXIV_API + "?id_list=" + arxiv_id + "&max_results=1"
    xml = http_get(url)
    entry_m = re.search(r"<entry>(.*?)</entry>", xml, re.DOTALL)
    if not entry_m:
        return {"title": "", "summary": "", "authors": [], "categories": [], "date": "", "error": "No entry found"}
    entry = entry_m.group(1)
    def extract(tag):
        pat = r"<(?:\{[^}]*\})?" + tag + r">(.*?)</(?:\{[^}]*\})?" + tag + r">"
        m = re.search(pat, entry, re.DOTALL)
        if m:
            return m.group(1).strip().replace("\n", " ")
        return ""
    title = extract("title")
    summary = extract("summary")
    date = extract("published")
    authors = []
    author_blocks = re.findall(r"<author>(.*?)</author>", entry, re.DOTALL)
    for block in author_blocks:
        name_m = re.search(r"<name>(.*?)</name>", block, re.DOTALL)
        if name_m:
            authors.append(name_m.group(1).strip())
    cats = []
    for block in re.findall(r"<category[^>]*term=\"([^\"]*)\"", entry):
        cats.append(block)
    return {"title": title, "summary": summary, "authors": authors, "categories": cats, "date": date}

def fetch_semantic_scholar(title=None):
    if not title:
        return {}
    q = urllib.parse.quote(title)
    url = S2_SEARCH + "?query=" + q + "&limit=1&fields=title,authors,year,venue,citationCount,referenceCount,isOpenAccess,url,tldr"
    try:
        raw = http_get(url)
        data = json.loads(raw)
        hits = data.get("data", [])
        if hits:
            d = hits[0]
            authors = [a.get("name", "") for a in d.get("authors", [])] if isinstance(d.get("authors"), list) else []
            return {
                "title": d.get("title", ""),
                "authors": authors,
                "year": d.get("year"),
                "venue": d.get("venue"),
                "citationCount": d.get("citationCount", 0),
                "referenceCount": d.get("referenceCount", 0),
                "isOpenAccess": d.get("isOpenAccess"),
                "url": d.get("url"),
                "tldr": d.get("tldr", {}).get("summary", "") if d.get("tldr") else "",
            }
    except Exception:
        pass
    return {}

def fetch_pdf(arxiv_id, outdir=None):
    if outdir is None:
        outdir = tempfile.gettempdir()
    url = "https://arxiv.org/pdf/" + arxiv_id + ".pdf"
    outpath = os.path.join(outdir, arxiv_id + ".pdf")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        with open(outpath, "wb") as f:
            f.write(data)
        return {"status": "ok", "path": outpath, "size": len(data)}
    except Exception as e:
        return {"status": "error", "error": str(e)}

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "metadata"
    target = sys.argv[2] if len(sys.argv) > 2 else ""
    if mode == "metadata":
        arxiv_id = extract_arxiv_id(target)
        if not arxiv_id:
            print(json.dumps({"error": "Could not extract arXiv ID from: " + target}, ensure_ascii=False))
            sys.exit(1)
        arxiv_data = fetch_arxiv_xml(arxiv_id)
        s2_data = fetch_semantic_scholar(title=arxiv_data.get("title", ""))
        result = {"arxiv_id": arxiv_id, "arxiv": arxiv_data, "semantic_scholar": s2_data}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif mode == "pdf":
        arxiv_id = extract_arxiv_id(target)
        if not arxiv_id:
            arxiv_id = target.strip()
        outdir = sys.argv[3] if len(sys.argv) > 3 else tempfile.gettempdir()
        result = fetch_pdf(arxiv_id, outdir)
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(json.dumps({"error": "Unknown mode: " + mode}, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()
