import csv

with open("lesson_11/examples/data/cars.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

file_path = "lesson_11/davidhasenson/person.csv" #input("Enter path to file: ")
with open(file_path) as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        print(row)
