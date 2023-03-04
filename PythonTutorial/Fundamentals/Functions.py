def printme( name ):
    print (name);
    return;
printme('My Name is Tony Stark');

# Keyword Arguments
def printinfo(name, age):
    print ("Name:", name);
    print ("Age:", age);
    return;
printinfo(age = 27, name = 'Tony Stark');

# Default Arguments
def printinfo1(name, age = 25):
    print ("Name:", name);
    print ("Age:", age);
    return;
printinfo1(age = 27, name = 'Tony Stark');
printinfo1(name = 'Pepper Pots');

# Return Statement
def stellarobjects(planets, moons):
    total = planets + moons;
    print ('Inside the Function:', total);
    return total;
total = stellarobjects(9, 200);
print ('Outside the Function:', total);

# Global & Local variables
avg = 0;
def average(total, count):
    avg = total/count;
    print ('Average inside the function:', avg);
    return avg;
average(100,50);
print ('Average outside the function:', avg);
