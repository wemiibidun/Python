Write a function called unique_english_letters that takes the string word as a parameter. 
The function should return the total number of unique letters in the string. 
Uppercase and lowercase letters should be counted as different letters.
We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" #Makes a string of the letters in alphabet to count

# Write your unique_english_letters function here:
def unique_english_letters(word):
  counter = 0 #initializes counter
  for unique in letters: #creates loop to loop through the letters in the alphabet
     if unique in word: #If the letter in the alphabet is in the word....
       counter = counter + 1 #then increment the counter
  return counter


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
