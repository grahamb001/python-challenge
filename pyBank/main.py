import csv
import os
import pandas as pd

months = 0
totalNet = 0

budgetDataCsv = os.path.join("Resources", "budget_data.csv")

with open(budgetDataCsv, 'r') as csvfile:
    budgetData = pd.read_csv(csvfile, delimiter=',')

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

f = open("FinancialAnalysis.txt", "w")
f.write("Financial Analysis"+ "\n")
f.write("--------------------------------------------" +"\n")
f.write("Total Months: " + str(months)+ "\n")
f.write("Total: $" + str(totalNet)+ "\n")    
f.write("Average Change: " + "$" + str(averageChange)+ "\n")          
f.write("Greatest Increase in Profits: " + str(increaseDate) + " ($" +  str(maxRevenue) + ")"+ "\n")           
f.write("Greatest Decrease in Profits: " + str(decreaseDate) + " ($" +  str(minRevenue) + ")")          
f.close()