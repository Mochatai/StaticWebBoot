from textnode import TextNode, TextType
from htmlnode import Leafnode
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    
    new_list =[]

    for x in old_nodes:
        if x.text_type != TextType.TEXT:
            new_list.append(x)
            continue
        
        text_split = x.text.split(delimiter)

        if len(text_split) %2  == 0:
            raise Exception("delimiter not found")
        
        
        for y in range(len(text_split)):
            if text_split[y] == "":
                continue
            if y % 2 == 0:
                new_list.append(TextNode(text_split[y], TextType.TEXT))
                continue

            new_list.append(TextNode(text_split[y], text_type))
        
    return new_list

def extract_markdown_images(text: str) -> tuple:
    #alts_list = re.findall(r"!\[(.+?)\]", text)
    #urls_list = re.findall(r"\]\((.+?)\)", text)
    #final_list = []
    urls_alt = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return urls_alt
    
    for x in range(len(alts_list)):
        final_list.append((alts_list[x],urls_list[x]))

    return final_list

    

def extract_markdown_links(text: str) -> list[tuple]:
    #alts_list = re.findall(r"\[(.+?)\]", text)
    #urls_list = re.findall(r"\]\((.+?)\)", text)
    
    urls_alt = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return urls_alt
    final_list = []

    for x in range(len(alts_list)):
        final_list.append((alts_list[x],urls_list[x]))

    return final_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    final_list = []
    temp = []

    for old_n in old_nodes:
        images = extract_markdown_images(old_n.text)
        temp = []
        
        if old_n.text_type != TextType.TEXT:
            final_list.append(old_n)
            continue
                
        txt = old_n.text

        if len(images) == 0:
            final_list.append(old_n)
            continue

        for x in range(len(images)):
            temp_x = txt.split(f"![{images[x][0]}]({images[x][1]})",1)

            if temp_x[0] != "":
                temp.append(TextNode(temp_x.pop(0), TextType.TEXT, None))
            temp.append(TextNode(images[x][0], TextType.IMAGE, images[x][1]))
            txt = temp_x[0]
        if txt != "":
            temp.append(TextNode(txt, TextType.TEXT, None))
        final_list.extend(temp)
    return final_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    final_list = []
    temp = []

    for old_n in old_nodes:
        links = extract_markdown_links(old_n.text)
        temp = []
        
        if old_n.text_type != TextType.TEXT:
            final_list.append(old_n)
            continue
                
        txt = old_n.text

        if len(links) == 0:
            final_list.append(old_n)
            continue

        for x in range(len(links)):
            temp_x = txt.split(f"[{links[x][0]}]({links[x][1]})",1)

            if temp_x[0] != "":
                temp.append(TextNode(temp_x.pop(0), TextType.TEXT, None))
                
            temp.append(TextNode(links[x][0], TextType.LINK, links[x][1]))
            txt = temp_x[0]
        if txt != "":
            temp.append(TextNode(txt, TextType.TEXT, None))
        final_list.extend(temp)
    return final_list

def text_to_textNodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes1 = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes2 = split_nodes_delimiter(new_nodes1, "`", TextType.CODE)
    new_nodes3 = split_nodes_link(new_nodes2)
    new_nodes4 = split_nodes_image(new_nodes3)
    
    return new_nodes4




