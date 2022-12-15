# Read in text file
with open("input.txt") as file:
  inventory = file.readlines()

# Initialise a list to store the elves calorie totals and a int to add up the calories
elfCalories = []
currentCount = 0

# Iterate over lines from text file
for item in inventory:
  # Check if line isn't blank then and add number to running total
  if not item.isspace():
    currentCount += int(item)
  # If line is blank, store the total in a new list item and initialise the running count
  else:
    elfCalories.append(currentCount)
    currentCount = 0

# Initialise a variable to store a running count of the top 3 elves
topTotal = 0

# Iterate 3 times to get the top 3 elves
for i in range(3):
  # Find the index of the biggest value in the elfcalories list
  biggestValue = max(elfCalories)
  # Pop it off the list so when we iterate again we get the next biggest value
  elfCalories.remove(biggestValue)
  # Total up the values
  topTotal += biggestValue

  print(f"{i + 1}: {biggestValue} calories")

print(f"Total calories: {topTotal}")