#Detect Floating Point Number
import re
for _ in range(int(input())):
    print (bool(re.match(r'^[-+\.]?[0-9]*\.[0-9]+$', input())))
   
   
#Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


#Group(), Groups() & Groupdict()
