
content = []
for line in open('abc'):
    content.append(line)

print("File: ")
for line in reversed(content):
    print(line)