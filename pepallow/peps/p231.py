import ast
from pepallow import HandledTransformer


class PEP231Transformer(HandledTransformer):
    def visit_Attribute(self, node):
        name = node.value
        attr = node.attr
        ctx = node.ctx
        
        if isinstance(ctx, ast.Load):
            node = ast.IfExp(
                ast.Call(ast.Name("hasattr", ast.Load()), [name, ast.Str("__findattr__")], []),
                ast.Call(ast.Attribute(name, "__findattr__", ast.Load()), [ast.Str(attr)], []),
                orelse=ast.Attribute(name, attr, ctx),
            )
        
        return node

    def visit_Assign(self, node):
        if all(isinstance(target, ast.Attribute) for target in node.targets):
            target = node.targets.pop()
            name = target.value
            attr = target.attr
            ctx = target.ctx
            
            node = ast.Expr(ast.IfExp(
                ast.Call(ast.Name("hasattr", ast.Load()), [name, ast.Str("__findattr__")], []),
                ast.Call(ast.Attribute(name, "__findattr__", ast.Load()), [ast.Str(attr), node.value], []),
                orelse=ast.Call(ast.Name("setattr", ast.Load()), [name, ast.Str(attr), node.value], []),
            ))
            
        return node


class AssetBean:
    """
    Directly copied from https://www.python.org/dev/peps/pep-0231/
    """
    def __init__(self, x):
        self.__myfoo = x

    def __findattr__(self, name, *args):
        if name.startswith("_"):
            if args:
                setattr(self, name, args[0])
            else:
                return getattr(self, name)
        else:
            if args:
                name = "_set_" + name
            else:
                name = "_get_" + name
            return getattr(self, name)(*args)

    def _set_foo(self, x):
        self.__myfoo = x

    def _get_foo(self):
        return self.__myfoo
