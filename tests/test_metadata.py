import unittest
import sys
import os
import json

# Add the scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

class TestExtractArxivId(unittest.TestCase):
    """Test arXiv ID extraction from various input formats."""

    def test_bare_id(self):
        from fetch_metadata import extract_arxiv_id
        self.assertEqual(extract_arxiv_id("1706.03762"), "1706.03762")

    def test_bare_id_with_version(self):
        from fetch_metadata import extract_arxiv_id
        self.assertEqual(extract_arxiv_id("1706.03762v2"), "1706.03762")

    def test_abs_url(self):
        from fetch_metadata import extract_arxiv_id
        self.assertEqual(extract_arxiv_id("https://arxiv.org/abs/1706.03762"), "1706.03762")

    def test_pdf_url(self):
        from fetch_metadata import extract_arxiv_id
        self.assertEqual(extract_arxiv_id("https://arxiv.org/pdf/2401.12345v3"), "2401.12345")

    def test_invalid_input(self):
        from fetch_metadata import extract_arxiv_id
        self.assertIsNone(extract_arxiv_id("not-an-id"))
        self.assertIsNone(extract_arxiv_id(""))
        self.assertIsNone(extract_arxiv_id("random text"))

    def test_whitespace_handling(self):
        from fetch_metadata import extract_arxiv_id
        self.assertEqual(extract_arxiv_id("  1706.03762  "), "1706.03762")

if __name__ == "__main__":
    unittest.main()
