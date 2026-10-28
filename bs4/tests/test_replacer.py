import unittest
from bs4 import BeautifulSoup, SoupReplacer

class TestSoupReplacer(unittest.TestCase):

    def test_basic_tag_replacement(self):
        """Verify <b> tags are converted to <blockquote> during parse time."""
        html_doc = "<div><b>First bold</b><p>Normal text</p><b>Second bold</b></div>"
        b_to_blockquote = SoupReplacer("b", "blockquote")
        
        soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)
        
        self.assertIsNone(soup.find("b"))
        self.assertEqual(len(soup.find_all("blockquote")), 2)
        self.assertEqual(soup.find("blockquote").string, "First bold")

    def test_nested_tag_replacement(self):
        """Verify replacement works on nested elements without tree breakage."""
        html_doc = "<p>Outer <b>inner <b>nested</b> text</b></p>"
        b_to_i = SoupReplacer("b", "i")
        
        soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_i)
        
        self.assertIsNone(soup.find("b"))
        self.assertEqual(len(soup.find_all("i")), 2)
        self.assertIn("nested", soup.find("i").get_text())

if __name__ == "__main__":
    unittest.main()