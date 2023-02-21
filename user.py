from admin import *
import sys
import json
class User:
    def __init__(self):
        self.User_Details={}
        self.Ordered_list=[]
  
    def User_Registration(self):
        while True:
            self.User_name=input("Enter Your Full Name: ")
            self.User_mobile=input("Enter a valid mobile number: ")
            if len(self.User_mobile)!=10:
                print("Please correct the mobile number you have entered")
                #self.User_name=input("Enter Your Full Name: ")
                #self.User_mobile=input("Enter a valid mobile number: ")
                break
            else:
                self.User_email=input("Enter a valid Email Id :")
                self.User_address=input("Enter Address :")
                self.User_password=input("Enter a valid Password :")
                if len(self.User_password)!=8:
                    print("Password must be 8 digit number")
                    break
                else:
                    self.User_Details={"Name":self.User_name,"Mobile":self.User_mobile,"Email_Id":self.User_email,"Address":self.User_address,"Password":self.User_password}
                    with open("User_LoginDetails.json","w") as f:
                        json.dump(self.User_Details,f)
                        return self.User_Details

    def User_Login(self):
        self.User_login_mobile=input("Enter a valid mobile number: ")
        self.User_login_password=input("Enter a valid Password :")
        if self.User_login_mobile==self.User_mobile and self.User_login_password==self.User_password:
            print("Your have succefully logged in as User")
        else: 
            print("Invalid Login")
            sys.exit()

        while True:
            print("*"*125)
            print("Enter A for placing an Order")
            print("Enter B for Order History")
            print("Enter C for Profile Update")
            print("Enter D for Exit")
            print("*"*125)
            option=input("Enter your choice : ")

            if option == "A" or option =="a":
                print("The Menu is :")
                print("1.Tandoori Chicken---4pieces----Rs.240")
                print("2.Vegan Burger---1 piece----Rs.320")
                print("3.Truffle Cake---500gms----Rs.900")
                print("*"*125)
                OD=input("Enter your item you want to place order : ")
                if OD=="1":
                    self.Ordered_list.append("Tandoori Chicken")
                    print("Item 1 is ordered",self.Ordered_list)
                    opt2=input("Do you wish to place order again,Yes or No: ")
                    if opt2=="Yes" or "yes":
                        print("The Menu is :")
                        print("1.Tandoori Chicken---4pieces----Rs.240")
                        print("2.Vegan Burger---1 piece----Rs.320")
                        print("3.Truffle Cake---500gms----Rs.900")
                    elif opt2=="no" or "No":
                        print("Thank you for ordering")
                                
                elif OD=="2":  
                    self.Ordered_list.append("Vegan Burger")
                    print("Item 2 is ordered",self.Ordered_list)
                    opt3=input("Do you wish to place order again,Yes or No")
                    if opt3=="Yes" or "yes":
                        print("The Menu is :")
                        print("1.Tandoori Chicken---4pieces----Rs.240")
                        print("2.Vegan Burger---1 piece----Rs.320")
                        print("3.Truffle Cake---500gms----Rs.900")
                    elif opt3=="no" or "No":
                        print("Thank you for ordering")
                                
                    
                elif OD=="3":
                    self.Ordered_list.append("Truffle Cake")
                    print("Item 1 is ordered",self.Ordered_list)
                    opt4=input("Do you wish to place order again,Yes or No")
                    if opt4=="Yes" or "yes":
                        print("The Menu is :")
                        print("1.Tandoori Chicken---4pieces----Rs.240")
                        print("2.Vegan Burger---1 piece----Rs.320")
                        print("3.Truffle Cake---500gms----Rs.900")
                    elif opt4=="no" or "No":
                        print("Thank you for ordering")
                            
                
                else:
                    print("please choose valid item")
                    break
    


            if option=="B" or option=="b":
                with open("Ordered_List.json","w")as f:
                    json.dump(self.Ordered_list,f)
                    print("Here are the list of items you have ordered")
                    return self.Ordered_list
            else:
                pass


            if option=="C" or option=="c":
                    with open("User_LoginDetails.json","r") as f:
                        Updated_List=json.load(f)
                            
                    print("Enter 1 for updating Name")
                    print("Enter 2 for updating Mobile Number")
                    print("Enter 3 for updating Email Id")
                    print("Enter 4 for updating Address")
                    print("Enter 5 for updating Password")
                    update_choice=input("Enter your choice : ")
                    
                    if update_choice=="1":
                        New_Name=input("enter a New name : ")
                        Updated_List["Name"]=New_Name
                        with open("User_LoginDetails.json","w") as f:
                            json.dump(New_Name,f)
                            return Updated_List
                            
                            
                    elif update_choice=="2":
                        New_Mobile_Number=input("enter a New Mobile Number : ")
                        if len(New_Mobile_Number)!=10:
                            print("Please enter correct mobile number")
                            break
                        else:
                            Updated_List["Mobile"]=New_Mobile_Number
                            with open("User_LoginDetails.json","w") as f:
                                json.dump(New_Mobile_Number,f)
                                print( Updated_List)
                                
                    elif update_choice=="3":
                        New_Email_Id = input("enter a New Email_Id ")
                        Updated_List["Email_Id"]=New_Email_Id
                        with open("User_LoginDetails.json","w") as f:
                            json.dump(New_Email_Id,f)
                            print(Updated_List)
                            
                    elif update_choice=="4":
                        New_Address = input("enter a New Address : ")
                        Updated_List["Address"]=New_Address
                        with open("User_LoginDetails.json","w") as f:
                            json.dump(New_Address,f)
                            print(Updated_List)
                            
                    elif update_choice=="5":
                        New_Password = int(input("enter a New Password : "))
                        if len(str(New_Password))!=8:
                            print("Please enter correct mobile number")
                            break
                        else:
                            Updated_List["Password"]=New_Password
                            with open("User_LoginDetails.json","w") as f:
                                json.dump(New_Password,f)
                                print(Updated_List)
                        
                    else:
                        pass
            
                        
                        
            if option =="D" or option == "d":
                print("***************Thank you for visiting us********************")
                sys.exit()
