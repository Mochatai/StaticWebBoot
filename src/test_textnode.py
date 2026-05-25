import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text g", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_non(self):
        node = TextNode("This is a text g", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url, node2.url)

if __name__ == "__main__":
    unittest.main()