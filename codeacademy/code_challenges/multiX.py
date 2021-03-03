Write a function named count_multi_char_x that takes a string named word and a string named x. 
This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. 
However, this time, make sure your function works when x is multiple characters long.

For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word,x):
  multi_x = word.split(x)
  return (len(multi_x)-1 )

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
