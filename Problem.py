# Find the most repeated character in this sentence


from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency)

sorted_char_frequency = sorted(char_frequency.items(), key=lambda kv: kv[1])
print(sorted_char_frequency[1])
