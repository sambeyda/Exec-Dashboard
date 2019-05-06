

###Imported Modules

import os
import pandas 
import matplotlib.pyplot as plt #Nomenclature taken from Professor's alternative solution: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py
import matplotlib.ticker as ticker
import csv
import operator


### Introducing User to the executive dashboard
print("--------------------")
print ("Welcome to Sam's executive dashboard tool! Here we will analyze your sales data.")
print("--------------------")
print("Before using, please have your sales data in a folder title 'Data' ")
print("--------------------")
###


## User inputs CSV files...Looked at the TA's code for inspiration: https://github.com/hiepnguyen034/data_dashboard
while True:
    year = input("Please enter the year of the sales data year in the form of YYYY: ")
    if year == "DONE": ## Validation requirement to prevent further code execution
        exit() ## TODO: Make this exit entire script!
    else:
        month = input("Please enter the month of the sales data in the form of MM: ")
        file_name = "Data/sales-"+ year+month+".csv" ## Finding csv file in data sub-directory
        if not os.path.isfile(file_name): ## Check if file is found with given inputs
            print("Sorry! Your chosen file cannot be found with the current input. Please try again or enter 'DONE' for year to exit")
        else:
            break ## Move on 

##

##adapted from Pandas exploration exercise: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_explore.py
def month_converter(month_code):
	full_months= {'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return full_months[month_code]

month_name_in_full  = month_converter(month)
##

##READING CSV FILE
monthly_data=pandas.read_csv(file_name) ##Read CSV 
monthly_total = monthly_data["sales price"].sum() # Sum of the column in csv file titles "Sales Price"
print("------------------")
print(month_name_in_full+ " " + year + " Sales Total: $" + "{0:,.2f}".format(monthly_total)) #Dashboard sales result. Used month converter function to display month name, and USD syntax for dollar formatting
products = monthly_data["product"]
#Top products formation
unique_products = products.unique() ## Adapted from Professor alternative solution
unique_products = unique_products.tolist()
top_sellers = [] # Create list for top seller output
# filering approach adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
for p in unique_products:
    row = monthly_data[monthly_data["product"] == p ] 
    sales_by_product = row["sales price"].sum()
    top_sellers.append({"name": p, "monthly_sales": sales_by_product})
#Sorting the list of top sellers by variable of "monthly_sales"
top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True) ##
print("------------------")
print("Top Selling Products:")
#Printing text of top sellers
Tracker = 1
for d in top_sellers:
    print("  " + str(Tracker) + ": " + str(d["name"]) + ": $" + "{0:,.2f}".format(d["monthly_sales"])) ###converted float to string
    Tracker = Tracker + 1

print("------------------")
##


##CHART OUTPUT BEGINS: Inspiration from professor's alternative solution! https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py
print("Visualizing the data....Please exit graph for script to end properly")

products_sorted = []
monthly_sales_sorted = []

for s in top_sellers:
    products_sorted.append(s["name"]) ##Retrieve names
    monthly_sales_sorted.append(s["monthly_sales"]) ##Retrieve sales totals


 ###Attempted to get bar chart to sort in descending order with .sort, however then the products did not match sales
    ###Tried to consult matplotlib and the internet for help, but after multiple hours of trying this, I've given up
products_sorted.reverse()
monthly_sales_sorted.reverse()


fig,ax = plt.subplots() 
### Adapted from Stackoverflow thread website: https://stackoverflow.com/questions/38152356/matplotlib-dollar-sign-with-thousands-comma-tick-labels
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.xaxis.set_major_formatter(tick) 
plt.barh(products_sorted, monthly_sales_sorted)
plt.xlabel("Sales in USD")
plt.ylabel("Product Name")

#####GOT RID OF THIS BECAUSE LABELS DID NOT CORRESPOND WITH CORRECT PRODUCT!!!!!!
### Adapted from stackoverflow thread 
# https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
# for i, v in enumerate(monthly_sales_sorted):
#     ax.text(v + 3, i + .25, str(tick(v)), color='blue', fontweight='bold') #Displays each bar chart's value


plt.title("Top Selling Products in " + month_name_in_full + " " + year)
plt.tight_layout()
plt.show()
print("--------------------")
print("Hope Sam's Executive Dashboard tool was able to provide your necessary insight!")
exit() #END SCRIPT

###
