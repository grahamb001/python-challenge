import csv
import os
import pandas as pd

months = 0
totalNet = 0

budgetDataCsv = os.path.join("Resources", "budget_data.csv")

with open(budgetDataCsv, 'r') as csvfile:
    budgetData = pd.read_csv(csvfile, delimiter=',')
    #header = next(budgetData)

    for row in budgetData:
        months = budgetData["Revenue"].count()
        totalNet = budgetData["Revenue"].sum()
        averageChange = round(budgetData["Revenue"].mean(), 2)
        maxRevenue = budgetData["Revenue"].max()
        indate = budgetData.loc[budgetData["Revenue"] == maxRevenue, "Date"]
        increaseDate = indate.iloc[0]
        minRevenue = budgetData["Revenue"].min()
        decDate = budgetData.loc[budgetData["Revenue"] == minRevenue, "Date"]
        decreaseDate = decDate.iloc[0]

    print("Financial Analysis")
    print("--------------------------------------------")
    print("Total Months: " + str(months))
    print("Total: " + "$" + str(totalNet))
    print("Average Change: " + "$" + str(averageChange))
    print("Greatest Increase in Profits: " + str(increaseDate) + " ($" +  str(maxRevenue) + ")") 
    print("Greatest Decrease in Profits: " + str(decreaseDate) + " ($" +  str(minRevenue) + ")")

with open("FinancialAnalysis.txt", "w") as text_file:
        text_file.write("Financial Analysis         "
        "Total Months: " + str(months) + "      "
        +"Total: $" + str(totalNet)+ "      "          
        +"Average Change: " + "$" + str(averageChange)+ "     "           
        +"Greatest Increase in Profits: " + str(increaseDate) + " ($" +  str(maxRevenue) + ")"+ "      "           
        +"Greatest Decrease in Profits: " + str(decreaseDate) + " ($" +  str(minRevenue) + ")")          
