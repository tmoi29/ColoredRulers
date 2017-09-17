import csv
import sys
import random

occupations  = open("occupations.csv", "r")
jobs = csv.reader(occupations)
dictionary = {"Jobs":"" , "Percent":""}
job_type = []
percent = []

for row in jobs:
    try:
        job_type.append(row[0])
        percent.append(float(row[1]))
    except:
        pass 
dictionary["Jobs"] = job_type
dictionary["Percent"] = percent

def random_job():
    """generate a random number, add the percents, last one
     to go over is the desired job"""
    num = random.random()*100
    i=-1
    while num>0:
        i+=1
        num-=dictionary["Percent"][i]
    return dictionary["Jobs"][i]
        
print(random_job())
