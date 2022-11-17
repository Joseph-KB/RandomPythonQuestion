# Prompt the user for a list of integers. For all values greater than 100 store 'over' instead

# eval is a built in function of python which takes as it is in a code

value=eval(input("Enter the list in the format [0,1,2,3....,120,450] \n"))


# below given is a list comprehension which is similar to ternary operation
# ternary operation --->-----[if TRUE] if (condition) else [if FALSE]-------
lis_1=[i if i<100 else "over" for i in value]  

print("The converted list when element is more than 100 is : ",lis_1)


# Another method to store each input value
lis_2=[]

size=int(input("Enter the size of integer list: "))
for i in range(size):
    a=int(input(f"Enter the {i+1}th element....  "))
    if a<100:
        lis_2.append(a)
    else:
        lis_2.append("over")
print("The second method list is : ",lis_2)