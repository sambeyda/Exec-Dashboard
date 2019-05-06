#Testing for Executive Dashboard Project

from app.Monthly_sales import to_usd

def test_to_usd():
    #Tests whether number is returned with $ sign
    assert to_usd(4.50) == "$4.50"