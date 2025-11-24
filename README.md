Hash Function 1:
    This function just took the length of the stringData and added 67 to it. This was very inefficent with run time being around 12 seconds for both the title and quote hash table. The collusion count for each was a little bit above 112 million and each had an unused space of 73.

Hash Function 2:
    This function took the unicode for each char in the stringData and added them together. This was a little bit more efficent than the first one with runtime being around 10 seconds for both the title and quote hash table. The collision counter for the Title table was a little under 88 million while the Quote table was a little under 92 million with both having 73 unused space.

Hash Function 3:
    This function too the unicode for each char, multiplied it by a static num, then added the key to itself. This was very efficent with runtime being around 0.2 seconds for the Title and Quote tables. The collision counter for the Title table was around 1.44 million and the Quote table being around 1.35 million with both having 73 unused space.

Hash Function 4:
    This Function takes the set size of the Hash Tables and floor divides it by the unicode for each char and adds key. This was more efficent than the first two, but not as good as the third. The runtime for the Title table was 6.35 seconds and the time for the Quote table was 8.84 seconds. The collision counter for Title was around 60 million and Quote was around 84 million with both having 73 unused space.

Hash Function 5:
    This Function takes the length of stringData, multiplies it by two, and adds key for each char in stringData (loops it). The runtime for title was 9.98 seconds and quote was 9.19 seconds. The total collisions for title was around 94 million and quote was around 91.3 million with both having 73 unused space.