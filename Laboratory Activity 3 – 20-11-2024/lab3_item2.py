def is_perfect_number(number):
    if number <= 0:
        return False

    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            if is_perfect_number(num):
                print(f"{num} is a perfect number!")
            else:
                print(f"{num} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")
