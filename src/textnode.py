class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, that_textnode):
        if (
            self.text == that_textnode.text and
            self.text_type == that_textnode.text_type and
            self.url == that_textnode.url
        ):
            return True
        else:
            return False

    # note to self: repr only stores a string, it doesn't print
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")