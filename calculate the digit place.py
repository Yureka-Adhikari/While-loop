num = int(input("Enter a number: "))
digit_count = 0

while num != 0:
    num= num//10
    digit_count= digit_count+1
    
print(f"The given number {num} has {digit_count} digits")
