# Store a list of first names. Count the occurance of 'a' within the list


lis_1=["joseph","aswin","akhil","jishnu","anandhu"]

count=0

for fname in lis_1:
    a=fname.count("a")
    count+=a

print(f"The count of letter \"a\" in  the given list of firstname is: {count}")