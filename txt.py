import os

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())

# Example usage:
file_path = "example.txt"
result = count_lines(file_path)
print(f"There are {result} lines in the file.")
