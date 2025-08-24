from src.math_operations import add, sub

def test_add():
    assert add(5,3)==8
    assert add(2,7)==9
    assert add(3,3)==6

def test_sub():
    assert sub(4,2)==2
    assert sub(3,5)==-2
    assert sub(8,8)==0