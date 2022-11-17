# Count the occurance of each word in a line of text

string="This world is so beautifull, have you thought of another world "
string=string.replace(",","")       # more characters can be removed by using regualr expression
string=string.split()

dictonary=dict()

for word in string:
    word=word.lower()
    if word in dictonary:
        dictonary[word] += 1
    else:
        dictonary[word] = 1

print("A dictionary with count of words is obtained:  ",dictonary)