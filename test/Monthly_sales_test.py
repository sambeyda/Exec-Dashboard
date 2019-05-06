#Testing for Executive Dashboard Project

def test_to_usd():
    #Tests whether number is returned with $ sign
    assert to_usd(4.50) == "$4.50"