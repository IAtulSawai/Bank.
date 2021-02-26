import sys
data={'1234':{'Name': 'Atul', 'Pin': '1234', 'Amount': '1000', 'Account Type': 'Saving', 'Address': 'Bhopal'},
      '1235':{'Name': 'Many', 'Pin': '1235', 'Amount': '1000', 'Account Type': 'Saving', 'Address': 'Indore'}}

list1=["Name","Pin","Amount","Account Type","Address"]


def new_line():
    print("------------------------------------------------------------")

def account_creation():
    acc_num = input("Enter Account Number :")

    for item in list1:
        list2.append(input("Enter %s:" % item))
    data[acc_num] = dict(zip(list1, list2))
    # print(data)
    print("Account Created")
    print("Please Remember Your Pin And Account Number !!")
    new_line()
    return

#Function for Withdraw Amount
def withdraw_amt():
    new_line()
    amt = int(input("Enter Amount To Withdraw : "))

    if int(data[acc_num]["Amount"]) > amt and (int(data[acc_num]["Amount"]) - amt) >= 500:
        new_amt = int(data[acc_num]["Amount"]) - amt
        data[acc_num]["Amount"] = new_amt

        print("Withdraw Successful !!")
        print("Available Balance is : ", data[acc_num]["Amount"])
        new_line()

    else:
        print("Insufficient Amount !! \nMinimum Balance Should Be 500 ")
        print("Your Available Balance is :", data[acc_num]["Amount"])
        new_line()


#Function For Deposit Amount
def deposit_amt():
    new_line()
    amt = int(input("Enter Amount To Deposite : "))
    new_amt = int(data[acc_num]["Amount"]) + amt
    data[acc_num]["Amount"] = new_amt
    new_line()
    print(" Deposit Successful !!")
    print("Available Balance is : ", data[acc_num]["Amount"])
    new_line()

def other_opt():
    new_line()
    ch=int(input("1.Check Balance :\n2.Withdraw Amount :\n3.Deposit Amount :\n>>>>Please Enter Your Choice :"))
    if ch==1:
        print("Available Balance is :",data[acc_num]["Amount"])
        new_line()

    elif ch==2:
        withdraw_amt()

    elif ch==3:
        deposit_amt()


def int_rate():
    new_line()
    ch2 = int(input("1.Saving :\n2.FD : \n3.HomeLoan : \n4.Education Loan\n5.Exit :\n>>>>Enter Your Choice :"))
    dict1 = {
        "saving": {"Saving Balance upto <<Rs.50Lc": "3.50%p.a.", "Saving Deposite Balance >>Rs.50L": "4.00%p.a."},
        "FD": {"For 15 to 45 Days": "4.50%", "For 46 to 90 Days": "4.75%", "For 91 to 180 Days": "5.50%",
               "For 181 to 270 Days": "5.90%"},
        "Home Loan": "8.20% to 9.50%",
        "Education Loan": "10.09% to 11.75%"}

    if ch2 == 1:
        for key, value in dict1["saving"].items():
            print(key, ":", value)
        new_line()
    elif ch2 == 2:
        for key, value in dict1["FD"].items():
            print(key, ":", value)
        new_line()
    elif ch2 == 3:
        print("Home Loan",dict1["Home Loan"])
        new_line()
    elif ch2 == 4:
        print("Education Loan ",dict1["Home Loan"])

        new_line()
    else:

        new_line()

def other_services():
    ch1 = int(input("1.Bank Details :\n2.Interest Rate Check :\n3.Lockers :\n>>>>Please Enter Your Choice :"))

    if ch1 == 1:
        new_line()
        acc_num = input("Enter Your Account Number : ")
        acc_pin = input("Enter Your Pin : " )

        if acc_num in data and data[acc_num]["Pin"] == acc_pin:
            for key ,value in data[acc_num].items():
                print(key,">>>",value)
        new_line()

    elif ch1==2:
       int_rate()

    elif ch1==3:
        new_line()
        ch3=int(input("Want Lockers :\nPress 1 if Yes :\nPress 2 if no :\n>>>>"))
        if ch3==1:
            acc_num = input("Enter Your Account Number : ")
            acc_pin = input("Enter Your Pin : ")
            if acc_num in data and data[acc_num]["Pin"] == acc_pin:
                print("Locker Granted")
            new_line()
        elif ch3==2:
            print("Thankyou For Visiting !!\n Stay Safe :-)")
            new_line()


#RunCode
while True:
    list2=[]
    ch=int(input("1.New Customer :\n2.Existing Customer :\n3.Other Services :\n4.Exit :\n>>>>Enter Your Choice : "))
    new_line()
    if ch==1:
        account_creation()
    elif ch==2:
        acc_num=input("Enter Your Account Number : ")
        acc_pin=input("Enter Your Pin : ")
        if acc_num in data and data[acc_num]["Pin"] == acc_pin:
            print("Record Found !")
            other_opt()
        else:
            print("Record Not Found !!\nPlease Enter Correct Account Number And Password !!")
            print("------------------------------------------------------------")

    elif ch==3:
        other_services()
    elif ch==4:
        sys.exit()

