# The list of pies to print to the screen
pieList = ["Pecan", "Kit Kat", "Apple Crisp", "Bean", "Banoffee",
             "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

pieCountList = [0,0,0,0,0,0,0,0,0,0,0]
# The amount of candy the user will be allowed to choose
order = "y"
# The list used to store all of the candies selected inside of
pieCart = []

for pie in pieList:
    print("[" + str(1+pieList.index(pie)) + "]" + pie)
while (order == "y" ):
    userchoice = int(input("choose your pie by number."))-1
    
    pieCart.append(pieList[userchoice]) 

    pieCountList[userchoice] += 1
    print("Great, you ordered "+pieList[userchoice])   
    order = input("continue order, (y)es or (n)o?")


for pie in pieCart:
    print("[" + str(1+pieCart.index(pie)) + "]" + pie )

pieIndex = len(pieCart)
print(str(pieIndex)+" pie ordered")

for i in range(1,12):
    print( str(pieList[i-1]) +" "+str(pieCountList[i-1]) )
