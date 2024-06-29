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


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def toHTML(self):
        if self.tag is None:
            raise ValueError("can't have an empty/NoneType tag")
        if self.children is None:
            raise ValueError("no children found, use LeafNode instead")
        tag = f'<{self.tag}{super().propstoHTML()}>'
        for child in self.children:
            tag += child.toHTML()
        tag += f'</{self.tag}>'
        return tag

    def __repr__(self):
        return f'{self.tag}, {self.children}, {self.props}'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)

    def toHTML(self):
        if self.value is None:
            raise ValueError("value cannot be NoneType")
        if self.tag is None:
            return str(self.value)
        if self.children is not None:
            raise ValueError("can't have children in LeafNode")
        if self.props is not None:
            return f'<{self.tag}{super().propstoHTML()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.children}, {self.props})'
