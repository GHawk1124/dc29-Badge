with open("text", 'r') as f:
    content = f.read()[0:-1].split(" ")
string = ""
for number in content:
    string += chr(int(number))
print(string)
