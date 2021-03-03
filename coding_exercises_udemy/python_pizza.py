'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

# Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

# Example Output

```
Your final bill is: $28.
```
When you hit run, this is what should happen 👉 https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4

'''

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill = bill + 3
  else:
    bill  

if size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill = bill + 3
  else:
    bill 

if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill = bill + 2
  else:
    bill      

if  extra_cheese == "Y":
  bill = bill + 1 
else:
  bill

print(f"Your final bill is ${bill}")
