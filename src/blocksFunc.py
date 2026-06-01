from textnode import TextNode, TextType
from htmlnode import HTMLNode, Leafnode, ParentNode, text_node_to_html_node
from inlineTotextNode import text_to_textNodes
from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"



def markdown_to_blocks(markdown: str) -> list[str]:
    new_mark = markdown.split("\n\n")

    new_str_mark = []

    for x in new_mark:
        if x == "":
            continue
        new_str_mark.append(x.strip())

    return new_str_mark


def block_to_block_type(markdown: str):

    lines = markdown.split("\n")

    if markdown.startswith(("#","##","###","####","#####","######")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE
    
    if markdown.startswith(">"):
        for x in lines:
            if ">" not in x:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if markdown.startswith("- "):
        for x in lines:
            if "- " not in x:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if markdown.startswith("1. "):
        i = 1
        for x in lines:
            if f"{i}. " not in x:
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH



    if markdown.startswith("."):
        return BlockType.UNORDERED_LIST
    
    if re.search(r"^(.?)\.", markdown):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    
    

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    temp = []
    for block in blocks:
        
        block_type = block_to_block_type(block)
        
        all = text_to_children(block_type, block)
        temp.append(all)
        

    parent_div = ParentNode("div", temp)

    return parent_div



def text_to_children(block_type, block):
    

    match block_type:
        case BlockType.PARAGRAPH:
            temp = text_to_textNodes(block)

            
            list_textnodes_leafnode = []
            for text_node in temp:
                list_textnodes_leafnode.append(text_node_to_html_node(text_node))
            pt = ParentNode(BlockType.PARAGRAPH.value, list_textnodes_leafnode)
            
            return pt
         
        case BlockType.HEADING:
            striped_block = block.strip()

            h_count = re.search(r"^#+ ", striped_block)
            h_count_num = h_count.end() - 1
            striped_block_slice = striped_block[h_count_num + 1:]

            temp = text_to_textNodes(striped_block_slice)
            list_textnodes_leafnode = []
            for text_node in temp:
                list_textnodes_leafnode.append(text_node_to_html_node(text_node))
            pt = ParentNode(f'h{h_count_num}', list_textnodes_leafnode)
            
            return pt
            

        case BlockType.CODE:
            
            strip_code = block.strip("```")
            
            txt_node_code = TextNode(strip_code, TextType.CODE)
            txt_node_code_to_html = text_node_to_html_node(txt_node_code)
            htmo_code_node = ParentNode("pre", [txt_node_code_to_html])

            return htmo_code_node

        case BlockType.QUOTE:
            text_strip = block.strip()
            text_clean_strip = re.sub(r">+ ", "", text_strip)

            text_clean_strip_node = text_to_textNodes(text_clean_strip)

            list_textnodes_leafnode = []
            for text_node in text_clean_strip_node:
                list_textnodes_leafnode.append(text_node_to_html_node(text_node))
            pt = ParentNode(f'{BlockType.QUOTE.value}', list_textnodes_leafnode)
            
            return pt


        case BlockType.UNORDERED_LIST:
            text_strip = block.strip()
            text_clean_strip = re.sub(r"-+ ", "", text_strip)

            text_clean_strip_node = text_to_textNodes(text_clean_strip)

            list_textnodes_leafnode = []
            for text_node in text_clean_strip_node:
                temp = text_node_to_html_node(text_node)
                list_textnodes_leafnode.append(Leafnode("li",temp.to_html()))
            pt = ParentNode(f'{BlockType.UNORDERED_LIST.value}', list_textnodes_leafnode)
            
            return pt


        case BlockType.ORDERED_LIST:
            text_strip = block.strip()
            text_clean_strip = re.sub(r"[0-9]. +", "", text_strip)

            text_clean_strip_node = text_to_textNodes(text_clean_strip)

            list_textnodes_leafnode = []
            for text_node in text_clean_strip_node:
                temp = text_node_to_html_node(text_node)
                list_textnodes_leafnode.append(Leafnode("li",temp.to_html()))
            pt = ParentNode(f'{BlockType.ORDERED_LIST.value}', list_textnodes_leafnode)
            
            return pt
        


def main():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)
if __name__ == "__main__":
    main()