#I wrote   my code with these methods:Loops,function,dictionary,list,if-else,sqlite,class
class customer ():
    name=""
    bill=0


Menus={"Menu1":3.75,"Menu2":3.5}#Menus["Menu1"]
Meals={"Hamburger":2.5,"Chickenburger":2,"Frenchfries":0.5}
Drinks={"Water":0.25,"Coke":0.75,"Milkshake":0.75,"Coffee":1,"Orangejuice":1}
Desserts={"Ice Cream ":1,"Donut":1.25}

meals=["Hamburger","Chickenburger","Frenchfries"]
drinks=["Water","Coke","Milkshake","Coffee","Orangejuice"]
desserts=["Ice Cream","Donut"]
Menu1_list=[ "Menu1" ,"Hamburger + Frenchfries + Coke","=3.75$"]
Menu2_list=["Menu2","Chickenburger + Frenchfries + Coke","=3.50$"]

dolar="$"
bill=0
products=[]
products_names=""
Number_of_products=[]

print("WELCOME! to the Project Restaurant")
Username=input("Please enter your name:")

while True:
   Choice_1 = input("Choose:[1]Menus [2]Meals [3]Drinks [4]Dessert")
   if int(Choice_1) == 1 :

          print(Menu1_list,"\n",Menu2_list)
          Choice_2=input("Choose: [1]Menu1=3.75$ or [2]Menu2=3.50$ ")

          if int(Choice_2) == 1 :
            print(Menu1_list)
            HM1=input("How many Menu 1 would like to buy?") #HM = How many
            bill += Menus["Menu1"] * int(HM1)
            products.append(Menu1_list[0])
            Number_of_products.append(int(HM1))
            products_names+=products.pop()+'+'

          elif int(Choice_2) == 2 :
            print(Menu2_list)
            HM2=input("How many Menu 2 would you like to buy?")
            bill += Menus["Menu2"] * int(HM2)
            products.append(Menu2_list[0])
            Number_of_products.append(int(HM2))
            products_names += products.pop() + '+'
   elif int(Choice_1) == 2 :

         print(meals)
         Choice_3=input("Choose: [1]Hamburger=2.50$ [2]Chickenburger=2$ [3]Frenchfries=0.5$")

         if int(Choice_3) == 1 :
            HM3=input("How many Hamburger would you like to buy?")
            bill += Meals["Hamburger"] * int(HM3)
            products.append(meals[0])
            Number_of_products.append(int(HM3))
            products_names += products.pop() + '+'

         elif int(Choice_3) == 2 :
            HM4=input("How many Chickenburger would you like to buy?")
            bill += Meals["Chickenburger"]* int(HM4)
            products.append(meals[1])
            Number_of_products.append(int(HM4))

            products_names += products.pop() + '+'
         elif int(Choice_3) == 3 :
            HM5=input("How many portions of french fries would you like to buy?")
            bill += Meals["Frenchfries"] * int(HM5)
            products.append(meals[-1])
            Number_of_products.append(int(HM5))
            products_names += products.pop() + '+'

   elif int(Choice_1) == 3 :
         print(drinks)
         Choice_4=input("Choose: [1]Water=0.25$ [2]Coke=1$ [3]Milkshake=0.75$ [4]Coffee=1$ [5]Orangejuice=1$")

         if int(Choice_4) == 1:
            HM6=input("How many bottle of water would you like to buy ?")
            bill += Drinks["Water"] * int(HM6)
            products.append(drinks[0])
            Number_of_products.append(int(HM6))
            products_names += products.pop() + '+'

         elif int(Choice_4) == 2 :
            HM7=input("How many can of coke would you like to buy?")
            bill += Drinks["Coke"] * int(HM7)
            products.append(drinks[1])
            Number_of_products.append(int(HM7))
            products_names += products.pop() + '+'

         elif int(Choice_4) == 3 :
            HM8=input("How many glass of milkshake would you like to buy?")
            bill += Drinks["Milkshake"] * int(HM8)
            products.append(drinks[2])
            Number_of_products.append(int(HM8))
            products_names += products.pop() + '+'

         elif int(Choice_4) == 4 :
            HM9=input("How many cup of coffee would you like to buy?")
            bill += Drinks["Coffee"] * int(HM9)
            products.append(drinks[3])
            Number_of_products.append(int(HM9))
            products_names += products.pop() + '+'


         elif int(Choice_4) == 5 :
            HM10=input("How many glass of orangejuice would you like to buy?")
            bill += Drinks["Orangejuice"] * int(HM10)
            products.append(drinks[-1])
            Number_of_products.append(int(HM10))
            products_names += products.pop() + '+'

   elif int(Choice_1) == 4 :
         print(desserts)
         Choice_5=input("Please Choose:[1]Icecream=1$ [2]Donut=1.25$")

         if int(Choice_5) == 1 :
            HM11=input("How many cornet of ice cream would you like to buy?")
            bill += Desserts["Ice Cream "] * int(HM11)
            products.append(desserts[0])
            Number_of_products.append(int(HM11))
            products_names += products.pop() + '+'

         elif int(Choice_5) == 2 :
            HM12=input("How many donat would you like to buy ? ")
            bill += Desserts["Donut"] * int(HM12)
            products.append(desserts[-1])
            Number_of_products.append(int(HM12))
            products_names += products.pop() + '+'
   else:

       try:
           if int(Choice_1) > 4 :
               print("You entered wrong number!")
       except ValueError:
           print("ERROR:Wrong number")

   status_1=input("Would you like to keep going? [1] Yes [2] No")

   if int(status_1) == 1:
       continue

   elif int(status_1) == 2:
        break

import payment_module
payment_module.method()

def init(self,Username,bill):
    self.name=Username
    self.bill=bill


print(Username,products_names,bill,dolar)

print(bill,"$")
order_register=open(r"order_register.txt","w")
order_register.write(Username)
order_register.write(str(products_names))
order_register.write(str(sum(Number_of_products)))
order_register.write(str(bill))
order_register.write("$")

import  sqlite3 as sql
data_base=sql.connect('database.db')
connection=data_base.cursor()
connection.execute("Create Table IF NOT EXISTS order_register(name,product_name,product_quantity,bill,dolar)")
search="insert into order_register (name,product_name,product_quantity,bill,dolar) VALUES ('"+Username+"','"+str(products_names)+"','"+str(sum(Number_of_products))+"','"+str(bill)+"','"+str(dolar)+"')"
connection.execute(search)
data_base.commit()
data_base.close()










