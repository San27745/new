#count sub string 
text = input("Enter a string: ")
sub = input("Enter substring to search: ")
cnt = 0
for i in range(len(text) - len(sub) + 1):
    if text[i:i + len(sub)] == sub:
        cnt = cnt + 1
print("Substring occurs", cnt, "times")