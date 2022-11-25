import csv
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog

dineout=0
shopping=0
travel=0
medicines=0
utilities=0
entertainment=0
education=0
totalExpense=0
expenses_dict={}

def expense_tracker():
    
    global dineout, shopping,utilities,entertainment, education, totalExpense, travel,medicines
    global expenses_dict
    # opening the CSV file
    with open('2022 Expense tracker - January (1).csv', mode ='r')as file:
   
  # reading the CSV file
      csvFile = csv.reader(file)
 
  # traversing each expense and add amount to category
      
      for expense in csvFile:
            category= expense[2]
            if (category=='Dine out'):
                dineout+=int(expense[1])
                expenses_dict['Dine out']=dineout
            elif (category=='Shopping'):
                shopping+=int(expense[1])
                expenses_dict['Shopping']=shopping
            elif (category=='Utilities'):
                utilities+=int(expense[1])
                expenses_dict['Utilities']=utilities
            elif (category=='Travel'):
                travel+=int(expense[1])
                expenses_dict['Travel']=travel
            elif (category=='Education'):
                education+=int(expense[1])
                expenses_dict['Education']=education
            elif (category=='Entertainment'):
                entertainment+=int(expense[1])
                expenses_dict['Entertainment']=entertainment
            elif (category=='Medicines'):
                medicines+=int(expense[1])
                expenses_dict['Medicines']=medicines


    totalExpense=dineout+shopping+entertainment+education+utilities+medicines+travel
    
    
    #plot pie chart
    plot_pie_chart(expenses_dict , totalExpense)
    
def plot_pie_chart(expenses_dict ,totalExpense):
    
    explode = [0.2, 0.1, 0.4, 0.7, 0.4, 0.5, 0.2]
    plt.pie(expenses_dict.values(), labels=expenses_dict.keys(), explode= explode, radius=1.5 ,shadow = True,wedgeprops = {"edgecolor" : "black",
                      'linewidth': 2,
                      'antialiased': True} ,autopct='%.2f%%',textprops = dict(color ="purple", size=19) )
   
    #plt.legend(title='Expense Categories',loc='lower right')
    plt.legend(title='Expense Categories',bbox_to_anchor=(1.34, 1), loc="upper left")
    plt.suptitle('Category wise Expense tracking', size=16, y=1.12);      


    
if __name__=='__main__':
    expense_tracker()
