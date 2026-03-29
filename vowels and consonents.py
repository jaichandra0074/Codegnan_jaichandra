text = input("Enter the string : ")
vowels = "aeiouAEIOU"

vowel_count = sum(text.count(v) for v in vowels)
space_count = text.count(" ")
total_chars = len(text)

consonant_count = total_chars - vowel_count - space_count

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Spaces:", space_count)
