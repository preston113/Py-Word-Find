import random

#user will input words
words = ["car", "dog", "bat"]

 
#this will be user input with validation with error explanation
rows = 5
columns = 5
#creating list for rnadom letters
ABC_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# to initializing matrix 
res = [ [ ABC_list[random.randint(0, 25)] for i in range(columns) ] for j in range(rows) ] 

#setting words
for word in words:
    res[1][2] = word[0]
    res[1][3] = word[1]
    res[1][4] = word[2]
# formmating the output by removing the commas and qoutes
for i in res:
    str_i = str(i)
    format_str = str_i.replace(',', ' ')
    format_str = format_str.replace('\'', '')
    print(format_str)

# demo commit