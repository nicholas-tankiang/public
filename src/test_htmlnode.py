import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # props_to_html tests 
    def test_props_to_html(self):
        #func with no props, expecting empty
        node = HTMLNode("a", props=None)
        self.assertEqual(node.props_to_html(), "")

        # Test with one prop input, expecting one output
        node = HTMLNode("img", props={"src": "image.jpg"})
        self.assertEqual(node.props_to_html(), ' src="image.jpg"') 

        # Test with multiple props given
        node = HTMLNode("a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()