# Input
text = input("Enter a string: ")

# Initialization
vowels = "aeiouAEIOU"
vowel_count = consonant_count = space_count = symbol_count = digit_count = 0

# Character classification
for char in text:
    if char.isdigit():
        digit_count += 1
    elif char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    elif char == " ":
        space_count += 1
    else:
        symbol_count += 1

# Output with summary
print("\nCharacter Type Summary:")
print(f"Vowels         : {vowel_count}")
print(f"Consonants     : {consonant_count}")
print(f"Spaces         : {space_count}")
print(f"Special Symbols: {symbol_count}")
print(f"Digits         : {digit_count}")

# Final Summary
total_characters = len(text)
print(f"\nSummary: The input contains {total_characters} characters in total, "
      f"with {vowel_count} vowels, {consonant_count} consonants, "
      f"{space_count} spaces, {symbol_count} special symbols, and {digit_count} digits.")
