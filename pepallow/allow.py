import ast
import sys
from contextlib import suppress, ExitStack
from pepallow.peps import PEPS


class TreeHandler:
    def __init__(self, tree):
        self.tree = tree
        self._inserteds = set()

    def set_global(self, itemid, item):
        self._inserteds.add(itemid)
        self.tree.body = [item] + self.tree.body  # self.tree.body.insert(0, item)


class PEPTransformer(ast.NodeTransformer):
    def visit(self, tree):
        if isinstance(tree, ast.Module):
            self.handler = TreeHandler(tree)

        return super().visit(tree)

    def visit_With(self, node):
        if (
            isinstance(node.items[0].context_expr, ast.Call)
            and isinstance(node.items[0].context_expr.func, ast.Name)
            and node.items[0].context_expr.func.id == "Allow"
        ):
            pep = node.items[0].context_expr.args[0].n
            new_node = PEPS[pep]["transformer"](self.handler).visit(node)
            ast.copy_location(new_node, node)
            ast.fix_missing_locations(new_node)

        return node


class Allow(ExitStack):
    def __init__(self, pep, *args, **kwargs):
        self.pep = pep
        super().__init__(*args, **kwargs)

    def __enter__(self):
        super().__enter__()
        for exc in PEPS[self.pep]["suppress"]:
            self.enter_context(suppress(exc))


def allow():
    main = __import__("__main__")
    main_ast = ast.parse(open(main.__file__).read())
    transformer = PEPTransformer()
    main_ast = transformer.visit(main_ast)
    ast.fix_missing_locations(main_ast)
    exec(compile(main_ast, main.__file__, "exec"), main.__dict__)


allow()
