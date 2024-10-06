from textnode import TextNode
from htmlnode import HTMLNode

def main():
    test_node = TextNode("blabla", "bold", "https://goog.com")
    print(repr(test_node))
    test_html = HTMLNode("href", "value", props={"href": "https://"})
    print(repr(test_html))
main()