string = input()

char = "-_ "
new_string = ""
new_string += string[0].lower()


for i in range(1,len(string)):
    if string[i] == " " or string[i] == "-" or string[i] == "_":
        new_string += ""
        new_string += string[i+1].upper()
        flag = True
    else:
        if flag:
            flag = False
            continue
        new_string += string[i]
        
print(new_string)