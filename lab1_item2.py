input_chars = input("Enter two space-seperated characters: ").split()
char1, char2 = input_chars
greater_char = max(char1, char2)
print("---------------")
print(f"The character withgreater value is: {greater_char}")
print("---------------")
print("This part is optional to include.")
print("Showing ASCII Values:")
print(f"{char1} : {ord(char1)}")
print(f"{char2} : {ord(char2)}")