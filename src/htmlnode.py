class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # if props has None value, set it to empty list so it can be used in below func
        if self.props == None:
            props = {}
        else:
            # to not modify self.props, use props copy
            props = self.props

        # list comprehension so I can add initial whitespace
        string_list = " ".join(
            f'{key}="{value}"' for key, value in props.items()
            )
        # Return with a leading space if there are any attributes, else empty string
        return (f" {string_list}" if string_list else "")

    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")