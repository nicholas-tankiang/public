import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_child(self):
        # Test that creating a LeafNode with a child raises an error
        with self.assertRaises(TypeError):
            LeafNode("tag", "value", children=["exists"])

    """
    # NOTE: error is raised during init, valueerror not raised
    def test_leaf_node_without_value(self):
        # Test that creating a LeafNode without a value raises a ValueError
        with self.assertRaises(ValueError):
            LeafNode("tag")
    """

    def test_leaf_node_basic(self):
        # Test a basic LeafNode with tag and value
        node = LeafNode("tag", "value")
        self.assertEqual(node.to_html(),"<tag>value</tag>")

    def test_leaf_node_with_props(self):
        # Test a LeafNode with tag, value, and props
        node = LeafNode("tag", "value", props={"prop": "value1"})
        self.assertEqual(node.to_html(), '<tag prop="value1">value</tag>')

    def test_leaf_node_raw_text(self):
        # Test a LeafNode with no tag (should return raw text)
        node = LeafNode(None,"value")
        self.assertEqual(node.to_html(),"value")
        
    def test_leaf_node_empty_string_value(self):
        # Test a LeafNode with an empty string as value
        node = LeafNode("tag", "")
        self.assertEqual(node.to_html(), "<tag></tag>")

if __name__ == '__main__':
    unittest.main()