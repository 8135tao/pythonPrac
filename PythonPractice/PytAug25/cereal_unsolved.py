import os
import csv

#cereal_csv = os.path.join("../PytAug25", "cereal_bonus.csv")
cereal_csv = os.path.join("cereal_bonus.csv")

with open(cereal_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    csv_header = next(csvreader)    
#    print(f"CSV Header: {csv_header}")
    
#    next(csvreader, None)
    for row in csvreader:
        fiber = float(row[7])
        if fiber> 5:
            print(row)