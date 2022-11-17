# Generate positive list from a given list of integers

size=int(input("Enter the size of integer list... "))
array=[]       # for input list having integers

extracted_array=[]  # this extracts postive numbers from the list

converted_array=[]  # this converts integer to positive number

for i in range(size):
    element=int(input(f"Enter the {i+1}th element of array.    "))
    array.append(element)

for i in array:
    if i>=0:
        extracted_array.append(i)
    j=abs(i)
    converted_array.append(j)

converted_array_1=[abs(i) for i in array]

print("The initial array is: ",array)
print("extracted positive array is: ", extracted_array)
print("Method 1 conerted array: ",converted_array)
print("Method 2 converted array is: ",converted_array_1)