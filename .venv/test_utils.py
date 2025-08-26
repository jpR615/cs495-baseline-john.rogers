def test1():
    assert utils.normalize("CarrOt") == "carrot"

def test2():
    assert utils.normalize("young sheldon") == "young-sheldon"

def test3():
    assert utils.normalize("Apples and Bananas") == "apples-and-bananas"