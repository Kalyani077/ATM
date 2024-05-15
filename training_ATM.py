import time
class ATM():
    def v(self,usernames,passwords,pin,balance):
        user = input("Enter the username:")
        time.sleep(1)
        if user not in usernames:
            print("invalid user")
        else:  
            index = usernames.index(user)  
            pas = input("enter password:")
            time.sleep(1)
            if pas not in passwords[index]:
                for i in range(2,-1,-1):
                    print("incorrect password",i,"attempts left")
                    time.sleep(1)
                    if i == 0:
                        print("maximum limit reached")
                        break
                        exit()
                    pas = input("enter password:")
            else:
                print("select an option:")
                time.sleep(1)
                print("1.Withdraw")
                time.sleep(1)
                print("2.deposit")
                time.sleep(1)
                print("3.Account balanace")
                time.sleep(1)
                print("4.change password")
                time.sleep(1)
                choice = int(input("enter your choice:"))
                time.sleep(1)
                if choice == 1:
                    amount = int(input("enter the amount:"))
                    time.sleep(1)
                    avail_balance = balance[index]-amount
                    pin_number = int(input("enter your pin:"))
                    time.sleep(1)
                    if pin_number != pin[index]:
                        print("invalid pin")
                    else:
                        if amount<=balance[index]:
                            print("collect the amount")
                            time.sleep(2)
                            print("Available Balance:",avail_balance)
                        else:
                            print("Insufficient balance")
                elif choice == 2:
                    deposit_amount = int(input("Enter the amount:"))
                    av_balance = balance[index]+deposit_amount
                    pin_number = int(input("enter your pin:"))
                    if pin_number != pin[index]:
                        print("invalid pin")
                    else:
                        print("amount deposited successfully")
                        print("Available Balance:",av_balance)
                elif choice == 3:
                    pin_number = int(input("enter your pin:"))
                    if pin_number != pin[index]:
                        print("invalid pin")
                    else:
                        print("available balance:",balance[index])
                elif choice == 4:
                    pas = input("enter password:")
                    if pas not in passwords[index]:
                        print("incorrect password")
                    else:
                        new_password = input("Enter your new password:")
                        confirm_password = input("please confirm the password:")
                        while new_password != confirm_password:
                            print("Re-Enter the password")
                            new_password = input("Enter your new password:")
                            confirm_password = input("please confirm the password:")
                        else:
                            print("password changed successfully")
                            exit()
                else:
                    print("invalid selection")
usernames = ["kalyani07","kallu08","hema34"]
passwords = ["23@hema","34@kallu","56@kalyani"]
pin = [1295,3456,7843]
balance = [1000,2567,567]
B = ATM()
B.v(usernames,passwords,pin,balance)