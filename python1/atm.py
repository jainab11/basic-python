notes = [500,100,50,20,10]
amount = int(input("enter a aount"))
for no in notes:
    count = amount//no
    print(f"note value: {no} the number of notes{count}")
    amount = amount%no