import ast
from pepallow import HandledTransformer

NUMBER = 211
SUPPRESS = (TypeError,)


class PEP211Transformer(HandledTransformer):
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
            if len(node.target.elts) < 2:
                raise ValueError(
                    f"Not enough values to unpack (expected 2, got {len(node.target.elts)})"
                )
            elif len(node.target.elts) > 2:
                raise ValueError("Too many values to unpack (expected 2)")

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
