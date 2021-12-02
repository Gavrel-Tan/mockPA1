class Cart:
    items = []
    prices = []
    totalItems = 0
    totalPrice = 0

    def calcTotalPrice(self):
        self.totalItems = len(self.items)
        for item in self.prices:
            self.totalPrice += float(item)


myCart = Cart()
with open("myCart.txt") as file:
    fileStr = file.read()
fileList = fileStr.split("\n")
for item in fileList:
    itemList = item.split("\t")
    myCart.items.append(itemList[0])
    myCart.prices.append(itemList[1])

myCart.calcTotalPrice()
print("The total price for ", myCart.totalItems, " items is $", myCart.totalPrice)
