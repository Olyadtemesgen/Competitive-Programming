t = int(input())
 
for x in range(t):
    x = int(input())
 
    index = 0
    saved  = x
    while x:
 
        if x % 2:
            break
 
        index += 1
        x //= 2
    
    x //= 2
    
    if x:
 
        print(2 ** index)
    
    else:
        
        if index:
            print(1 + 2 ** index)
        
        else:
            aa = False
            index2 = 0
            
            while saved:
                
                if aa and saved % 2:
                    break
                
                elif saved % 2:
                    aa = True
                
                saved //= 2
                index2 += 1
            
            print(1 + 2 ** index2)
