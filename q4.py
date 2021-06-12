print("Enter a number")

originalnum = int(input())


rev = 0
temporary = originalnum

while(originalnum != 0):
    remainder = originalnum % 10
    rev = rev*10 + remainder
    originalnum = originalnum // 10

if(temporary == rev):
    print("Yes it is a pallindrome number")
else:
    print("No it is not a pallindrome number")
