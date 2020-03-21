money500 = 500
amount500 = 5
amount500_give = 0

money1_000 = 1_000
amount1_000 = 5
amount1_000_give = 0

money2_000 = 2_000
amount2_000 = 5
amount2_000_give = 0

money5_000 = 5_000
amount5_000 = 5
amount5_000_give = 0

money10_000 = 10_000
amount10_000 = 5
amount10_000_give = 0

money20_000 = 20_000
amount20_000 = 5
amount20_000_give = 0

candy = False

give =	185_250
price =	13_000
change = 0

# Post change
if (give > price):
	change = give - price
	print(f"Original change: {change}")
elif (give == price):
	print("Thank you! See you soon.")
else:
	print("Not enough money.")

# Calculate change with existing amount
while(change !=0):
	if (change >= 20_000 and amount20_000 > 0):
		change -= 20_000
		amount20_000 -= 1
		amount20_000_give += 1
		continue

	elif (change >= 10_000 and amount10_000 > 0):
		change -= 10_000
		amount10_000 -= 1
		amount10_000_give += 1
		continue
		
	elif (change >= 5_000 and amount5_000 > 0):
		change -= 5_000
		amount5_000 -= 1
		amount5_000_give += 1
		continue

	elif (change >= 2_000 and amount2_000 > 0):
		change -= 2_000
		amount2_000 -= 1
		amount2_000_give += 1
		continue

	elif (change >= 1_000 and amount1_000 > 0):
		change -= 1_000
		amount1_000 -= 1
		amount1_000_give += 1
		continue

	elif (change >= 500 and amount500 > 0):
		change -= 500
		amount500 -= 1
		amount500_give += 1
		continue

	else:
		candy = True
		break

# Give change to customer
print("Change:")
if amount20_000_give != 0:
	print(f"20.000vnd x{amount20_000_give}")

if amount10_000_give != 0:
	print(f"10.000vnd x{amount10_000_give}")

if amount5_000_give != 0:
	print(f" 5.000vnd x{amount5_000_give}")

if amount2_000_give != 0:
	print(f" 2.000vnd x{amount2_000_give}")

if amount1_000_give != 0:
	print(f" 1.000vnd x{amount1_000_give}")

if amount500_give != 0:
	print(f"   500vnd x{amount500_give}")

if candy:
	print(f"Candy instead? ({change}vnd left)")