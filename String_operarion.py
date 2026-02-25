def string_statistics(text):
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for ch in text if ch in vowels)
    num_consonants = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
    num_spaces = text.count(" ")
    num_lowercase = sum(1 for ch in text if ch.islower())
    print("String Statistics:")
    print(f"Number of Vowels: {num_vowels}")
    print(f"Number of Consonants: {num_consonants}")
    print(f"Number of Spaces: {num_spaces}")
    print(f"Number of Lowercase Letters: {num_lowercase}")

user_input = input("Enter a string: ")
string_statistics(user_input)