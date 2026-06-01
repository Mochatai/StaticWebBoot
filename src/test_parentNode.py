import unittest

from htmlnode import Leafnode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = Leafnode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = Leafnode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_nonchildern(self):

        grandch = Leafnode(None, "ggg")
        parent_node = ParentNode("span", [grandch])
        root_node = ParentNode("div", [parent_node])
        
        self.assertEqual(root_node.to_html(),"<div><span>ggg</span></div>")

    def test_to_html_childernProp(self):
        grandch = Leafnode("a", "click me", {"href": "https://google.com"})
        parent_node = ParentNode("span", [grandch])
        root_node = ParentNode("div", [parent_node])
        
        self.assertEqual(root_node.to_html(),"<div><span><a href=\"https://google.com\">click me</a></span></div>")

def test_to_html_childernProps(self):
        grandch = Leafnode("a", "click me", {"href": "https://google.com", "target": "blank"})
        parent_node = ParentNode("span", [grandch])
        root_node = ParentNode("div", [parent_node])
        
        self.assertEqual(root_node.to_html(),"<div><span><a href=\"https://google.com\" target=\"blank\">click me</a></span></div>")

if __name__ == "__main__":
    unittest.main()