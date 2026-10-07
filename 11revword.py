#reverse each word of string
sentence = input("Enter a sentence: ")
word = sentence.split()
result = []
for w in word:
    result.append(w[::-1])
answer = " ".join(result)

print("Original sentence:", sentence)
print("Reversed words:", answer)