class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def toHTML(self):
        raise NotImplementedError

    def propstoHTML(self):
        if self.props is None:
            return ""
        finalProp = ""
        for prop in self.props:
            finalProp += f' {prop}="{self.props[prop]}"'
        return finalProp

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
