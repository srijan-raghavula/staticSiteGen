import unittest

from htmlnode import HTMLNode
from htmlnode import ParentNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "tag",
            "value",
            "children",
            {"ex": "somelink", "ex2": "someotherlink"}
        )
        node2 = HTMLNode()
        node.__repr__()
        node2.__repr__()
        self.assertEqual(
            node.propstoHTML(),
            ' ex="somelink" ex2="someotherlink"'
        )
        self.assertEqual(node2.propstoHTML(), "")


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            'p',
            [LeafNode("b", "Bold text"),
             LeafNode(None, "Normal text"),
             LeafNode("i", "italic text"),
             LeafNode(None, "Normal text")],
            {"ex": "somelink", "ex2": "someotherlink"}
        )
        self.assertEqual(node.toHTML(),
                         '<p ex="somelink" ex2="someotherlink"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
                         )
        node2 = ParentNode(
            'p',
            [LeafNode("b", "Bold text"),
             LeafNode(None, "Normal text"),
             LeafNode("i", "italic text"),
             LeafNode(None, "Normal text")],
        )
        self.assertEqual(node2.toHTML(),
                         '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
                         )


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(
            "tag",
            "value",
            None,
            {"ex": "somelink", "ex2": "someotherlink"}
        )
        node2 = LeafNode(
            "tag",
            "value",
            None,
            None,
        )
        self.assertEqual(
            node.toHTML(), '<tag ex="somelink" ex2="someotherlink">value</tag>')
        self.assertEqual(node2.toHTML(), '<tag>value</tag>')


if __name__ == "__main__":
    unittest.main()
