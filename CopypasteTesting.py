"""
Copy and paste depot
Dante Daciuk
13/3/24
"""
print(" __________")
print("|          |")
print("|          |")
print("|          |")
print("|          |")
print("|          |")
print("|__________|")
print("")
print("♠ spade")
print("♥ heart")
print("⯁ diamond")
print("♣️ club")

card_dictionary = {"1 of ⯁": 1, "1 of ♠": 1, "1 of ♥": 1, "1 of ♣️": 1, 
"2 of ⯁": 2, "2 of ♠": 2, "2 of ♥": 2, "2 of ♣️": 2,
"3 of ⯁": 3, "3 of ♠": 3, "3 of ♥": 3, "3 of ♣️": 3,
"4 of ⯁": 4, "4 of ♠": 4, "4 of ♥": 4, "4 of ♣️": 4,
"5 of ⯁": 5, "5 of ♠": 5, "5 of ♥": 5, "5 of ♣️": 5,
"6 of ⯁": 6, "6 of ♠": 6, "6 of ♥": 6, "6 of ♣️": 6,
"7 of ⯁": 7, "7 of ♠": 7, "7 of ♥": 7, "7 of ♣️": 7,
"8 of ⯁": 8, "8 of ♠": 8, "8 of ♥": 8, "8 of ♣️": 8,
"9 of ⯁": 9, "9 of ♠": 9, "9 of ♥": 9, "9 of ♣️": 9,
"10 of ⯁": 10, "10 of ♠": 10, "10 of ♥": 10, "10 of ♣️": 10,
"J of ⯁": 11, "J of ♠": 11, "J of ♥": 11, "J of ♣️": 11,
"Q of ⯁": 12, "Q of ♠": 12, "Q of ♥": 12, "Q of ♣️": 12,
"K of ⯁": 13, "K of ♠": 13, "K of ♥": 13, "K of ♣️": 13,
"A of ⯁": 14, "A of ♠": 14, "A of ♥": 14, "A of ♣️": 14,}


test_tuple = ["1A", "1B", "2", "3"]
test_tuple_two = ["1A", "1B", "2", "3"]

print(type(test_tuple))
tuple_value = 0
tuple_value_two = 0
print("The testTuple is ", test_tuple, test_tuple_two)
randomCard = random.choice(test_tuple)
randomCardTwo = random.choice(test_tuple_two)
if "1" in randomCard:
    print("1 is present")
    tuple_value = 1
elif "2" in randomCard:
    print("2 is present")
    tuple_value = 2
elif "3" in randomCard:
    print("3 is present")
    tuple_value = 3

if "1" in randomCardTwo:
    print("1 is present")
    tuple_value_two = 1
elif "2" in randomCardTwo:
    print("2 is present")
    tuple_value_two = 2
elif "3" in randomCardTwo:
    print("3 is present")
    tuple_value_two = 3

if tuple_value > tuple_value_two:
    print("Player won")
elif tuple_value < tuple_value_two:
    print("Player lost!")
else:
    print("WAR!!!")

print(tuple_value)
print(tuple_value_two)