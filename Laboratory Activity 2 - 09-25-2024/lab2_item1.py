def is_palindrome(number):
    str_num = str(number)
    
    if str_num == str_num[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

num = int(input("Enter an integer: "))

print(is_palindrome(num))
