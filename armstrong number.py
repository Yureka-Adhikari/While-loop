num=int(input("Enter a number you would like to check: "))

temp= num
sum=0

while temp > 0:
    digit= temp%10
    sum= sum + (digit**3)
    temp= temp // 10
    
if num == sum:
    print(f"The given number: {num} is an armstrong number.")
else:
    print(f"The given number: {num} is NOTTT an armstrong number.")