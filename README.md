# PEPAllow
![pepalllow](pepallow.png)
See what happens if a pep was accepted.
## Supporteds
- PEP211
- PEP231
- PEP313
## Demo
[![asciicast](https://asciinema.org/a/239257.svg)](https://asciinema.org/a/239257)
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
