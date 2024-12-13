#Christopher Robles Serrano
#Module 11 Lab 3A
#12/11/2024
#This program writes to a csv file. We are writing students names and grades using programmer input.

import csv

#Creating a dictionary of data to import to a csv file.
myDictionary = [
    {'First Name' : 'John', 'Last Name' : 'Smith', 'Exam 1' : 100.1, 'Exam 2' : 90.67, 'Exam 3': 80},
    {'First Name' : 'Rebecca', 'Last Name' : 'Nancy', 'Exam 1' : 99, 'Exam 2' : 68, 'Exam 3': 19},
    {'First Name' : 'Christian', 'Last Name' : 'Jones', 'Exam 1' : 78, 'Exam 2' : 54.58, 'Exam 3': 56},
    {'First Name' : 'Amanda', 'Last Name' : 'Farms', 'Exam 1' : 90.2, 'Exam 2' : 90.34, 'Exam 3': 90}
    ]

#Opening grades2.csv to write to.
with open('grades2.csv', mode = 'w', newline = '') as myFile:
    #Creating our headers for formatting.
    headers = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

    #Dictionary writer to import myDictionary passing in myFile and our header values.
    writer = csv.DictWriter(myFile, fieldnames=headers)

    #Writing header and rows.
    writer.writeheader()
    writer.writerows(myDictionary)
    print('Data transfer successful!\n')

#Opening grades2.csv in read mode to check our data.
with open('grades2.csv', mode = 'r', newline='') as myFile:
    #Using a csv reader to read our file(myFile)
    reader = csv.reader(myFile)

    #Skipping the first line to get to our rows of data.
    header = next(reader)

    #For loop to assign each collumn of each row to a variable corresponding to its value.
    for row in reader:  
        fName, lName, exam1, exam2, exam3 = row
        #Converting from string to float
        exam1 = float(exam1)
        exam2 = float(exam2)
        exam3 = float(exam3)
        
        #Finding the average.
        average = (exam1 + exam2 + exam3)/3

        #Print to terminal a summary of our data.
        print(f'Student: {fName} {lName}\nExams: {exam1}, {exam2}, {exam3}\nAverage: {average:.2f}\n')


