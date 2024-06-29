import htmlnode
import re


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


def texttoTextNode(text):
    return splitNodesDelimiter(splitNodesDelimiter(splitNodesDelimiter(splitNodesImages(splitNodesLinks([TextNode(text, "text")])), '`', "code"), "*", "italic"), "**", "bold")


def splitNodesDelimiter(nodes, delimiter, text_type):
    if type(nodes) is not list:
        raise Exception("onlyLists")
    newNodes = []
    for node in nodes:
        if type(node) is not TextNode:
            newNodes.update(node)
            continue
        if node.text.startswith(delimiter):
            isText = False
        isText = True
        splitText = node.text.split(delimiter)
        nodeList = []
        for text in splitText:
            if isText is True:
                nodeList.append(TextNode(text, text))
            else:
                nodeList.append(TextNode(text, text_type))
            isText = not isText
        newNodes.extend(nodeList)
    return newNodes


def splitNodesImages(nodes):
    newNodes = []
    for node in nodes:
        if type(node) is not TextNode:
            continue
        if node.text is not None:
            print(type(node.text))
            extract = extractMDImages(node.text)
            if len(extract) == 0:
                newNodes.extend([node])
                continue
            split = node.text.split(f'![{extract[0][0]}({extract[0][1]})]', 1)
            list = []
            if split[0] != '':
                list.append(TextNode(split[0], "text"))
            list.append(TextNode(extract[0], "image"))
            if len(split) > 1 and split[1] != '':
                newNodes.extend(list.append(splitNodesImages([split[1]])))
                continue
            newNodes.extend(list)
    return newNodes


def splitNodesLinks(nodes):
    newNodes = []
    for node in nodes:
        if type(node) is not TextNode:
            continue
        if node.text is not None:
            extract = extractMDLinks(node.text)
            if len(extract) == 0:
                newNodes.extend([node])
                continue
            split = node.text.split(f'![{extract[0][0]}({extract[0][1]})]', 1)
            list = []
            if split[0] != '':
                list.append(TextNode(split[0], "text"))
            list.append(TextNode(extract[0], "link"))
            if len(split) > 1 and split[1] != '':
                newNodes.extend(list.append(splitNodesLinks([split[1]])))
                continue
            newNodes.extend(list)
    return newNodes


def extractMDImages(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extractMDLinks(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
