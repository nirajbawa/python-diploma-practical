import os
char_frequency = {}

file_path = os.path.join(os.getcwd(), "IO", "text.txt")
with open(file_path, "r") as file:
    for line in file:
        print(line)
        for char in line:
            char_frequency[char] = char_frequency.get(char, 0)+1
            
print(char_frequency)