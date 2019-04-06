import ast


class PEP211Transformer(ast.NodeTransformer):
    """
    PEP211 => Adding A New Outer Product Operator
    
    for (i, j) in S @ T:
        pass
        
    =>
    
    for i in S:
        for j in T:
            pass
    """

    def visit_For(self, node):
        if isinstance(node.iter, ast.BinOp) and isinstance(node.iter.op, ast.MatMult):
            node.iter = ast.Call(
                ast.Name("zip", ast.Load()), [node.iter.left, node.iter.right], []
            )
        return node
