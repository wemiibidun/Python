'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left. 

Where x, y and z are replaced with the actual calculated numbers. 

When you hit run, this is what should happen 👉 https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA

'''

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#There are 365 days in a year, 52 weeks in a year and 12 months in a year.

#Write your code below this line 👇
age = 90 - (int(age))
days = age * 365
weeks= age * 52
months= age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
