from tkinter import *
from tkinter import filedialog
import os
import Module

sale = Module.SalesReceipt()


#file save text box
def OpenFile():
    SalesReceipt.filename = filedialog.asksaveasfilename(parent = SalesReceipt,
                                                  initialdir = os.getcwd(),
                                                  title = "Name the file you wish to create",
                                                  filetypes = (("Text File", "*.txt"),("All Files", "*.*")))
    fileContents = str(SalesReceipt.filename) + ".txt"
    global TransactionFile
    TransactionFile = open(fileContents, "w")

def SaveFile():
    itemName = txtItemName.get()
    itemPrice = txtItemPrice.get()
    itemQuantity = txtItemQuantity.get()
    extended = txtExtended.get()
    tax = txtTax.get()
    total = txtTotal.get()
    payFile.write(itemName + ", " + itemPrice + ", " + itemQuantity + ", "
                  + extended + ", " + tax +  ", " + total + '\n')

    
#function to total the items and write them to the file
def Total():
    txtSaleTotal.delete(0,END)
    txtSaleTotal.insert(END, format(sale.SaleTotal()))
    txtTax.insert(END, format(sale.SalesTax()))
    txtTotal.delete(0, END)
    txtTotal.insert(END, format(sale.FinalSaleAmt()))
    for line in sale.SalesDetail():
        TransactionFile.write(line + '\n')
        return
    
#function to clear the data from the GUI
def ClearItem():
    txtItemName.delete(0, END)
    txtItemPrice.delete(0, END)
    txtItemQuantity.delete(0, END)
    txtExtended.delete(0, END)
    txtSaleTotal.delete(0,END)
    txtTax.delete(0, END)
    txtTotal.delete(0, END)
    txtItemName.focus()
    return

#button for exiting the program saving info to file with the close function
def ExitProgram():
    TransactionFile.close()
    SalesReciept.destroy()
    return
#Title for the GUI
SalesReceipt = Tk()
SalesReceipt.title('Transaction Receipt')
SalesReceipt.geometry('800x600')

#create textboxes
txtItemName = Entry(SalesReceipt)
txtItemName.grid(row = 0, column = 1)
txtItemPrice = Entry(SalesReceipt)
txtItemPrice.grid(row = 1, column = 1)
txtItemQuantity =Entry(SalesReceipt)
txtItemQuantity.grid(row = 2, column = 1)
txtExtended = Entry(SalesReceipt)
txtExtended.grid(row = 3, column = 1)
txtSaleTotal = Entry(SalesReceipt)
txtSaleTotal.grid(row = 4, column = 1)
txtTax = Entry(SalesReceipt)
txtTax.grid(row = 5, column = 1)
txtTotal = Entry(SalesReceipt)
txtTotal.grid(row = 6, column = 1)

#create labels
lblItemName = Label(SalesReceipt, text = 'Item Description:')
lblItemName.grid(row = 0, column = 0)
lblItemPrice = Label(SalesReceipt, text = 'Item Price:')
lblItemPrice.grid(row = 1, column = 0)
lblItemQuantity = Label(SalesReceipt, text = "Item Quantity")
lblItemQuantity.grid(row = 2, column = 0)
lblExtended = Label(SalesReceipt, text = 'Extended Price:')
lblExtended.grid(row = 3, column = 0)
lblSaleTotal = Label(SalesReceipt, text = 'Sale Total')
lblSaleTotal.grid(row = 4, column = 0)
lblTax = Label(SalesReceipt, text = 'Sales Tax:')
lblTax.grid(row = 5, column = 0)
lblTotal = Label(SalesReceipt, text = 'Total:')
lblTotal.grid(row = 6, column = 0)

#create buttons
#Button to call Create File function
buttonOpenFile = Button(SalesReceipt, text = 'Create a File', command = OpenFile)
buttonOpenFile.grid(row = 1, column = 2)
#button to call save item function
buttonSaveItem = Button(SalesReceipt, text = 'Save to File', command = SaveFile)
buttonSaveItem.grid(row = 1, column = 3)
#button to calculate pay
buttonCalc = Button(SalesReceipt, text = "Calculate Extended Price")
buttonCalc.grid(row = 3, column = 2)
#button to call total function
buttonGetTotal = Button(SalesReceipt, text = 'Total', command = Total)
buttonGetTotal.grid(row = 6, column = 2)
#button to exit the program
buttonExitProgram = Button(SalesReceipt, text = 'Exit Program', command = ExitProgram)
buttonExitProgram.grid(row = 8, column = 1)
#button to clear info
buttonClearItem = Button(SalesReceipt, text = 'Clear Items', command = ClearItem)
buttonClearItem.grid(row = 7, column = 1)

#main loop of program
txtItemName.focus()
SalesReceipt.mainloop()
