
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node no value")
        if self.tag == None:
            return self.value
        
        if self.children != None:
            prop =  self.props
            return f'<{self.tag} {prop}>{self.value}</{self.tag}>'

        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props}'