import pytest

@pytest.fixture(params=["SSH","AWS"])
def setup_connection(request):
    print("\n****connected to a server")
    def fin():
        print("\n****closing connection")

    request.addfinalizer(fin)
    return request.param
              
def is_palindrome(x):
    return x[::-1]==x

test_strings=[("madam",True),("carrom",False),("abcddcba",True)]

@pytest.mark.parametrize('string,exp',test_strings)
@pytest.mark.usefixtures("setup_connection")
#def test_palindromes(setup_connection,string,exp):
def test_palindromes(string,exp):
    act= is_palindrome(string)
    assert act==exp
    
'''def test_palindromes():
     for string ,exp in test_strings:
         print("Testing: ",string)
         act= is_palindrome(string)
         assert act==exp'''
