from user import *
from admin import *
import json
import sys

x=Admin()
z=User()

while True:
     print("*"*125)
     print("Enter 1 for Admin Login")
     print("Enter 2 for User Login")
     print("Enter 3 for Exit")
     print("*"*125)
     Login=input("Enter your choice :")
     if Login == "1":
          print("*"*125)
          x.Admin_Registration()
          print("*"*125)
          x.Admin_Login()
          print("Enter 1 for Adding Food Items :")
          print("Enter 2 for Editing Food Items :")
          print("Enter 3 for View Food Items :")
          print("Enter 4 for Removing Food Items :")
          option=input("Enter your choice :")
          if option=="1":
               print(x.Add_new_food_item())
               print(x.Add_new_food_item())
               print(x.Add_new_food_item())
               print("Food Item added Successfully")
               print("Do you wish to update again")
               opt1=input("Enter Yes or No  : ")
               if opt1=="Yes" or "yes":
                     print("Enter 1 for Adding Food Items :")
                     print("Enter 2 for Editing Food Items :")
                     print("Enter 3 for View Food Items :")
                     print("Enter 4 for Removing Food Items :")
               elif opt1=="No" or "no":
                     print("Invalid details")

          elif option=="2":
               print(x.Edit_fooditem())
               print("Food Item has been updated Successfully")
          elif option=="3":
               print(x.View_foodlist())
          elif option=="4":
               x.Remove_fooditem()
               print("Food Item has been successfully removed")

          else:
               print("Invalid choice")
               break
                                
               
     elif Login == "2":
               print(z.User_Registration())
               print("*"*125)
               print(z.User_Login())
               print("*"*125)

     elif Login=="3":
          print("*****************Thank You visit again********************")
          sys.exit()
