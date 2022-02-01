matrix = [
    [7,"i",3],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ","#"],
    ["s","M"," "],
    ["$","a"," "],
    ["#","t","%"],
    ["^","r","!"]
]
length1 = len(matrix)
tab = matrix[0]
length = len(tab)
message = " "
for i in range(0,length):
    for j in range(0,length1):
        code = matrix[j][i]
        code = str(code)
        code = code.lower()
        if(ord(code) >= 97 and ord(code) <= 122):
            message+= code
        else:
            message+=" "
print(message)

