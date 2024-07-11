import htmlnode
import inlineMD
from textnode import TextNodetoHTMLNode
from splitblocks import blockType
from splitblocks import MDtoBlocks


def doctoHTMLNode(doc):
    blocks = MDtoBlocks(doc)
    htmlnodes = []
    for block in blocks:
        htmlnodes.append(blocktoHTML(block, blockType(block)))
    tag = ""
    for node in htmlnodes:
        tag += node
    print(tag)
    node = htmlnode.LeafNode("div", tag)
    return node


def blocktoHTML(block, type):
    match(type):
        case "paragraph":
            return paraHTML(block)
        case "heading":
            return headingHTML(block)
        case "code":
            return htmlnode.ParentNode("pre", codeHTML(block))
        case "quote":
            return quoteHTML(block)
        case "ul":
            return ulHTML(block)
        case "ol":
            return olHTML(block)
        case _:
            raise NotImplementedError


def paraHTML(block):
    textnodes = inlineMD.texttoTextNode(block)
    htmlnodes = [TextNodetoHTMLNode(node) for node in textnodes]
    parent = htmlnode.ParentNode("p", htmlnodes)
    return parent


def headingHTML(block):
    hashes = 0
    for char in block:
        if char == '#':
            hashes += 1
    blocked = block[hashes:]
    textnodes = inlineMD.texttoTextNode(blocked)
    htmlnodes = [TextNodetoHTMLNode(node) for node in textnodes]
    parent = htmlnode.ParentNode(f'h{hashes}', htmlnodes)
    return parent


def codeHTML(block):
    textnodes = inlineMD.texttoTextNode(block)
    htmlnodes = [TextNodetoHTMLNode(node) for node in textnodes]
    codeparent = htmlnode.ParentNode("code", htmlnodes)
    return codeparent


def quoteHTML(block):
    stripped = []
    for line in block.split("\n"):
        line = line[2:]
        stripped.append(line)
    block = "\n".join(stripped)
    textnodes = inlineMD.texttoTextNode(block)
    htmlnodes = [TextNodetoHTMLNode(node) for node in textnodes]
    parent = htmlnode.ParentNode("blockquote", htmlnodes)
    return parent


def ulHTML(block):
    stripped = []
    for line in block.split("\n"):
        line = line[2:]
        stripped.append(line)
    children = toliHTML(stripped)
    parent = htmlnode.ParentNode("ul", children)
    return parent


def olHTML(block):
    stripped = []
    for line in block.split("\n"):
        line = line[2:]
        stripped.append(line)
    children = toliHTML(stripped)
    parent = htmlnode.ParentNode("ol", children)
    return parent


def toliHTML(lst):
    htmlnodes = [htmlnode.LeafNode("li", line) for line in lst]
    return htmlnodes
