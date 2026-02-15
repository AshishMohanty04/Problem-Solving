word = str(input("enter an word :"))

result = ""

for ch in word:
    if ch not in result:
        result += ch

print(result)
