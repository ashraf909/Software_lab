def count_and_sum_vowels(user_input):
    txt = user_input.strip().lower()
    
    target_vowels = ['a', 'e', 'i', 'o', 'u']
    total_vowels = 0
    total_ascii = 0
    
    for item in txt:
        if item in target_vowels:
            total_vowels += 1
            total_ascii += ord(item)
            
    return (total_vowels, total_ascii)