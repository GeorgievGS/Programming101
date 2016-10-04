array = "T T T H T T T H T T T H H H H"
frequency = 1
best_numb = ""
best_frequency = 0

array = array.split(" ")

for x in range(1,len(array)):
    if array[x] != array[x-1]:
        if frequency > best_frequency:
            best_numb = array[x-1]
            best_frequency = frequency
            frequency = 1
        else:
            frequency = 1
            best_numb = array[x]
    else:
        frequency += 1


if frequency > best_frequency:
    best_frequency = frequency
    print("%s wins!" %best_numb)
elif frequency < best_frequency:
    print("%s wins!" %best_numb)
    
else:
    print("Draw!")



            
        
            
  

            
            
    
    
        
        

    
