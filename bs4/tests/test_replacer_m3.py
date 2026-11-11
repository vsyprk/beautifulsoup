import unittest
from bs4 import BeautifulSoup, SoupReplacer

class TestSoupReplacerM3(unittest.TestCase):

    def test_name_xformer_lambda(self):
        html = "<div><b>Bold Text</b></div>"
        b_to_blockquote = SoupReplacer(
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
        )
        soup = BeautifulSoup(html, "html.parser", replacer=b_to_blockquote)
        self.assertIsNotNone(soup.find("blockquote"))
        self.assertIsNone(soup.find("b"))

    def test_attrs_xformer_dict(self):
        html = '<p class="old" id="p1">Hello</p>'
        def transform_attrs(tag):
            if tag.name == "p":
                return {"class": "test", "id": tag.attrs.get("id")}
            return tag.attrs

        replacer = SoupReplacer(attrs_xformer=transform_attrs)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        p = soup.find("p")
        self.assertEqual(p["class"], "test")
        self.assertEqual(p["id"], "p1")

    def test_xformer_side_effect_delete_attr(self):
        html = '<div class="remove-me"><p class="remove-me">Text</p></div>'
        def remove_class_attr(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]

        replacer = SoupReplacer(xformer=remove_class_attr)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        for tag in soup.find_all(True):
            self.assertNotIn("class", tag.attrs)

    def test_xformer_add_or_replace_class(self):
        html = '<p>No class</p><p class="existing">Has class</p>'
        def add_test_class(tag):
            if tag.name == "p":
                tag.attrs["class"] = "test"

        replacer = SoupReplacer(xformer=add_test_class)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        for p in soup.find_all("p"):
            self.assertEqual(p.get("class"), "test")

    def test_combined_name_and_attrs_xformer(self):
        html = '<h1 class="header">Title</h1>'
        replacer = SoupReplacer(
            name_xformer=lambda tag: "h2" if tag.name == "h1" else tag.name,
            attrs_xformer=lambda tag: {"class": "subheader"} if tag.name == "h1" else tag.attrs
        )
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        h2 = soup.find("h2")
        self.assertIsNotNone(h2)
        self.assertEqual(h2["class"], "subheader")

    def test_xformer_conditional_mutation(self):
        html = '<a href="http://example.com">Link 1</a><a href="https://secure.com">Link 2</a>'
        def enforce_https(tag):
            if tag.name == "a" and tag.attrs.get("href", "").startswith("http://"):
                tag.attrs["href"] = tag.attrs["href"].replace("http://", "https://")

        replacer = SoupReplacer(xformer=enforce_https)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        links = soup.find_all("a")
        self.assertTrue(all(link["href"].startswith("https://") for link in links))

if __name__ == "__main__":
    unittest.main()