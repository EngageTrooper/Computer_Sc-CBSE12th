outputNeeded = 'My Name is Anthony Possobon'
#Using .center method
print("The Center aligned String is:")
print(outputNeeded.center(40,"#"))

#Using .ljust method
print("Left Aligned String is:")
print(outputNeeded.ljust(40,"-"))

#Using .rjust method
print("Right aligned String is:")
print(outputNeeded.rjust(40,"-"))

#Using Format Method
print("{} and {}".format("Shivam","Mickeyfying"))

tab = input("Shivam is CEO of Which Studio::")

print("No. 1 Game Development Studio is:: {}".format(tab))
