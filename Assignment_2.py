
#Task_1
number = float(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")

else:
    print(f"{number} is an odd number")

#Task_2
n = int(input("Enter a number:  "))
total_sum = 0
for i in range(1,n+1):
    total_sum += i
print(f"The total sum of numbers from 1 to {i} is {total_sum}")