import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode("<a>", "value inside", ["list"], {"href": "https://www.google.com"})
        g = node.props_to_html()
        print(g)
    def test_isnon(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)

    def test_eq(self):
        node = HTMLNode("<a>", "value inside", ["list"], {"href": "https://www.google.com"})
        node2 = HTMLNode("<a>", "value inside", ["list"], {"href": "https://www.google.com"})
        self.assertEqual(node.tag, node2.tag)

if __name__ == "__main__":
    unittest.main()