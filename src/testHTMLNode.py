import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "tag",
            "value",
            "children",
            '{"ex": "somelink" "ex2": "someotherlink"}'
        )
        node2 = HTMLNode()
        node.__repr__()
        node2.__repr__()
        self.assertEqual(
            node.propstoHTML(),
            'ex="somelink" ex2="someotherlink"'
        )
        self.assertEqual(node2.propstoHTML(), "")


if __name__ == "__main__":
    unittest.main()
