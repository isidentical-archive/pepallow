import ast

class HandledTransformer(ast.NodeTransformer):
    def __init__(self, handler, *args, **kwargs):
        self.handler = handler
        super().__init__(*args, **kwargs)
