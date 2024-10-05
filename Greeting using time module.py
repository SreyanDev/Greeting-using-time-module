#Check out the README.md file before running this.

name = str(input("What is your name: "))   #Asking the user the name and storing in the name variable or var.

import time                                     #Importing time module to get real world time.

hours = int(time.strftime("%H"))                #Assigning hours and type casting it from string to interger.

minitues = int(time.strftime("%M"))             #Assigning hours and type casting it from string to interger.

seconds = int(time.strftime("%S"))              #Assigning hours and type casting it from string to interger.

print(f"\nTime is {hours}:{minitues}:{seconds}.\n")          #Printing the full time.

if hours >= 1 and hours < 12:                   #Coditions for detecting wheather it is morning or afternoon or evening.

    print(f"Good morning {name}!")

elif hours >=12 and hours < 4:

    print(f"Good afternoon {name}!")

elif hours >=4 and hours < 6:

    print(f"Good evening {name}!")

else:

    print(f"Good night {name}!")                #If it is not either of those then  is night.
