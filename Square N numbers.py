# A list of Square of N numbers

n=int(input("Enter the Nth number OR the last number... "))

array=[i for i in range(1,n+1)]

square_array=[i**2 for i in array]

print("Set of inital list is: ",array)
print("Squared list is : ",square_array)