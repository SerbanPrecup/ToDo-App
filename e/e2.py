import csv

with open("wheater.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a City: ")

for row in data:
    if row[0] == city:
        print(row[1])