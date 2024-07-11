import unittest

from textnode import TextNode
from inlineMD import splitNodesLinks
from inlineMD import splitNodesImages
from inlineMD import splitNodesDelimiter
from inlineMD import texttoTextNode
from inlineMD import extractMDLinks
from inlineMD import extractMDImages


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
                     TextNode("twice", bold)]]
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


class TestExtractMDimgnlinks(unittest.TestCase):
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
        input1 = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) and another [link1](https://boot.dev)"
        output1 = [
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
            TextNode(" and another ", "text"),
            TextNode("link1", "link", "https://boot.dev"),
        ]
        input2 = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        output2 = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image",
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        ]
        self.assertEqual(texttoTextNode(input), output)
        self.assertEqual(texttoTextNode(input1), output1)
        self.assertEqual(texttoTextNode(input2), output2)


if __name__ == "__main__":
    unittest.main()
