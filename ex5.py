# name = 'Zed A. Shaw'
# age = 35 # not a lie
# height = 74 # inches
# weight = 180 # lbs
# eyes = 'Blue'
# teeth = 'White'
# hair = 'Brown'
#
# print(f"Let's talk about {name}.")
# print(f"He's {height} inches tall.")
# print(f"He's {weight} pounds heavy.")
# print(f"Actually that's not too heavy.")
# print(f"He's got {eyes} eyes and {hair} hair.")
# print(f"He's teeth are usually {teeth} depending on the coffee.")
#
# #this line is tricky, try to get it exactly right
# total = age + height + weight # 35 + 74 + 180 = 289
# print(f"If i add {age}, {height}, and {weight} I get {total}")


height_in_inches = int(input('Enter height in inches: '))
weight_in_pound = int(input('Enter weight in pounds: '))

convert_inches_to_cm = height_in_inches * 2.54
convert_pounds_to_kg = weight_in_pound * 0.45

print(convert_inches_to_cm)
print(convert_pounds_to_kg)