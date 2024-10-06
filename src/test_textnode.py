import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    # test for not equal text
    def test_not_eq(self):
        node = TextNode("I am me", "none")
        node2 = TextNode("I am not me", "none")
        self.assertNotEqual(node, node2)
    
    #test for diff text_type
    def test_text_type(self):
        node = TextNode("same", "dif", "https://suckit.com")
        node2 = TextNode("same", "same", "https://suckit.com")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("yes", "yes", None)
        node2 = TextNode("yes", "yes", None)
        self.assertEqual(node, node2)

    def test_numbers(self):
        node = TextNode(12, 12)
        node2 = TextNode(12, 12)
        self.assertEqual(node, node2)
    
if __name__ == "__main__":
    unittest.main()