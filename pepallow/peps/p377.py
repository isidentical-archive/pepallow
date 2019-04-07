import ast
from pepallow import HandledTransformer

NUMBER = 377
SUPPRESS = (NameError,)

class PEP377Transformer(HandledTransformer):
    def visit_Name(self, node):
        if node.id == "StatementSkipped" and ("stk" not in self.handler._inserteds):
            self.handler.set_global(
                "stk",
                ast.Assign(
                    [ast.Name("StatementSkipped", ast.Store())],
                    ast.Call(
                        ast.Name("type", ast.Load()),
                        [
                            ast.Str(node.id),
                            ast.Tuple([ast.Name("Exception", ast.Load())], ast.Load()),
                            ast.Dict([], []),
                        ],
                        [],
                    ),
                ),
            )

        return node

    def visit_With(self, node):
        if (
            isinstance(node.items[0].context_expr, ast.Call)
            and isinstance(node.items[0].context_expr.func, ast.Name)
            and node.items[0].context_expr.func.id == "Allow"
        ):
            self.generic_visit(node)
            return node

        if len(node.items) == 1:
            assign = (
                ast.Pass()
                if node.items[0] is None
                else ast.Assign(
                    [node.items[0].optional_vars],
                    ast.Name("StatementSkipped", ast.Load()),
                )
            )
            node = ast.Try(
                [node],
                [
                    ast.ExceptHandler(
                        type=ast.Name("StatementSkipped", ast.Load()),
                        name=None,
                        body=[assign],
                    )
                ],
                [],
                [],
            )

        return node
