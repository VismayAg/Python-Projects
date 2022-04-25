x = int(input())

dict = {}

for i in range(x):
    text = input().split()
    dict[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in dict:
            print(inpt+"="+dict[inpt])
        else:
            print("Not found")
    except EOFError:
        break