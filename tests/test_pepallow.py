import pytest
from pepallow.allow import Allow
from pepallow.peps.p231 import AssetBean as Bean

def test_pep211():
    with Allow(211):
        s = [1, 2, 3]
        t = "abc"
        
        product = []
        counter = 0
        for i, j in s @ t:
            product.append(f"{i}{j}")
            counter += 1
            
        assert counter == 9
        assert product == ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
        

def test_pep231():
    with Allow(231):
        b = Bean(3)
        assert b.foo == 3
        b.foo = 4
        assert b.foo == 4

def test_pep276():
    with Allow(276):
        counter = 0
        items = []
        for number in 10:
            items.append(number)
            counter += 1
            
        assert counter == 10
        assert sum(items) == 45

def test_pep313():
    with Allow(313):
        assert IV + I == V
        assert VI + M == 1006
        print(IV)
        print(M - DV)
    
    
