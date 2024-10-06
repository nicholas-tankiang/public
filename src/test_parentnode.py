import unittest
from parentnode import ParentNode
from leafnode import LeafNode 

class TestParentNode(unittest.TestCase):
    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", children=[])  
            node.to_html()

    def test_single_child(self):
        node = ParentNode("p", [LeafNode("b", "bold content")])
        self.assertEqual(node.to_html(), "<p><b>bold content</b></p>")

    def test_multi_child(self):
        node = ParentNode("p", [
            LeafNode("b", "bold content"), 
            LeafNode(None, "cold content")
        ])
        self.assertEqual(node.to_html(), "<p><b>bold content</b>cold content</p>")

    def test_parent_child(self):
        node = ParentNode("p", [
            LeafNode("b", "bold content"),
            ParentNode("div", [
                LeafNode("c", "cold content")
            ])
        ])
        self.assertEqual(node.to_html(), "<p><b>bold content</b><div><c>cold content</c></div></p>")

if __name__ == '__main__':
    unittest.main()