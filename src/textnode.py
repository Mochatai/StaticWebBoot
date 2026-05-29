from enum import Enum
from LeafNode import LeafNode

class TextType(Enum):
     TEXT = ""
     BOLD = "b"
     ITALIC = "i"
     CODE = "code"
     LINK = "a"
     IMAGE = "img"

class TextNode:
        def __init__(self, text, text_type, url=None):
            self.text = text
            self.text_type = text_type
            self.url = url
    

        

        def __eq__(self, other):
            return True if self.text == other.text and self.text_type == other.text_type and self.url == other.url else False
    
        def __repr__(self):
            return f'TextNode({self.text}, {self.text_type}, {self.url})'
        
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
             
             if isinstance(text_node, TextNode) == False:
                  raise Exception("text_node is not of type TextNode")
                  
             if text_node.text_type.value == "":
                  return LeafNode(None, text_node.text)
             
             if text_node.text_type.value == "b":
                  return LeafNode("b", text_node.text)
             
             if text_node.text_type.value == "i":
                  return LeafNode("i", text_node.text)
             
             if text_node.text_type.value == "code":
                  return LeafNode("code", text_node.text)
             
             if text_node.text_type.value == "a":
                  return LeafNode("a", text_node.text, {"href": f'{text_node.url}'})
             
             if text_node.text_type.value == "img":
                  return LeafNode("img", None, {"src": f'{text_node.url}', "alt": f'{text_node.text}'})