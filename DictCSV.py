##################################################
###   Author      : Ahmed Gama                ####
###   Description : Dictionary of CSV file    ####
###                                           ####
###   Date        : 3 Dec 2020                ####
###   Version     : v1                        ####
##################################################
import csv
reader = csv.reader(open("csvfile.csv" , "r"))
mydict = dict()
for line in reader :
    mydict[line[1]] = {"first name":line[2],"last name":line[3],"nick name":line[0]}
print(mydict)
    