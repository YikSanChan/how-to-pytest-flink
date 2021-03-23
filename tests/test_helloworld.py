from tasks.helloworld.udf import add

def test_add():
    assert add(1,1) == 3
