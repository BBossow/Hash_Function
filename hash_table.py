# Author: Bruce Bossow
# Date: 11/14/25
# COS 226

# HW 5 Hash Table

import csv
import time

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

def openFile(file):
    data = []
    with open(file, 'r', newline = '', encoding = "utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append(row)
    return data

def main():
    # create empty hash table
    size = 15068
    hashTitleTable = [None] * size

    hashQuoteTable = [None] * size

    collisions = 0
    unusedSpace = 0

    movieNames = []
    counter = 0

    file = "MOCK_DATA.csv"
    reader = openFile(file)

    #TIME STATISTIC
    start = time.time()
    for row in reader:
        placed = False
        # create a DataItem from row
        movie = DataItem(row)
        movieNames.append(movie.movie_name)
        #print(movie.movie_name)
        #print(row[0])

        # feed the appropriate field into the hash function to get a key
        titleKey = hashFunction(movie.movie_name)

        # mod the key value by the hash table length
        loc = titleKey % len(hashTitleTable)
        # try to insert DataItem into hash table
        while placed != True:
            if hashTitleTable[loc] == None:
                #print(movie.movie_name + " " + str(loc))
                hashTitleTable[loc] = movie.movie_name
                placed = True
            else:
                # If this code runs then there was a collision, can track number of collisions with this 
                collisions += 1
                loc += 1
        
                
        # handle any collisions 

    end = time.time()
    print(f"{end-start:0.2f} seconds")
    print(f"number of collisions = {collisions}")
    #print(hashTitleTable[0:1000])
    #print(hashTitleTable)
    for titles in hashTitleTable:
        if titles == None:
            unusedSpace += 1
    print(f"Unused Space = {unusedSpace}")



if __name__ == "__main__":
    main()