a = int(input("Enter total number of soldiers in a circle :"))
b = list(bin(a))
c = ["0","b"]
for x in range(3,len(b)):
    c.append(b[x])
c.append(b[2]) 
d = int("".join(c),2)

print("Whoever happens to be at nummber {} in circle will survive.".format(d))
