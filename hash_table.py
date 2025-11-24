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

def openFile(file):
    data = []
    with open(file, 'r', newline = '', encoding = "utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append(row)
    return data

#first Hash Function
#number of collisions = 112194921
# time = 18
def hashFunction(stringData):
    # takes the length of string data and adds 67
    key = len(stringData) + 67

    return key

#second Hash function
# number of collisions = 87842862
# time = 12.07
def hashFunction2(stringData):
    # takes the unicode for each char in string data and adds them together
    key  = 0
    for char in stringData:
        # takes the unicode for each char to make the key
        key += ord(char)

    return key 

def hashFunction3(stringData):
    # takes the unicode for each char in string data, adds them together, then multiplies the total by length of string data
    key  = 0
    num = 31
    for char in stringData:
        # takes the unicode for each char to make the key
        key = ord(char) * num + key

    return key 

def main():
    # create empty hash table's
    size = 15073
    hashTitleTable = [None] * size
    hashQuoteTable = [None] * size

    # variables for stat tracking
    collisions = 0
    unusedSpace = 0

    file = "MOCK_DATA.csv"
    reader = openFile(file)

    ### TITLE HASH TABLE

    #TIME STATISTIC
    start = time.time()
    for row in reader:
        # create a DataItem from row
        movie = DataItem(row)

        # feed the appropriate field into the hash function to get a key
        titleKey = hashFunction3(movie.movie_name)

        # mod the key value by the hash table length
        loc = titleKey % size

        # try to insert DataItem into hash table
        while True:
            if hashTitleTable[loc] is None:
                #print(movie.movie_name + " " + str(loc))
                hashTitleTable[loc] = movie.movie_name
                break
            # If this code runs then there was a collision, can track number of collisions with this 
            collisions += 1
            loc = (loc + 1) % size
        
                
        # handle any collisions 

    end = time.time()
    print("Title Hash Table")
    #print("Quote Hash Table")
    print(f"{end-start:0.2f} seconds")
    print(f"number of collisions = {collisions}")
    
    for titles in hashTitleTable: # hashTitleTable  hashQuoteTable
        if titles == None:
            unusedSpace += 1
    print(f"Unused Space = {unusedSpace}\n")

    #reset the stats for the quote table
    unusedSpace = 0
    collisions = 0

    ### QUOTE HASH TABLE

    start = time.time()
    for row in reader:
        # create a DataItem from row
        movie = DataItem(row)

        # feed the appropriate field into the hash function to get a key
        quoteKey = hashFunction3(movie.quote)

        # mod the key value by the hash table length
        loc = quoteKey % size

        # try to insert DataItem into hash table
        while True:
            if hashQuoteTable[loc] is None:
                hashQuoteTable[loc] = movie.quote
                break
            # If this code runs then there was a collision, can track number of collisions with this 
            collisions += 1
            loc = (loc + 1) % size

    end = time.time()
    print("Quote Hash Table")
    print(f"{end-start:0.2f} seconds")
    print(f"number of collisions = {collisions}")
    
    for titles in hashQuoteTable:
        if titles == None:
            unusedSpace += 1
    print(f"Unused Space = {unusedSpace}")



if __name__ == "__main__":
    main()