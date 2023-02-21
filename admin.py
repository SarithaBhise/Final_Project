import sys
import json
class Admin:
    def __init__(self):
        self.food_item={}
        self.food_id=len(self.food_item)+1
    
    def Admin_Registration(self):
        while True:
            self.Admin_name=input("Enter Your Full Name: ")
            self.Admin_mobile=input("Enter a valid mobile number: ")
            if len(self.Admin_mobile)!=10:
                print("Please correct the mobile number you have entered")
                self.name=input("Enter Your Full Name: ")
                self.Admin_mobile=input("Enter a valid mobile number: ")
            else:
                self.Admin_email=input("Enter a valid Email Id :")
                self.Admin_address=input("Enter Address :")
                self.Admin_password=input("Enter a valid Password :")
                if len(self.Admin_password)!=8:
                    print("Password must be 8 digit number")
                    break
                else:
                    self.Admin_Details={"Name":self.Admin_name,"Mobile":self.Admin_mobile,"Email_Id":self.Admin_email,"Address":self.Admin_address,"Password":self.Admin_password}
                    with open("LoginDetails_of_Admin.json","w") as f:
                        json.dump(self.Admin_Details,f)
                        return self.Admin_Details
    def Admin_Login(self):
        print("-----------------Welcome---------------------------")
        print("Please enter your Admin login details here ")
        self.login_Admin_mobile=input("Enter a valid mobile number: ")
        self.login_Admin_password=input("Enter a valid Password :")
        if self.login_Admin_mobile==self.Admin_mobile and self.login_Admin_password==self.Admin_password:
            print("Your have succefully logged in as a Admin")
        else: 
            print("Invalid Admin Login")
            sys.exit()


    def Add_new_food_item(self):
        print("------------Enter the Details here-------------")
        self.food_name=input("Enter Food Name :")
        self.quantity=(input("Enter Food Qunatity :"))
        self.price= int(input("Enter Food Price: "))
        self.stock=(input("Enter Food Stock: "))
        self.discount=(input("Enter Discount: "))
        self.Item={"Food_name":self.food_name,"Quantity":self.quantity,"Price":self.price,"Stock":self.stock,"Discount":self.discount}
        self.food_id=len(self.food_item)+1
        self.food_item[self.food_id]=self.Item
        with open("Food_item.json","w") as f:
            json.dump(self.food_item,f)
            print("-"*50)
            print("Your Food item has been added successfully")
        return self.food_item
   
    def Edit_fooditem(self):
        Item_id = input("Please enter the Id which is to be updated :")
        with open("Food_item.json","r") as f:
            Update_FoodId = json.load(f)
            
        if Item_id not in Update_FoodId:
            print("Please enter a valid Id")
            
        else:
            print(Update_FoodId[Item_id])
            
            while True:
                    print("Enter 1 for updating Food name")
                    print("Enter 2 for updating Food Quantity")
                    print("Enter 3 for updating Food Price")
                    print("Enter 4 for upodating Food Stock")
                    print("Enter 5 for updating Food Discount")
                    Edit_Food=int(input("Enter the Food Id you want to edit : "))
    
                    if Edit_Food == 1:
                        New_Foodname=input("Enter a new Food Name:")
                        Update_FoodId[Item_id]["Food_name"]= New_Foodname
                        with open("Food_item.json","w") as f:
                            json.dump(New_Foodname,f)
                            print("The updated Food Name is:",New_Foodname)    
                            return Update_FoodId[Item_id]
                        
                    if Edit_Food == 2:
                        New_FoodQuantity=input("enter new Food Quantity: ")
                        Update_FoodId[Item_id]["Quantity"]= New_FoodQuantity
                        with open("Food_item.json","w") as f:
                            json.dump(New_FoodQuantity,f)
                            print("The updated Food Quantity is:",New_FoodQuantity)
                            return Update_FoodId[Item_id]
                        
                    if Edit_Food == 3:
                        New_FoodPrice=input("enter new Food Price: ")
                        Update_FoodId[Item_id]["Price"]= New_FoodPrice
                        with open("Food_item.json","w") as f:
                            json.dump(New_FoodPrice,f)
                            print("The updated Food Price is:",New_FoodPrice)
                            return Update_FoodId[Item_id]
                        
                    if Edit_Food == 4:
                        New_FoodStock=input("enter new Food Stock: ")
                        Update_FoodId[Item_id]["Stock"]= New_FoodStock
                        with open("Food_item.json","w") as f:
                            json.dump(New_FoodStock,f)
                            print("The updated Food Stock is:",New_FoodStock)
                            return Update_FoodId[Item_id]   
                        
                         
                    if Edit_Food == 5:
                        New_FoodDiscount=input("enter new Food Discount: ")
                        Update_FoodId[Item_id]["Discount"]= New_FoodDiscount
                        with open("Food_item.json","w") as f:
                            json.dump(New_FoodDiscount,f)
                            print("The updated food name is:",New_FoodDiscount)
                            return Update_FoodId[Item_id]  
                  
                    
             
          

    def View_foodlist(self):
        print("------------The Food items you wish to view are------------- ")
        return self.food_item


    def Remove_fooditem(self):
        food_item=int(input("Enter the food id you want to remove : "))
        del self.food_item[food_item]
        print("Remaining Food items are:",self.food_item)
        with open("Food_item.json","w") as f:
            json.dump(self.food_item,f)
            return self.food_item
