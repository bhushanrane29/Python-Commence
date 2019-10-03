"""
The Josephus problem is a highly addictive conundrum if ever there was one.
A relatively well-known arithmetical puzzle that crops up regularly in 
popular mathematics and even computer science, 
it is part of the family of decimation problems. 
The somewhat bloody origin1 of this word makes perfect sense
in the context of the Josephus problem. The problem statement is
very simple: 41 people are standing in a circle and a starting point is chosen.
Starting with this person, we count 1, 2, and the third person is removed.
2 The process continues: 1, 2, and the third person is removed.
The first people to leave the circle are therefore numbered 3, 6, 9 and 12.
The same process is repeated around the circle (Figure 2a). Notice that after 
one full circle, empty places appear, which complicates matters. 
Here are the numbers of the unlucky losers, in the order of their elimination. 
 
 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 1, 5, 10, 14, 19, 23, 28...  
 
The question is: 
Where to stand in the circle to be last survivor? In other words, what will be last remaining number in the circle? 
 
"""


#For any number of people in circle using only Python list and for loop

a = int(input("Enter total number of soldiers in a circle :"))
b = list(bin(a))
c = ["0","b"]
for x in range(3,len(b)):
    c.append(b[x])
c.append(b[2]) 
d = int("".join(c),2)

print("Whoever happens to be at nummber {} in circle will survive.".format(d))
