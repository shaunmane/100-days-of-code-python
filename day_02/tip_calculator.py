print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")
tip_input = input("How much tip would you like to give? ")
split = input("How many people to split the bill? ")

# convert tip_input 
tip = int(tip_input)/100 + 1

pay = float(bill)/int(split) * float(tip)  

print(f"Each person should pay: ${pay:.2f}")