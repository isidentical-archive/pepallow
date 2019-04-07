# PEPAllow
![pepalllow](pepallow.png)
See what happens if a pep was accepted.
## Supporteds
- [PEP211](https://www.python.org/dev/peps/pep-0211/) - Adding A New Outer Product Operator
- [PEP231](https://www.python.org/dev/peps/pep-0231/) - \_\_findattr\_\_()
- [PEP276](https://www.python.org/dev/peps/pep-0276/) - Simple Iterator for ints
- [PEP313](https://www.python.org/dev/peps/pep-0313/) - Adding Roman Numeral Literals to Python
- [PEP336](https://www.python.org/dev/peps/pep-0336/) - Make None Callable
- [PEP377](https://www.python.org/dev/peps/pep-0377/) - Allow \_\_enter\_\_() methods to skip the statement body
## Usage
```py
from pepallow.allow import Allow

with Allow(313):
    assert IV == 4

with Allow(211):
    s = [1, 2, 3]
    t = "abc"
    for i, j in s @ t:
        pass
...
```
## How It Works
When you import `pepallow.allow`, it reimport your module then patch it with `pepallow.peps/*` items. The items uses power of the `AST` module cpython gave us.
