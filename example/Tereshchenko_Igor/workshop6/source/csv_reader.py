import csv
input_file = 'data/orders.csv'
import re
try:
   with open(input_file, encoding="utf-8", mode='r') as file:


       csv_reader = csv.reader(file, delimiter=',')
       line_number = 0
       for row in csv_reader:
           print(row)
           line_number += 1

except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))