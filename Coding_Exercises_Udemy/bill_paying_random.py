'''
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

** names = names_string.split(", ") <-- this line breaks names into individual names and puts them inside a **List** called `names`. 

For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input

```
Angela, Ben, Jenny, Michael, Chloe
```
Note: notice that there is a space between the comma and the next name. 
# Example Output

```
Michael is going to buy the meal today!
```


# Hint

1. You might need the help of the `len()` function.   

2. Remember that Lists start at index 0!

'''

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
num_items = len(names)
name_index = random.randint(0, num_items -1)
name_select = names [name_index]

print(f"{name_select} is going to buy the meal today!")
