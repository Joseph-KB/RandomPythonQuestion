# Generate a list of vowel words present in a user input word

vowel_list=['a','e','i','o','u']

word=input("Enter the word... ")

lis_1=[]

for i in word:
    if i in vowel_list:
        lis_1.append(i)

lis_1=list(set(lis_1))        # set is used to reduce count of vowel to one ..if multiple 'a' is present list should only give 'a' once


print(f"The vowel list of the {word} is: ",lis_1)