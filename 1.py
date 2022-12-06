size = 4
str1 = ["hello", "2", "world", ":-)"]
str2 = []
index = 0
while index < size:
    length = len(str1[index])
    if length <= 3:
        str2.append(str1[index])
    index += 1
print(str2)