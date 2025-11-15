# Author: Bruce Bossow
# Date: 11/14/25
# COS 226

# HW 5 Hash Table

import csv

class DataItem:
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_date = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.min_duration = line[6]
        self.production_company = line[7]
        self.quote = line[8]

def hashFunction(stringData):
    # do things to stringData, turn it into int
    key = len(stringData) + 67

    return key
# create empty hash table
size = 20000
hashTitleTable = [None] * size

hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"
counter = 0

with open(file, 'r', newline = '', encoding = "utf8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        # create a DataItem from row
        movie = DataItem(row)
        #print(movie.movie_name)

        # feed the appropriate field into the hash function to get a key
        titleKey = hashFunction(movie.movie_name)

        # mod the key value by the hash table length
        loc = titleKey % len(hashTitleTable)
        # try to insert DataItem into hash table
        hashTitleTable[loc] = movie.movie_name
        # handle any collisions 
        counter += 1

print(counter)