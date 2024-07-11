def MDtoBlocks(markdown):
    rawsplit = markdown.split("\n\n")
    blockedList = []
    for line in rawsplit:
        sentences = line.split("\n")
        for i in range(len(sentences)):
            if sentences[i] == '':
                sentences.pop(i)
        noWhites = [sentence.strip() for sentence in sentences]
        blockedList.append("\n".join(noWhites))
    return blockedList


def blockType(block):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    ul = "ul"
    ol = "ol"

    Quote = False
    UL = False
    OL = False
    if block.startswith("#"):
        return heading
    elif block.startswith("```"):
        return code
    lines = block.split("\n")
    for line in lines:
        if line != '':
            if line[0] == '>':
                Quote = True
            elif ((line[0] == '*' or line[0] == '-') and line[1] == ' '):
                UL = True
            elif line[0] == '.' and line[1] == ' ':
                OL = True

    if Quote:
        if UL is False and OL is False:
            return quote
        return paragraph
    if UL:
        if OL is False and Quote is False:
            return ul
        return paragraph
    if OL:
        if Quote is False and UL is False:
            return ol
        return paragraph
    else:
        return paragraph
