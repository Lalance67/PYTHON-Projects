import collections
def vowels(ans):
    vow = "aeiou"
    return sum(collections.Counter(ans)[i] for i in vow)
ans = input("Input: ").lower()
print(f"Output: {vowels(ans)}")