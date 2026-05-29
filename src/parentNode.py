
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)
        self.tag =tag
        self.children = children
        self.props = props
        
    def to_html(self):
        
        if self.tag == None:
            raise ValueError("parent node no tag")
        if self.children == None:
            raise ValueError("children node no value")
        
        st = f'<{self.tag}>'

        for x in self.children:
            st += x.to_html()

        return st + f'</{self.tag}>'
        
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props}'
    
