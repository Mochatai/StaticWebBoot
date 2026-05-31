import unittest
from inlineTotextNode import split_nodes_delimiter, split_nodes_link, split_nodes_image, text_to_textNodes
from textnode import TextNode, TextType


class test_extractImgLink(unittest.TestCase):
        
        def test_text_to_textNodes(self):
            text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            node = text_to_textNodes(text)
            self.assertListEqual(
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),

                ],
                node,
            )


if __name__ == "__main__":
    unittest.main()