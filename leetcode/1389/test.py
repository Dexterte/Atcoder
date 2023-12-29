import production


def test_1():
    res = production.Solution.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
    assert res == [0, 4, 1, 3, 2]

def test_2():
    res = production.Solution.createTargetArray([1], [0])
    assert res == [1]

test_1()
test_2()