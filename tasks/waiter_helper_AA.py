# List of starters
starters = ["Calamari", "Bread and olives", "Soup"]
# List of mains
mains = ["Fish of the day", "Chef's special pasta", "House burger"]
# List of desserts
desserts = ["Sticky toffee pudding", "Ice cream", "Crumble and custard"]
# List of drinks
drinks = ["Beer", "Wine", "Soft drink"]

# Customer greeting
greeting = "Hello customer. Welcome to the restaurant."
print(greeting)

# Ask the customer for starter choice
print("Here is our menu:")
print("Starters:", starters)
customer_starter = input("What would you like to begin with?: ")

# Ask the customer for main choice
print("Mains:", mains)
customer_main = input("And for your main course?: ")

# Ask the customer for dessert choice
print("Desserts:", desserts)
customer_dessert = input("What would you like for dessert?: ")

# Ask the customer for drink choice
print("Drinks:", drinks)
customer_drink = input("What drink would you like with your meal?: ")

# Customer choices
print("Starter: ", customer_starter)
print("Main Course: ", customer_main)
print("Dessert: ", customer_dessert)
print("Drink: ", customer_drink)

