import pytest
from pepallow.allow import Allow
from pepallow.peps.p231 import AssetBean as Bean

def test_pep211():
    with Allow(211):
        assert IV == 4
        assert M == 1000
        assert (M - D) + VI == 506
        with pytest.raises(AssertionError):
            assert VI == 5
        

def test_pep231():
    with Allow(231):
        b = Bean(3)
        assert b.foo == 3
        b.foo = 4
        assert b.foo == 4

def test_pep313():
    with Allow(313):
        assert IV + I == V
        assert VI + M == 1006
        print(IV)
        print(M - DV)
    
    
