# Loop through a range of numbers (0 through 4)
for x in range(5):
    print(x)

print("-----------------------------------------")

# Loop through a range of numbers (2 through 6)
for x in range(2, 7):
    print(x)

print("----------------------------------------")

# Iterate through letters in a string
word = "Peace"
for letters in word:
    print(letters)

print("----------------------------------------")

# Iterate through a list
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal)

print("----------------------------------------")

# Loop while a condition is being met
run = int(input("how many numbers?"))
cont = "y"
i= 0

while cont == "y":
    
    while i<= run:
        print(f"{i}", end = " ")
        i = i+1
    cont = input("To run again. Enter 'y'")
    if cont == "y":
        i=run
        run = run + int(input("how many numbers this time?"))
        

#   run = input("To run again. Enter 'y'")



