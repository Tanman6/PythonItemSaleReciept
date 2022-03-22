'''
The class created collects the data for a sales receipt, and provides
methods for:
    - Adding receipt items
    - Calculating the item total (Extended Price)
    - Calculating the Sales tax
    - Calculating the sales total
    - returning the contents of the receipt
'''

#Class Definition

class SalesReceipt:

#Internal Class variables
    itemList = [] #List object that contains receipt line items
    saleTotal = 0.00 #Total sales amount before taxes
    salesTax = 0.00 #Sales tax amount
    itemTotal = 0.00 #Extended price for an item
    
#Class attributes that are externally addressable
#Must set attribute values in main program
    def _init_(itemName, itemQty, itemPrice):
        sale.itemName = "" #Name of item to be sold
        sale.itemQty = 0 #Quantity of item to be sold
        sale.itemPrice = 0.00 #Price of item to be sold
        return

#Class method for calculating the extended price (requires no parameters)
#Returns the extended price for an item
#Uses the class attribute values which must be set by the main program
    def ExtPrice(sale):
        sale.itemTotal = sale.itemQty * sale.itemPrice
        return sale.itemTotal

#Adds an item to the list containing the sales receipt line items
#Returns the extended price
#Increments the sales receipt total with line item extended price
    def AddItem(sale):
        sale.itemTotal = sale.ExtPrice()
        sale.saleTotal += sale.itemTotal
        sale.itemList.append(sale.itemName + "," + str(sale.itemQty) + "," + format(sale.itemPrice, ".2f") + "," + format(sale.itemTotal, ".2f"))
        return sale.itemTotal

#Return a list containing the line items in the sales receipt
#The items are separated by commas
    def SalesDetail(sale):
        return sale.itemList

#Returns the total of the sles line items
    def SaleTotal(sale):
        return sale.saleTotal

#Returns the sales tax amount
    def SalesTax(sale):
        sale.salesTax = sale.saleTotal * 0.08
        return sale.salesTax

#Returns the final sale total including taxes
    def FinalSaleAmt(sale):
        total = sale.saleTotal + sale.salesTax
        return total

              

    

