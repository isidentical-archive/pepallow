import ast
from pepallow import HandledTransformer

NUMBER = 276
SUPPRESS = (TypeError,)

class PEP276Transformer(HandledTransformer):
    """
    PEP276 => Iterator ints
    
    for n in 3:
        ...

    =>

    for n in range(3):
        ...
    """

    def visit_For(self, node):
        if isinstance(node.iter, ast.Num):
            if not isinstance(node.iter.n, int):
                raise TypeError("The number should be integer, not float / complex.")
            node.iter = ast.Call(ast.Name("range", ast.Load()), [node.iter], [])
        return node
