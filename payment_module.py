def method():
    payment_method=input("Please Choose payment method: [1]Credit Card/Cash  [2]Online : ")
    if int(payment_method) == 1 :
        print("Your order has been received please pay to the cashier")
    elif int(payment_method) == 2 :
         print("Connecting to payment provider...")
         import random # I try to explain  online payment failure chance with random numbers between 0 and 1 :)
         if  random.random() >= 0.5 :
             print("Connetcion successful! Payment completed.")
         elif random.random()  < 0.5 :
             print("Connection failed! Please pay to the cashier")
             return random


