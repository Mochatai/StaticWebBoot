import unittest
from textnode import TextNode, TextType
from inlineTotextNode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from htmlnode import text_node_to_html_node


class test_extractImgLink(unittest.TestCase):
        
        def test_split_image(self):
            node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                ],
                new_nodes,
            )

        def test_split_image_single(self):
            node = TextNode(
                "![image](https://www.example.COM/IMAGE.PNG)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
                ],
                new_nodes,
            )

        def test_split_images(self):
            node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode(
                        "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                    ),
                ],
                new_nodes,
            )

        def test_split_links(self):
            node = TextNode(
                "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("another link", TextType.LINK, "https://wikipedia.org"),
                    TextNode(" with text that follows", TextType.TEXT),
                ],
                new_nodes,
            )


if __name__ == "__main__":
    unittest.main()