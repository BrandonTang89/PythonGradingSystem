stack = []

reference = {")" : "(", "]": "[", "}": "{"}
sequence = input()
valid= True
for i in sequence:
    #print(i)
    if i == "]" or i == ")" or i== "}":
        if len(stack) == 0 or stack[-1] != reference[i]:
            valid = False
            break
        else:
            #print("poping")
            stack.pop()
    else:
        stack.append(i)

            
if len(stack)  > 0:
    valid = False
if valid:
    print("Valid")
else:
    print("Invalid")
