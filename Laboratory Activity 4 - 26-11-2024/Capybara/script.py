from capybara import Capybara

def main():
    capybara = Capybara("Biscoff", "M", 5)

    test_case = input("Enter the test case number: ")

    if test_case == "1":
        print(f"Test case 1: Name: {capybara.name}, Gender: {capybara.gender}, Age: {capybara.age} years old")

if __name__ == "__main__":
    main()

