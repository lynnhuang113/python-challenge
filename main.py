import os
import csv
budget_data = "budget_data.csv"

total_revenue = 0
total_months = 0
starting_revenue = 0
revenue_change = 0
greatest_increase =  0
greatest_decrease = 0
revenue_change = []
date = []
new_date = 0

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:  
        total_months  = total_months + 1
        total_revenue += int(row[1])
        date.append(row[0])
        
        revenue_change.append(int(row[1]) - starting_revenue)

        if ( int(row[1]) - starting_revenue > greatest_increase):
            greatest_increase = int(row[1]) - starting_revenue

        if ( int(row[1]) - starting_revenue < greatest_decrease):
            greatest_decrease = int(row[1]) - starting_revenue

        starting_revenue = int(row[1])
        
revenue_change.pop(0)   
new_date = []
months = []
years = []
for d in date:
    new_date.append(d.split('-'))
   
for k in new_date:
       months.append(k[0])
       years.append(k[1])

index_increase = revenue_change.index(greatest_increase)
index_decrease = revenue_change.index(greatest_decrease)
date_increase = months[index_increase + 1] + "-" + years[index_increase + 1]
date_decrease = months[index_decrease + 1] + "-" + years[index_decrease + 1]

analysis= "Financial Analysis"+'\n'+ \
"-" * 100 +'\n' +\
"Total Months: " + str(total_months)+'\n' +\
"Total Revenue: " + "$" + str(total_revenue)+'\n' +\
"Average Change: " + "$" + str(round(sum(revenue_change) / len(revenue_change),2))+'\n' +\
"Greatest Increase: " + date_increase + " ($" +  str(greatest_increase) + ")"+'\n' +\
"Greatest Decrease: " + date_decrease + " ($" +  str(greatest_decrease) + ")"
print(analysis)

with open(os.path.join(os.path.dirname(__file__),"pybank.txt"), "w") as file:
    file.write(analysis)
