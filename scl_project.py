from datetime import datetime
from itertools import product
from random import randint
from prettytable import *
import mysql.connector
from time import sleep
import requests
import json
import pyqrcode
from pyqrcode import *
import png
def generater():
    string = "https://github.com/codechan-dev/school_py/archive/refs/heads/main.zip"
    qr = pyqrcode.create(string)
    qr.png("qr.png",scale=10)


con=mysql.connector.connect(host="localhost",user="root",password="",database="pyconnect")
cur = con.cursor()
def greet():
    Time = datetime.now().hour
    if Time > 0 and Time < 12:
        print("Good morning")
    elif Time > 12 and Time < 16:
        print("Good afternoon")
    elif Time > 16 and Time < 19:
        print("Good afternoon")
    elif Time > 19 and Time < 24:
        print("Good evening")


def profile():
    print("name :",cust_name)
    print("age :",cust_age)
    print("address :",cust_address)
    menu()

def insert():
    a=input("enter dog name:")
    b=input("enter dog state")
    c=input("enter uses")

    sql = "INSERT INTO dogs (name, state,used) VALUES (%s, %s,%s)"
    val = [
      (a, b,c),
    ]

    cur.executemany(sql, val)

    con.commit()

    print(cur.rowcount, "was inserted.")



def admin():
    ad_details = ["admin", "password"]
    print("=================")
    print("Welcome to ADMIN PAGE")
    print("=================")
    while True:
        ad_username = input("Enter Admin's username : ")
        ad_password = input("Enter Admin's password : ")
        if ad_username != ad_details[0]:
            print("You have entered the wrong username")
            print("Please type the correct one")
            continue
        elif ad_password != ad_details[1]:
            print("You have entered the wrong password")
            print("Please type the correct one")
            continue
        else:
            print("Verified successfully")
            break
    choice = input("Do you want to see the customer detail records (y/n) : ")
    if choice == 'y' or choice == 'Y':
        cur.execute("select count(*) from orders")
        total = cur.fetchall()
    if total[0][0] == 0:
        print("No records found")
    else:
        print("\t\t CUSTOMERS DETAILS")
        cur.execute("SELECT * FROM orders")

        myresult = cur.fetchall()

        y=PrettyTable()
        y.field_names = ["name","quantity", "address", "phone", "id"]
        for x in myresult:
            y.add_row([x[0],x[1],x[2],x[3],x[4]])
        print(y)
        insert()
        menu()

def dd():
    
   
    
    
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="pyconnect"
    )
    
    
    mycursor = mydb.cursor()
    # greatings
    def greet():
        Time = datetime.now().hour
        if Time > 0 and Time < 12:
            print("Good morning")
        elif Time > 12 and Time < 16:
            print("Good afternoon")
        elif Time > 16 and Time < 19:
            print("Good afternoon")
        elif Time > 19 and Time < 24:
            print("Good evening")
    
    def end():
        print("Visit again, Have a nice day")
        exit()
    
    def db():
        d = datetime.now().strftime("%d - %m - %y")
        t = datetime.now().strftime("%H : %M : %S")
        cur.execute("insert into details values (null, '{}', {}, {}, '{}', '{}', '{}','{}')".format(cust_name, cust_age, username, purchased_products[0],
        cust_address, d, t))
        con.commit()
        end()
    
        purchased_products = []
        def cart():
            receipt = PrettyTable([" ", "Details"])
            receipt.add_row(["Name", cust_name])
            receipt.add_row(["Age", cust_age])
            receipt.add_row(["Contact number", username])
            receipt.add_row(["Products", purchased_products[0]])
            receipt.add_row(["Shipping address", cust_address])
            print(receipt)
            choice = input("Confirmation to place the order (y/n) : ")
        if choice == 'y' or choice == 'Y':
            print("Payment method will be 'Cash On Delivery'")
            print("Online payment method is not available at this moment ....SORRY for the inconvenience")
            print("Thank you {cust_name}, Your order will reach you within 2-3days")
            db()
    
    def create():
         mycursor.execute("CREATE TABLE dogs (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), state VARCHAR(255),used VARCHAR(255))")
    def profile():
        print(f"Name : {cust_name}")
        print(f"Age : {cust_age}")
        print(f"Contact number : {username}")
        print(f"Address : {cust_address}")
        menu()
    
    def admin():
        ad_details = ["pythoncoder", "pycharm"]
        print("=================")
        print("Welcome to ADMIN PAGE")
        print("=================")
        while True:
                ad_username = input("Enter Admin's username : ")
                ad_password = input("Enter Admin's password : ")
                if ad_username != ad_details[0]:
                    print("You have entered the wrong username")
                    print("Please type the correct one")
                    continue
                elif ad_password != ad_details[1]:
                    print("You have entered the wrong password")
                    print("Please type the correct one")
                    continue
                else:
                    print("Verified successfully")
                    break
        choice = input("Do you want to see the customer detail records (y/n) : ")
        if choice == 'y' or choice == 'Y':
            cur.execute("select count(*) from details")
            total = cur.fetchall()
            if total[0][0] == 0:
                print("No records found")
            else:
                print("\t\t CUSTOMERS DETAILS")
                cur.execute("select * from details")
                a = cur.fetchall()
                for i in a:
                    print(i)
        else:
            print("Thank you")
            menu()
    
    
    def display():
        mycursor.execute("SELECT * FROM dogs")
    
        myresult = mycursor.fetchall()
    
        for x in myresult:
          print(x)
    def insert():
        a=input("enter dog name:")
        b=input("enter dog state")
        c=input("enter uses")
    
        sql = "INSERT INTO dogs (name, state,used) VALUES (%s, %s,%s)"
        val = [
          (a, b,c),
        ]
    
        mycursor.executemany(sql, val)
    
        mydb.commit()
    
        print(mycursor.rowcount, "was inserted.")
    def menu():
        print("Available options :")
        print("1. create")
        print("2. display")
        print("3. insert")
        print("4. exit")
        choice = int(input("Enter your choice (Type number) : "))
        if choice not in [1, 2, 3, 4]:
            print("Please select the correct option")
            menu()
        elif choice == 1:
            create()
        elif choice == 2:
            display()
        elif choice == 3:
            insert()
        else:
           end()
    
    greet()
    
    menu()

def status():
    print("order placed.")



def menu():
    print("Available options :")
    print("1. Admin Page")
    print("2. Profile")
    print("3. dogs")
    print("4.order status")
    print("5. generate project download qr")
    choice = int(input("Enter your choice (Type number) : "))
    if choice not in [1, 2, 3, 4]:
        print("Please select the correct option")
        menu()
    elif choice == 1:
        admin()
    elif choice == 2:
        profile()
    elif choice == 3:
        dogs()
    elif choice == 4:
        status()
    elif choice ==5:
         generater()
    else:
         exit()





def login():
    u_details = ["user1", "password"]
    print("=================")
    print("Welcome to user PAGE")
    print("=================")
    while True:
        ad_username = input("Enter  username : ")
        ad_password = input("Enter  password : ")
        if ad_username != u_details[0]:
            print("You have entered the wrong username")
            print("Please type the correct one")
            continue
        elif ad_password != u_details[1]:
            print("You have entered the wrong password")
            print("Please type the correct one")
            continue
        else:
            print("Verified successfully")
            break



def dogs():
    cur.execute("SELECT * FROM details")

    myresult = cur.fetchall()

    y=PrettyTable()
    y.field_names = ["id", "type", "name", "age", "price"]
    for x in myresult:
        y.add_row([x[0],x[1],x[2],x[3],x[4]])
    print(y)
    quantity()
    ins()
    print("order placed successfully")


def ins():
    sql = "INSERT INTO orders (name,quantity, address,phone,id) VALUES (%s, %s,%s,%s,%s)"
    val = (cust_name ,1,cust_address,cust_phone,product)
    cur.execute(sql, val)
    con.commit()


def quantity():
    global product
    product=int(input("enter the 'id'  to order:"))

    


product=0
cust_name = ""
cust_age = ""
cust_address = ""
cust_phone=""
def home():
    global cust_name, cust_age, cust_address,cust_phone
    cust_name = input("Enter your name : ")
    cust_age = int(input("Enter your age : "))
    print("Enter the city name alone for shipping address ...")
    cust_address = input("Enter shipping address : ")
    cust_phone=input("enter your phone number")

if __name__ == "__main__":
    greet()
    print("Dont use alphabets or special characters for username")
    print("Use your valid mobile number, it will send you an OTP")
    home()
    login()
    menu()
    
   
