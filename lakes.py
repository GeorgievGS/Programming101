count = 0
level = 0
array = "ddhhuu"
result = 0

for x in array:
    if level <= 0:
        if x == "d":
            level -= 1
            count += 1
            result += 0.5 + count - 1
            print("l,c,r",level,count,result)
        elif x == "u":
            level += 1
            count -= 1
            if count >= 0:
                result += 0.5 + count
            print("l,c,r",level,count,result)
        elif x == "h":
            level += 0
            result += count
            print("l,c,r",level,count,result)

    else:
        count = 0
        if x == "u":
            level += 1
            print("l,c,r",level,count,result)
        elif x == "d":
            level -= 1
            print("l,c,r",level,count,result)
        elif x == "h":
            level += 0
            print("l,c,r",level,count,result)
            
print(result * 1000)         

 

    
     
