
sequence = input()
valid= True
counter = 0
for i in sequence:
    if i == '(':
        counter+=1
    else:
        counter-=1
        if counter < 0:
            valid = False
            break
if counter > 0:
    valid = False
if valid:
    print("Valid")
else:
    print("Invalid")
