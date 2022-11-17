#Generate a list of ordinal value for an user input word

word=input("Enter the word..... ")

ord_lis=[ord(i) for i in word]

print(f"The ordinal values of the word \"{word}\" is...",ord_lis)   # \ is used to represent as raw string/character
