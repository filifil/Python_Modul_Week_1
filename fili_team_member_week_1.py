#input from the user
num = int(input("Enter a number: "))

for i in range(2, num + 1, 2):  
# Print every even number    
    print(i)

num = int(input("Enter a number: "))

print("Even numbers whith while loop:")
i = 2  # Start from 2
while i <= num:
    print(i)
    i += 2  # Increasing  by 2     
