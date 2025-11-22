# Check if a Number is Even or Odd

num1= int(input(' enter the number :'))

if num1 % 2 == 0:
    print(num1," is a even number")
else:
    print(num1," is a odd number")


print('\n')

#Sum of Integers from 1 to 50 Using a Loop


total = 0

for num in range(1, 51):
    total += num

print("The sum of numbers from 1 to 50 is:", total)


