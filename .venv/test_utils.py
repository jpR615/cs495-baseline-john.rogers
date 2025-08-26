def test_lowercaseString():
    assert utils.normalize("CarrOt") == "carrot"

def test_dashString():
    assert utils.normalize("young sheldon") == "young-sheldon"

def test_lowerCaseString_and_dashString():
    assert utils.normalize("Apples and Bananas") == "apples-and-bananas"