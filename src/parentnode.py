from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        # Checks if the `children` list is empty or None
        if not self.children:  
            raise ValueError("ParentNode must have at least one child")
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        string_list = []
        for this_child in self.children:
            string_list.append(this_child.to_html())             
        joined_list = ''.join(string_list)
        
        return f"<{self.tag}>{joined_list}</{self.tag}>"
