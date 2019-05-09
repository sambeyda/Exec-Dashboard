#Testing for Executive Dashboard Project

from app.Monthly_sales import to_usd, get_top_sellers
import os
import pandas
#Basic Challenge
def test_to_usd():
    #Tests whether number is returned with $ sign and two decimal places
    assert to_usd(10) == "$10.00"

    #Tests whether number rounds decimal places
    assert to_usd(10.33333333333333) == "$10.33"

    #Tests whether there is a thousand seperator
    assert to_usd(10000) == "$10,000.00"

#Intermediate Challenge
def test_get_top_sellers():
    # it should return a list of names and sales totals, sorted by sales ascending with top sellers first:
    file_name = "sales-201902.csv" #Example file
    file_path = os.path.join(os.path.dirname(__file__), file_name) #filepath
    monthly_data = pandas.read_csv(file_path) #read file-path
    results = get_top_sellers(monthly_data) #invoke function
    expected_result = [
        {'name': 'Button-Down Shirt', 'monthly_sales': 6179.75},
        {'name': 'Super Soft Hoodie', 'monthly_sales': 2175.0},
        {'name': 'Super Soft Sweater', 'monthly_sales': 1349.91},
        {'name': 'Khaki Pants', 'monthly_sales': 1335.0},
        {'name': 'Vintage Logo Tee', 'monthly_sales': 414.70},
        {'name': 'Sticker Pack', 'monthly_sales': 225.0},
        {'name': 'Winter Hat', 'monthly_sales': 168.34999999999997}, #Adjustment for pytest to work
        {'name': 'Brown Boots', 'monthly_sales': 125.0}
    ]
    assert results == expected_result #Make sure top sellers data is correct