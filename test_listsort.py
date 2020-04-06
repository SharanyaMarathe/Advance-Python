import pytest
from sorting_list import sorting
inputs=[([1,3,5],[-2,3,8],sorted([1,3,5]+[-2,3,8]))]

@pytest.mark.parametrize('a,b,exp',inputs)
def test_sortedlist(a,b,exp):
    act= sorting(a,b)
    assert act==exp
'''def test_emptylist():
    a=[]
    b=[]
    output=sorting(a,b)
    exp=[]
    assert output==exp

def test_firstempty():
     a=[-1]
     b=[-1]
     output=sorting(a,b)
     exp=[-1,-1]
     assert output==exp
def test_secondempty():
     a=[11,58,145]
     b=[]
     output=sorting(a,b)
     exp=[11,58,145]
     assert output==exp
     
def test_doubledigits():
    a=[14,45,58]
    b=[-58,11,58,74]
    output=sorting(a,b)
    exp=[-58,11,14,45,58,58,74]
    assert output==exp

def test_negatives():
    a=[-58,-14,45]
    b=[-5,11,74]
    output=sorting(a,b)
    exp=[-58,-14,-5,11,45,74]
    assert output==exp

def test_equals():
    a=[45,45,45]
    b=[45,45,45]
    output=sorting(a,b)
    exp=[45,45,45,45,45,45]
    assert output==exp

def test_diffsizes():
    a=[-7,-5,-1,9,15]
    b=[-7,-5,-1,9,15]
    output=sorting(a,b)
    exp=sorted(a+b)
    assert output==exp
def test_overlaps():
    a=[-12,-2,18,78]
    b=[-12,-7,-2,1,9,15]
    output=sorting(a,b)
    exp=sorted(a+b)
    assert output==exp'''
    

