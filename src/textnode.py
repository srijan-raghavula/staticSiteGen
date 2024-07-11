import htmlnode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return (
            self.text == node.text and
            self.text_type == node.text_type and
            self.url == node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def TextNodetoHTMLNode(textnode):
    match textnode.text_type:
        case "text":
            return htmlnode.LeafNode(None, textnode.text)
        case "bold":
            return htmlnode.LeafNode("b", textnode.text)
        case "italic":
            return htmlnode.LeafNode("i", textnode.text)
        case "code":
            return htmlnode.LeafNode("code", textnode.text)
        case "link":
            return htmlnode.LeafNode("a", textnode.text,
                                     {"href": textnode.url})
        case "image":
            return htmlnode.LeafNode("img", "",
                                     {"src": textnode.url,
                                      "alt": textnode.text})
        case _:
            raise Exception(
                f'invalid text type: {textnode.text_type}'
            )
