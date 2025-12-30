import os
file_path = './File_Handling/demo.txt'

# Count the total number of vowel and consonants if a file and percentage

with open(file_path, 'r') as f:
    text = f.read()
    count_char = len(text)
    count_vowel = 0
    count_consonant = 0
    for char in text:
        if char.lower() in 'aeiou':
            count_vowel += 1
        else:
            count_consonant += 1

print("Total Char = ", count_char)
print("Total vowel = ", count_vowel)
print("Total consonant = ", count_consonant)
print(f"Vowel percentage {(count_vowel * 100) / count_char:.2f}")
print(f"Consonant percentage {(count_consonant * 100) / count_char:.2f}")
