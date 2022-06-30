

with open("words.txt", "r") as f:
    words = f.readlines()
    print(words)

clean_words = []
for w in words:
    clean_words.append(w.strip().upper())

print(clean_words)
