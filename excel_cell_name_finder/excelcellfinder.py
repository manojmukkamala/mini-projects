def getExCellName(n):
    
    if (n <= 0 or n > 17179869184):
        return('Cell Out Of Range')
    else:
        q, r = divmod(n, 16384)
        string = ''

        if (r == 0):
            return ('XFD' + str(q))

        else: 
            while (r > 0):
                r, rem = divmod(r - 1, 26)
                string = chr(65 + rem) + string
            return (string + str(q + 1))
            
            
##### Test Cases #######

print(getExCellName(1))            # Prints A1
print(getExCellName(17179869184))  # Prints XFD1048576
print(getExCellName(17179869185))  # Prints Cell Out Of Range
print(getExCellName(0))            # Prints Cell Out Of Range
print(getExCellName(-1))           # Prints Cell Out Of Range
print(getExCellName('Hello'))      # Prints Cell Out Of Range


