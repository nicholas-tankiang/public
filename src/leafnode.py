from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    # set props to optional in leaf's constructor
    def __init__(self, tag, value, props=None):
        # pass init's vars to parent class, but set children to None
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        #self.props_to_html
    

