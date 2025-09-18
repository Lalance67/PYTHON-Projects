word1 = "hello, world\n"   #  normal string that uses escape seq \n
word2 = r"world, world\n"  #  doesn't  read escape sequence (you can just add /, "", etc.)

print(word1)
print(word2)