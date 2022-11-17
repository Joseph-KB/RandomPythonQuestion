# Display the future leap year from current year to a final year entered by user
'''
For a year to be leap year the following situations should be satisfied
1) Year should have zero reminder when divided by 4. And the number should not be divisible by 100
2) If year is divisible by 400 it will be a leap year.
'''


current_year= int(input("Enter the current year....")) 
final_year=int(input("Enter the final year...."))

buffer=0

for i in range(current_year,(final_year+1)):
    if (i%4==0 and i%100!=0) or (i%400==0):
        buffer+=1

print(f"The count of leap year between {current_year} and {final_year} is: ", buffer)
