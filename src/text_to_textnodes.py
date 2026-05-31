
from inlineTotextNode import split_nodes_delimiter, split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

def text_to_textNodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes1 = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes2 = split_nodes_delimiter(new_nodes1, "`", TextType.CODE)
    new_nodes3 = split_nodes_link(new_nodes2)
    new_nodes4 = split_nodes_image(new_nodes3)
    
    return new_nodes4

def main():
    x = text_to_textNodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    
    for y in x:
        print(y)
if __name__ == "__main__":
    main()