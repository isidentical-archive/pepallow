import ast
from pepallow import HandledTransformer

NUMBER = 336
SUPPRESS = (TypeError,)

NoneType = ast.Assign(
    [ast.Name("__None", ast.Store())],
    ast.Call(
        ast.Call(
            func=ast.Name(id="type", ctx=ast.Load()),
            args=[
                ast.Str(s="NoneType"),
                ast.Tuple(elts=[], ctx=ast.Load()),
                ast.Dict(
                    keys=[
                        ast.Str(s="__slots__"),
                        ast.Str(s="__repr__"),
                        ast.Str(s="__bool__"),
                        ast.Str(s="__call__"),
                    ],
                    values=[
                        ast.List(elts=[], ctx=ast.Load()),
                        ast.Lambda(
                            args=ast.arguments(
                                args=[ast.arg(arg="s", annotation=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=ast.Str(s="None"),
                        ),
                        ast.Lambda(
                            args=ast.arguments(
                                args=[ast.arg(arg="s", annotation=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=ast.Num(n=0),
                        ),
                        ast.Lambda(
                            args=ast.arguments(
                                args=[ast.arg(arg="s", annotation=None)],
                                vararg=ast.arg(arg="a", annotation=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=ast.arg(arg="k", annotation=None),
                                defaults=[],
                            ),
                            body=ast.Name(id="s", ctx=ast.Load()),
                        ),
                    ],
                ),
            ],
            keywords=[],
        ),
        [],
        [],
    ),
)


class PEP336Transformer(HandledTransformer):
    def visit_NameConstant(self, node):
        if node.value is None:
            if "ntx" not in self.handler._inserteds:
                self.handler.set_global("ntx", NoneType)

            return ast.Name("__None", ast.Load())
        return node
