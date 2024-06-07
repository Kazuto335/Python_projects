name=input("enter your name \n")
print("good afternoon", name)

letter='''Dear <|NAME|>,
You are selected!

Date: <|DATE|>'''

name = input("Enter your name:\n")
date = input("Enter Date:\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print("\n",letter)

a = "This is the sting with  Double  Spaces"
doubleSpaces = a.find("i")
print(doubleSpaces)
a = a.replace(" ","   ")
print(a)


letter = "Dear Harry, This Python course is nice! Thanks!"
print(letter)

formatted_letter = "Dear Harry,\n\tThis Python course is nice!\n\tThanks!"
print(formatted_letter)
