# While Statement
days = 1;
while (days < 8):
    print ('The day is:', days);
    days = days + 1;
    
print ('Week Complete');

# For Loop
for letter in 'Tesla':
    print ("Current Letter:", letter);
  
models = ['model S', 'model X', 'model 3'];
for model in models:
    print ('Available Models:', model);
    
for i in range(1,10):
    print (i);
    
# Break Statement 
for i in range(1,10):
    if (i == 6):
        break;
    print (i);
 
# Continue Statement
for i in range(1,10):
    if (i == 6):
        continue;
    print (i);
    
