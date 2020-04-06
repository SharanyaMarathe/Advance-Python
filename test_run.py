def setup_module(module):
    print("inside setup module")

def teardown_module(module):
     print("tearing down module")
     
'''def setup_function(func):
     print("creating base file",func.__name__)
    
def teardown_function(func):
     print("deletting base file",func.__name__)'''
     

def find_target(aus,ind,aus2):
    return aus+aus2-ind+1


class Testruns:
    @classmethod
    def setup_class(cls):
        print("creating base file",cls.__name__)   #for whole class, any one is enough(class or method)

    @classmethod
    def teardown_class(cls):
         print("deletting base file",cls.__name__)
        
    '''def setup_method(self,cls):
        print("creating base file",cls.__name__)
    
    
    def teardown_method(self,cls):
         print("deletting base file",cls.__name__)''' # for each method

    def test_with_base_file(self):
        print("Test File")
           

    def test_case_01(self):
        aus1=250
        ind1=220
        aus2=150
        ind_trgt=find_target(aus1,ind1,aus2)
        exp=181
        assert exp==ind_trgt
    def test_case_02(self):
        aus1=25
        ind1=22
        aus2=150
        ind_trgt=find_target(aus1,ind1,aus2)
        exp=154
        assert exp==ind_trgt
        
def test_case_03():
     aus1=200
     ind1=20
     aus2=100
     ind_trgt=find_target(aus1,ind1,aus2)
     exp=281
     assert exp==ind_trgt
