from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    # set props to optional in leaf's constructor
    def __init__(self, tag, value, props=None):
        # pass init's vars to parent class, but set children to None
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        if self.props:
            props_string = self.props_to_html()
        else:
            props_string = ""
        
        # if props_string exist, add a space, else don't add space
        # ex: with props
        # <tag prop1="value1" prop2="value2">value</tag>
        # no props
        # <tag>value</tag>
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
        

    

