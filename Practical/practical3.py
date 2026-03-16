# Write a Python program to count the occurrences of each word in a given sentence
# counting sentence
sentence = input("enter the sentence: ")
words = sentence.split()
words_count = {}
for words in words:
    if words in words_count:
        words_count[words] += 1
    else:
        words_count[words] = 1
print("occurrences of each word:", words_count)


# counting characters in a sentence
char = input("enter the word: ")
char_count = {}
for char in char:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
    print("count word: " ,char_count)
