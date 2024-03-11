string = "Greeks"

def test(string):
    string = "GreeksforGreeks"
    print("Inside Function:", string)

test(id(string))
print("Outside Function:", string)