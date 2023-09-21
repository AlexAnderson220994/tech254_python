# What is a dictionary?

# Uses key/value pairs
# key = the reference to the object
# value = the data storage mechanism you want to use (variable, list, dictionary etc.)

# Making a dictionary

student_1 = {
    "name": "Alex",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data types", "operators"]
}

print(student_1)

# Accessing data using the key(s)

print(student_1["stream"]) # dictionaries are unordered so you can't specify an item
print(student_1["completed_lesson_names"][0])

# changing a value in a dict(ionary)

# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])
#
# student_1["completed_lesson_names"].remove("data_types")
# print(student_1["completed_lesson_names"])

# Getting the keys

print(student_1.keys())

# Sets from Frozen sets

# no order - randomises each time
# Only contains one of each type of item

car_parts = {"wheels", "doors", "exhaust", "windows"}
print(car_parts)

car_parts.add("steering_wheel")
print(car_parts)

car_parts.discard("windows")
print(car_parts)

# Frozen sets (immutable)

x = frozenset([1, 2, 3, 4, 5])

