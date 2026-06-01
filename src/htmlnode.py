from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        str_props = ""
        for x in self.props:
            str_props += f' {x}="{self.props[x]}"'
        return str_props
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}'
    

class Leafnode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    
    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props}'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children: list[HTMLNode] | None, props=None):
        super().__init__(tag,None, children, props)
        
        
    def to_html(self):
        
        if self.tag is None:
            raise ValueError("parent node no tag")
        if self.children is None:
            raise ValueError("children node no value")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

        
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props}'
    

def text_node_to_html_node(text_node: TextNode) -> Leafnode:
                            
            if text_node.text_type == TextType.TEXT:
                  return (Leafnode(tag=None, value=text_node.text))
             
            if text_node.text_type == TextType.BOLD:
                  return (Leafnode(tag="b", value=text_node.text))
             
            if text_node.text_type == TextType.ITALIC:
                  return (Leafnode(tag="i", value=text_node.text))
             
            if text_node.text_type == TextType.CODE:
                  return (Leafnode(tag="code", value=text_node.text))
             
            if text_node.text_type == TextType.LINK:
                  return (Leafnode(tag="a", value=text_node.text, props={"href": f'{text_node.url}'}))
             
            if text_node.text_type == TextType.IMAGE:
                  return (Leafnode(tag="img", value="", props={"src": f'{text_node.url}', "alt": f'{text_node.text}'}))
             
            raise ValueError(f"invalid text type")
            