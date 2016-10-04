n = input("How many bottles?")
n = int(n)
cordinates = []
distance = 0

if n < 0:
    print("Enter positive number")
else:
    while n > 0:
        x,y = map(int, input("Enter x,y:").split(" "))
        (x,y) = x,y
        if x < 0 or y < 0:
            print("Enter positive cordinates!")
        else:
            cordinates += [(x,y)]
        n -= 1
cordinates = sorted(cordinates,key = lambda x: (x[0],x[1]))

for char in range(len(cordinates) - 1):
    for ch in range(2):
        distance += cordinates[char + 1][ch] - cordinates[char][ch]

print (distance)
