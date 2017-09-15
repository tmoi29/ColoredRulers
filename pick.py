import csv
import sys
import random

occupations  = open("occupations.csv", "r")
jobs = csv.reader(occupations)
dictionary = {"Jobs":"" , "Percent":""}
classes = []
percent = []

for row in jobs:
    try:
        classes.append(row[0])
        percent.append(float(row[1]))
    except:
        pass 
dictionary["Jobs"] = classes
dictionary["Percent"] = percent

def random_job():
    """generate a random number, add the percents, last one
     to go over is the desired job"""
    num = randint(0,
