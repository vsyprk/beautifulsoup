import pytest
from bs4 import BeautifulSoup, Tag, NavigableString, Comment, CData, Doctype


class TestBeautifulSoupIteration:
    def test_empty_and_whitespace_documents(self):
        empty_soup = BeautifulSoup("", "html.parser")
        assert list(empty_soup) == []

        ws_soup = BeautifulSoup("   \n\t  ", "html.parser")
        nodes = list(ws_soup)
        assert len(nodes) == 1
        assert isinstance(nodes[0], NavigableString)

    def test_tags_and_navigable_strings_preorder(self):
        html = "<html><body><div><p>Hello</p><b>World</b></div></body></html>"
        soup = BeautifulSoup(html, "html.parser")

        visited = [
            node.name if isinstance(node, Tag) else str(node)
            for node in soup
        ]
        assert visited == ["html", "body", "div", "p", "Hello", "b", "World"]

    def test_special_page_elements_doctype_comment_cdata(self):
        xml = (
            "<!DOCTYPE html>"
            "<div><!-- header comment -->"
            "<script><![CDATA[var x = 1 < 2;]]></script>"
            "</div>"
        )
        soup = BeautifulSoup(xml, "html.parser")
        nodes = list(soup)

        assert any(isinstance(n, Doctype) for n in nodes)
        assert any(isinstance(n, Comment) and "header comment" in str(n) for n in nodes)
        assert any(isinstance(n, Tag) and n.name == "script" for n in nodes)
        assert any(isinstance(n, CData) and "var x = 1 < 2;" in str(n) for n in nodes)

    def test_lazy_generator_streaming_without_list_collection(self):
        html = "<ul>" + "".join(f"<li>item-{i}</li>" for i in range(50)) + "</ul>"
        soup = BeautifulSoup(html, "html.parser")

        it = iter(soup)
        # Confirm iter(soup) returns a generator/iterator object, not a list_iterator
        assert iter(it) is it
        assert not isinstance(it, type(iter([])))

        first = next(it)
        assert isinstance(first, Tag) and first.name == "ul"
        second = next(it)
        assert isinstance(second, Tag) and second.name == "li"
        third = next(it)
        assert isinstance(third, NavigableString) and str(third) == "item-0"

    def test_subtree_tag_iteration_unchanged(self):
        html = "<div><p><span>nested</span></p><a>sibling</a></div>"
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find("div")

        # Iterating over a regular Tag must still yield only its direct children
        direct_children = [child.name for child in div]
        assert direct_children == ["p", "a"]