from collections import Counter
ans = input("Input: ")
vowel = "aeiouAEIOU"
v_count = sum(Counter(ans)[v] for v in vowel)
count = Counter(ans)

c_count = sum(count[ch] for ch in count if ch.isalpha() and ch not in vowel)
print(f"number of consonants: {c_count}")
print(f"number of vowels: {v_count}")