import collections
text = input("Input: ").lower().split()
word_count = collections.Counter(text)
total = sum(collections.Counter(text)[i] for i in text)
print(f"total words: {total}")