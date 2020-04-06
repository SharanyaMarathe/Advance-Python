def find_target(aus,ind,aus2):
    return aus+aus2-ind+1

def test_case_01():
    aus1=250
    ind1=220
    aus2=150
    ind_trgt=find_target(aus1,ind1,aus2)
    exp=181
    assert exp==ind_trgt
def test_case_02():
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
