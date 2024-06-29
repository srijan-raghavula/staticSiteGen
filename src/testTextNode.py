import unittest

from textnode import TextNode
from textnode import splitNodesDelimiter
from textnode import extractMDImages
from textnode import extractMDLinks
from textnode import splitNodesImages
from textnode import splitNodesLinks
from textnode import texttoTextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a TextNode", "bold")
        node2 = TextNode("This is a TextNode", "bold")
        self.assertEqual(node, node2)


text = "text"
bold = "bold"
italic = "italic"
code = "code"
image = "image"
link = "link"


class TestNodesDelimiter(unittest.TestCase):
    def test_eq(self):
        global text, bold, italic, code
        oldNodes = [TextNode("Normal text in **bold** but normal again", text),
                    TextNode("**Bold start** but normal ending", text),
                    TextNode("Normal but **bold** and it's **twice**", text)]
        newNodes = [[TextNode("Normal text in ", text),
                     TextNode("bold", bold),
                     TextNode(" but normal again", text)],
                    [TextNode("Bold start", bold),
                     TextNode(" but normal ending", text)],
                    [TextNode("Normal but ", text),
                     TextNode("bold", bold),
                     TextNode(" and it's ", text),
                     TextNode("twice", bold)],
                    ]
        self.assertEqual(splitNodesDelimiter(oldNodes, '**', bold),
                         splitNodesDelimiter(oldNodes, '**', bold), newNodes)


class TestSplitNodesimg(unittest.TestCase):
    def test_eq(self):
        global text, bold, italic, code
        oldNodes = [TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text),
                    TextNode("![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text)
                    ]
        newNodes = [[TextNode("This is text with an ", text),
                    TextNode("image", image,
                             "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    TextNode(" and another ", text),
                    TextNode("second image", image,
                             "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                     ],
                    [TextNode("image", image,
                              "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    TextNode(" and another ", text),
                    TextNode("second image", image,
                             "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                     ]]
        self.assertEqual(splitNodesImages(oldNodes),
                         splitNodesImages(oldNodes), newNodes)


class TestSplitNodeslinks(unittest.TestCase):
    def test_eq(self):
        global text, bold, italic, code
        oldNodes = [TextNode("This is text with an [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text),
                    TextNode("[image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text)
                    ]
        newNodes = [[TextNode("This is text with an ", text),
                    TextNode("image", link,
                             "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    TextNode(" and another ", text),
                    TextNode("second image", link,
                             "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                     ],
                    [TextNode("image", link,
                              "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    TextNode(" and another ", text),
                    TextNode("second image", link,
                             "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                     ]]
        self.assertEqual(splitNodesLinks(oldNodes),
                         splitNodesLinks(oldNodes), newNodes)


class TestExtrctMDimgnlinks(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(extractMDImages("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"), [
                         ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
        self.assertEqual(extractMDLinks("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"), [
                         ("link", "https://www.example.com"), ("another", "https://www.example.com/another")])


class TestTexttoTextNode(unittest.TestCase):
    def test_eq(self):
        input = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        output = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image",
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(texttoTextNode(input), output)


if __name__ == "__main__":
    unittest.main()
