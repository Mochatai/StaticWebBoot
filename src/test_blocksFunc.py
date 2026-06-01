import unittest
from textnode import TextNode, TextType
from inlineTotextNode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from blocksFunc import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node, text_node_to_html_node
import copy

class test_blockFunc(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_block_to_blockType(self): 
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            temp = []
            for x in blocks:
                 temp.append(block_to_block_type(x))

            
            self.assertEqual(
                 temp,
                 [BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.UNORDERED_LIST]

            )
        def test_block_to_block_types(self):
            block = "# heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)
            block = "```\ncode\n```"
            self.assertEqual(block_to_block_type(block), BlockType.CODE)
            block = "> quote\n> more quote"
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
            block = "- list\n- items"
            self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
            block = "1. list\n2. items"
            self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
            block = "paragraph"
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


        def test_paragraphs(self):
            md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

        def test_codeblock(self):
            md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )

        def test_paragraphs(self):
            md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
            node = markdown_to_html_node(md)
            html = node.to_html()
            html = html.replace("\n", " ")
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

        def test_codeblock(self):
            md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            
            self.assertEqual(
                html,
                "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )
if __name__ == "__main__":
    unittest.main()