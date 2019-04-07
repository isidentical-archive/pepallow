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
        if (
            isinstance(node.target, ast.Tuple)
            and isinstance(node.iter, ast.BinOp)
            and isinstance(node.iter.op, ast.MatMult)
        ):
            if len(node.target.elts) != 2:
                raise ValueError("There is should be only 2 names to unpack.")
            a, b = node.target.elts
            return ast.For(
                target=a,
                iter=node.iter.left,
                body=[
                    ast.For(target=b, iter=node.iter.right, body=node.body, orelse=[])
                ],
                orelse=node.orelse,
            )
        return node
