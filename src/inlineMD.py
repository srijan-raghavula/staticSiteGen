import re
from textnode import TextNode


def texttoTextNode(text):
    node = [TextNode(text, "text")]
    bolds = splitNodesDelimiter(node, "**", "bold")
    italics = splitNodesDelimiter(bolds, "*", "italic")
    codes = splitNodesDelimiter(italics, "`", "code")
    images = splitNodesImages(codes)
    links = splitNodesLinks(images)
    return links


def splitNodesDelimiter(nodes, delimiter, text_type):
    if not isinstance(nodes, list):
        raise Exception("onlyLists")
    newNodes = []
    for node in nodes:
        if node.text_type != "text":
            newNodes.extend([node])
            continue
        if isinstance(node, list):
            newNodes.extend(splitNodesDelimiter(node, delimiter, text_type))
            continue
        if node.text.startswith(delimiter):
            isText = False
        isText = True
        splitText = node.text.split(delimiter)
        nodeList = []
        for text in splitText:
            if isText is True:
                nodeList.append(TextNode(text, "text"))
            else:
                nodeList.append(TextNode(text, text_type))
            isText = not isText
        newNodes.extend(nodeList)
    return newNodes


def splitNodesImages(nodes):
    newNodes = []
    for node in nodes:
        list = []
        if type(node) == 'list':
            list.extend(node)
            continue
        if isinstance(node.text, str) and node.text_type != None:
            extract = extractMDImages(node.text)
            if len(extract) > 0:
                split = node.text.split(
                    f"![{extract[0][0]}]({extract[0][1]})", 1)
                if split[0] != '':
                    list.append(TextNode(split[0], "text"))
                list.append(TextNode(extract[0][0], "image", extract[0][1]))
                if len(split) > 1 and split[1] != '':
                    for item in splitNodesLinks([TextNode(split[1], "text")]):
                        list.append(item)
            else:
                list.append(node)
        newNodes.extend(list)
    return newNodes


def splitNodesLinks(nodes):
    newNodes = []
    for node in nodes:
        list = []
        if type(node) == 'list':
            list.extend(node)
            continue
        if isinstance(node.text, str) and node.text_type != None:
            extract = extractMDLinks(node.text)
            if len(extract) > 0:
                split = node.text.split(
                    f"[{extract[0][0]}]({extract[0][1]})", 1)
                if split[0] != '':
                    list.append(TextNode(split[0], "text"))
                list.append(TextNode(extract[0][0], "link", extract[0][1]))
                if len(split) > 1 and split[1] != '':
                    for item in splitNodesLinks([TextNode(split[1], "text")]):
                        list.append(item)
            else:
                list.append(node)
        newNodes.extend(list)
    return newNodes


def extractMDImages(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extractMDLinks(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
