import pymysql as sql
import random
db=sql.connect(host='localhost',port=3306,user='root',password='',database='bank')
c=db.cursor()
print("connected")

def display():
    print("\n\n\t\t\t\t\t\tWELCOME IN APNA BANK ATM PORTAL MENU......")
    print("\n\n\n")
    print("\t\t\t PRESS 1 OPEN ACCOUNT:\t\t\t\t PRESS 2 WIDTHRAWAL MONEY:")
    print("\n")
    print("\t\t\t PRESS 3 DEPOSIT MONEY:\t\t\t\t PRESS 4 MINI STATEMENT:")
    print("\n")
    print("\t\t\t PRESS 5 PIN CHANGE:\t\t\t\t PRESS 6 CHANGE MOBILE_NO.:")
    y=int(input("Enter your choice:"))
    if y==1:
        opening_account()
    if y==2:
        widthdrawal_money()
    if y==3:
        deposit_money()
    if y==4:
        mini_statement()
    if y==5:
        pin_change()
    if y==6:
        mobile_number()
def opening_account():
    print("\n\n\n\t\t\t\t\t WELCOME NEW USER TO OPEN A ACCOUNT IN APNA BANK")
    print("\n\n\n\t\t\t\t\t Enter your details to opening a bank account")
    adhar_no=input("\n\n\n\t\t\t Enter your Adhar_Number:")
    name=input("\n\n\n\t\t\t Enter your Name:")
    fname=input("\n\n\n\t\t\t Enter your Father_Name:")
    mname=input("\n\n\n\t\t\t Enter your Mother_Name:")
    dob=input("\n\n\n\t\t\t Enter your DOB:")
    nomini1=input("\n\n\n\t\t\t Enter your NOMINI1:")
    nomini2=input("\n\n\n\t\t\t Enter your NOMINI2:")
    address=input("\n\n\n\t\t\t Enter your ADDRESS:")
    mobile_no=input("\n\n\n\t\t\t Enter your MOBILE_NUMBER:")
    alter_m_no=input("\n\n\n\t\t\t Enter your ALTER_MOBILE_NUMBER:")
    mail=input("\n\n\n\t\t\t Enter your MAIL_ID:")
    official_add=input("\n\n\n\t\t\t Enter your OFFICIAL_ADDRESS:")
    pan=input("\n\n\n\t\t\t Enter your PAN_CARD_NO.:")
    opening_bala=input("\n\n\n\t\t\t Enter your OPENING_BALANCE:")
    pin=random.randint(1111,9999)
    cmd="insert into bank values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(adhar_no,name,fname,mname,dob,nomini1,nomini2,address,mobile_no,alter_m_no,mail,official_add,pan,pin,opening_bala)   c.execute(cmd)
    db.commit()
    print("\n\n\n\t\t\t\t\t\t YOUR ACCOUNT IS SUCESSFULLY CREATED")
    print("\n\n\t\t\t\t\t\t THANKS FOR USING THIS ATM......")
    print("\n\n\n\t\t YOUR PIN NUMBER IS",pin)
    print("\n\n\n\t\t DON'T SHARE YOUR PIN NUMBER TO ANYONE")


def widthdrawal_money():
    print("\n\n\t\t\t\t WELCOME IN APNA BANK TO WIDTHDRAWAL MONEY....")
    i=input("\n\t\t\t Enter your adhar_no:")
    p=int(input("\n\t\t\t Enter the pin:"))
    cmd="select name from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t\t\t WELCOME IN APNA BANK......",z)
    
    cmd="select pin from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for a in var:
            if a==p:
                print("\n\t\t\t WELCOME.....")
    x=int(input("\n\t\t\t\t Enter the widthr_money:"))
    cmd="select opening_bala from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for b in var:
            print("\n\t\t\t\t Open_balan is:",b)
    w=int(b)-x
    print("\n\n\t\t\t\t Remaining balance is:",w);
    cmd="update bank set opening_bala=('{}') where adhar_no=('{}')".format(w,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")
 

def deposit_money():
    print("\n\n\n\t\t\t\t\t WELCOME USER TO WIDTHRAWAL A MONEY IN APNA BANK")
    i=input("\n\n\t\t\t\t Enter your adhar_no:")
    p=int(input("\n\t\t\t\t Enter your pin:"))
    cmd="select name from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t\t\t WELCOME IN APNA BANK.....",z)

    cmd="select pin from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                 print("\n\t\t\t YOUR PIN IS CORRECT..")
    x=int(input("\n\t\t\t\t Enter the deposit money:"))
    cmd="select opening_bala from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\t\t\t\t Open_balance is:",z)
    w=int(z)+x
    cmd="update bank set opening_bala=('{}') where adhar_no=('{}')".format(w,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\n YOUR CURRENT BALANCE IS:",w)
    print("\n\n\t\t\t\t\t THANKS FOR DEPOSITING THE MONEY FROM THIS ATM.......")
   


def mobile_number():
    print("\n\n\n\t\t\t\t\t WELCOME TO EDIT YOUR PHONE NUMBER")
    i=input("\n\n\t\t\t\t Enter your adhar_no:")
    p=int(input("\n\t\t\t\t Enter your pin:"))
    cmd="select name from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t\t\t WELCOME IN APNA BANK....",z)

    cmd="select pin from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    x=input("\n\t\t\t Enter your new mobie_number")
    cmd="update bank set mobile_no=('{}') where adhar_no=('{}')".format(x,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM.........")



def pin_change():
    print("\n\n\n\t\t\t\t\t WELCOME TO CHANGE YOUR PIN NUMBER")
    i=input("\n\n\t\t\t\t Enter your adhar_no")
    x=int(input("\n\t\t\t\t Enter your new pin"))
    cmd="select name from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t\t\t WELCOME IN APNA BANK.....",z)

    cmd="update bank set pin=('{}') where adhar_no=('{}')".format(x,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM.........")


def mini_statement():
    print("\n\n\n\t\t\t\t WELCOME IN MINI_STATEMENT")
    p=input("\n\n\t\t\t\t Please Enter your adhar_no")
    cmd="select name from bank where adhar_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t\t\t WELCOME IN APNA BANK.....",z)

    cmd="select opening_bala from bank where adhar_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\t\t\t\t YOUR BALANCE IS:",z)
            print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM.......")

def display_1():
    print("\n\n\t\t\t\t\t  WELCOME IN  EMPLOYEE PORTAL MENU")
    print("\n\n\n")

    print("\t\t\t PRESS 1 OPEN ACCOUNT:\t\t\t\t\t PRESS 2 CUSTOMER WIDTHRAWAL MONEY:")
    print("\n")
    print("\t\t\t PRESS 3 CUSTOMER DEPOSIT MONEY:\t\t\t PRESS 4 MINI STATEMENT:")
    print("\n")
    print("\t\t\t PRESS 5 CHANGE PROFILE:\t\t\t\t PRESS 6  CUSTOMER BALANCE:")
    print("\n\n")
    y=int(input("Enter your choice:"))
    if y==1:
        open_acc()
    if y==2:
        customer_width()
    if y==3:
        customer_deposit()
    if y==4:
        mini_statement()
    if y==5:
        edit_profile()
    if y==6:
        customer_bal()
    


def open_acc():
    print("\n\n\n\t\t\t\t WELCOME IN APNA BANK TO OPEN A NEW ACCOUNT IN EMPLOYEE PORATL.....")
    print("\n\n\t\t\t\t\t Enter your details to opening a bank account")
    id_no=input("\n\t\t\t\t Enter the customer id:")
    name=input("\n\n\t\t\t\t Enter the customer Name:")
    fname=input("\n\n\t\t\t\t Enter the customer Father_Name:")
    mname=input("\n\n\t\t\t\t Enter the customer Mother_Name:")
    dob=input("\n\n\t\t\t\t Enter the customer DOB:")
    address=input("\n\n\t\t\t\t Enter the customer Address:")
    nomini1=input("\n\n\t\t\t\t Enter the customer NOMINI1:")
    nomini2=input("\n\n\t\t\t\t Enter the customer NOMINI2:")
    mobile_no=input("\n\n\t\t\t\t Enter the customer MOBILE_NUMBER:")
    alter_mob_no=input("\n\n\t\t\t\t Enter the customer ALTER_MOBILE_NUMBER:")
    mail_id=input("\n\n\t\t\t\t Enter the customer MAIL_ID:")
    official_add=input("\n\n\t\t\t\t Enter the customer OFFICIAL_ADDRESS:")
    pan=input("\n\n\t\t\t\t Enter the customer PAN_CARD_NO.:")
    opening_bala=input("\n\n\t\t\t\t Enter the customer OPENING_BALANCE:")
    pin=random.randint(1111,9999)
    cmd="insert into employee values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id_no,name,fname,mname,dob,address,nomini1,nomini2,mobile_no,alter_mob_no,mail_id,official_add,pan,opening_bala,pin)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t YOUR  NEW CUSTOMER ACCOUNT IS SUCESSFULLY CREATED....")
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM BANKING......")
    print("\n\n\t YOUR PASSWORD IS",pin)
    print("\n\n\t\t\t\t\t\t\t` DON'T SHARE YOUR PASSWORD TO ANYONE......")

def customer_bal():
    print("\n\n\t\t\t\t WELCOME IN APNA BANK BANKING PORTAL......")
    i=input("\n\t\t\t Enter your customer id:")
    p=int(input("\n\t\t\t Enter the customer password:"))
    cmd="select pin from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("\n\n\t\t\t\t\t W_E_L_C_O_M_E I_N A_T_M.......")
    cmd="select name from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\t\t\t\t\t\t WELCOME IN APNA BANK....",z)

    cmd="select opening_bala from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for w in var:
            print("\n\t YOUR BALAENCE IS:",w)
    print("\n\n\t\t\t\t\t THANKS FOR USING ATM BANKING.....")


def customer_width():
    print("\n\n\t\t\t\t WELCOME IN APNA BANK TO WIDTHDRAWAL MONEY....")
    i=input("\n\t\t\t Please give your id_no:")
    p=int(input("\n\t\t\t Please give your password:"))
    cmd="select name from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t\t\t WELCOME IN APNA BANK......",z)
    cmd="select pin from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for a in var:
            if a==p:
                print("\n\t\t\t WELCOME.....")
    x=int(input("\n\t\t\t\t Enter the widthr_money:"))
    cmd="select opening_bala from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for b in var:
            print("\n\t\t\t\t Open_balan is:",b)
    w=int(b)-x
    print("\n\n\t\t\t\t Remaining balance is:",w);
    cmd="update employee set opening_bala=('{}') where id_no=('{}')".format(w,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def customer_deposit():
    print("\n\n\t\t\t\t WELCOME IN APNA BANK TO DEPOSIT MONEY")
    i=input("\n\n\t\t\t\t Please give your id_no:")
    p=int(input("\n\t\t\t\t Please give your password:"))
    cmd="select name from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t WELCOME IN APNA BANK.....",z)

    cmd="select pin from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("\n WELCOME.........")
    x=int(input("\n\t\t\t\t Enter the deposit money:"))
    cmd="select opening_bala from employee where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\t\t\t\t Open_balance is:",z)
    w=int(z)+x
    cmd="update employee set opening_bala=('{}') where id_no=('{}')".format(w,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")


def mini_statement():
    print("\t\t\t\t WELCOME IN APNA BANK")
    p=input("\n\n\t\t\t\t Please give your id_no")
    cmd="select name from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t\t WELCOME IN APNA BANK.....",z)

    cmd="select opening_bala from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\t\t\t\t YOUR BALANCE IS:",z)
            print("\n\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING.......")

def edit_profile():
    print("\n\n\n\t\t\t\t WELCOME IN APNA BANK EDITING PROFILE MENU...")
    print("\n\t\t\t Press 1 for edit the name:\t\t\t\t Press 2 for edit fname:")
    print("\n\t\t\t Press 3 for edit the mname:\t\t\t\t Press 4 for edit dob:")
    print("\n\t\t\t Press 5 for edit the address:\t\t\t\t Press 6 for edit mobile_no:")
    print("\n\t\t\t Press 7 for edit the mail_id:\t\t\t\t Press 8 for edit offiial_add:")
    print("\n\t\t\t Press 9 for edit the pan:\t\t\t\t Press 10 for edit alter_m_no:")
    print("\n\t\t\t Press 11 for edit the nomini1:\t\t\t\t Press 12 for edit nomini2:")
    print("\n\t\t\t Press 13 for edit the adhar_no:")
    x=int(input("\n\n\t\t\t Enter your choice:"))
    if x==1:
         edit_name()
    if x==2:
        edit_fname()
    if x==3:
        edit_mname()
    if x==4:
        edit_dob()
    if x==5:
        edit_add()
    if x==6:
        edit_mobile()
    if x==7:
        edit_mail()
    if x==8:
        edit_off_add()
    if x==9:
        edit_pan()
    if x==10:
        edit_alter_no()
    if x==11:
        edit_nomini1()
    if x==12:
        edit_nomini2()
    if x==13:
        edit_id_no()

def edit_name():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("ok")
    i=input("\n\t\t\t Enter your new name:")
    
    cmd="update employee set name=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_fname():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your fname:")
    
    cmd="update employee set fname=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_mname():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your mname:")
    
    cmd="update employee set mname=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_dob():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your dob:")
    
    cmd="update employee set dob=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_add():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your new address:")
    
    cmd="update employee set address=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_mail():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                    print("HELLO")
    i=input("\n\t\t\t Enter your new mail_id:")
    
    cmd="update employee set mail_id=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_mobile():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your new mobile_no:")
    
    cmd="update employee set mobile_no=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")


def edit_alter_no():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your another mobile_no:")
    
    cmd="update employee set alter_mob_no=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_off_add():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your new office_address:")
    
    cmd="update employee set official_add=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_pan():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your new pan:")
    
    cmd="update employee set pan=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")



def edit_nomini1():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your new nomini1:")
    
    cmd="update employee set nomini1=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")



def edit_nomini2():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t\t Please give your account_no")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your new nomini2:")
    
    cmd="update employee set nomini2=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_id_no():
    print("\n\n\t\t\t WELCOME IN EDITING MENU....")
    x=input("\t\t\t Enter your name:")
    p=input("\t\t\t\t Please give your password")
    cmd="select pin from employee where name=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter your new id_no:")
    
    cmd="update employee set id_no=('{}') where name=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t THANKS FOR USING THIS ATM BANKING")






def admin():
    print("\n\n\t\t\t\t WELCOME IN APNA BANK ADMINISTRATION")
    print("\n\n\n")
    print("\t\t\t PRESS 1 ADD EMPLOYEE:\t\t\t\t PRESS 2 EDIT PROFILE:")
    print("\n")
    print("\t\t\t PRESS 3 SALARY INCREMENT:\t\t\t PRESS 4 REMOVE EMPLOYEE:")
    print("\n")
    print("\t\t\t PRESS 5 EMPLOYEE PROMOTION:\t\t\t PRESS 6 EMPLOYEE TRANSFER")
    y=int(input("Enter your choice:"))
    if y==1:
        add_employee()
    if y==2:
        edit_profile()
    if y==3:
        salary_in()
    if y==4:
        remove_emp()
    if y==5:
        emp_promo()
    if y==6:
        emp_trans()

def salary_in():
    print("\n\n\t\t\t\t\t WELCOME IN ADMINISTRATION PORTAL...........")
    i=input("\n\n\t\t\t Enter the employee id_no:")
    x=input("\n\n\t\t\t Enter the employee paswword:")
    cmd="select pin from admins where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==x:
                print("\n\t\t\t HELLO")
    cmd="select salary from admins where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            print("\n\n\t\t\t WELCOME......")
    a=input("\n\n\t\t\t\t Enter the increase in salary")

    cmd="update admins set salary=salary+('{}') where id_no=('{}')".format(a,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\n YOUR EMPLOYEE SALARY IS SUCCESSFULY INCREASE")

def emp_promo():
    print("\n\n\t\t\t\t\t WELCOME IN ADMINISTRATION PORTAL...........")
    i=input("\n\n\t\t\t Enter the employee id_no:")
    x=input("\n\n\t\t\t Enter the employee paswword:")
    cmd="select pin from admins where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==x:
                print("\n\t\t\t HELLO")
    a=input("\n\n\t\t\t Your employee promotion:")
    cmd="update admins set designation=('{}') where id_no=('{}')".format(a,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\n\t\t\t\t CONGRESS... EMPLOYEE IS TO BE PROMATED")

def emp_trans():
    print("\n\n\t\t\t\t\t WELCOME IN ADMINISTRATION PORTAL...........")
    i=input("\n\n\t\t\t Enter the employee id_no:")
    x=input("\n\n\t\t\t Enter the employee paswword:")
    cmd="select pin from admins where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==x:
                print("\n\t\t\t HELLO")
    a=input("\n\n\t\t\t Employee is to be tranfer in new branch:")
    cmd="update admins set branch=('{}') where id_no=('{}')".format(a,i)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t CONGO... YOUR BANK EMPLOYEE IS TO BE TRANSFER IN NEW BRANCH........")

def remove_emp():
    print("\n\n\t\t\t\t\t WELCOME IN ADMINISTRATION PORTAL...........")
    i=input("\n\n\t\t\t Enter the employee id_no:")
    x=input("\n\n\t\t\t Enter the employee paswword:")
    cmd="select pin from admins where id_no=('{}')".format(i)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
                if z==x:
                    print("\n\t\t\t HELLO")
   
    cmd="delete from admins where id_no=('{}')".format(i)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t EMPLOYEE RECORD IS TO BE DELETED SUCCESSFULLY.......")
    
    


def add_employee():
    print("\n\n\t\t\t\t\t WELCOME IN ADD EMPLOYEE PORTAL")
    id_no=input("\n\n\n\t\t\t Enter Employee Id_no:")
    name=input("\n\n\t\t\t Enter Employee Name:")
    fname=input("\n\n\t\t\t Enter Employee Father Name:")
    relative_name=input("\n\n\t\t\t Enter Employee Relative Name:")
    dob=input("\n\n\t\t\t Enter Employee_DOB:")
    address=input("\n\n\t\t\t Enter Employee_Address:")
    office_add=input("\n\n\t\t\t Enter Employee_Official_Address:")
    mobile_no=input("\n\n\t\t\t Enter Employee_Mobileno:")
    alter_mob_no=input("\n\n\t\t\t Enter Employee_ Altermno:")
    bgroup=input("\n\n\t\t\t Enter blood_group:")
    mail_id=input("\n\n\t\t\t Enter Employee Mail_id:")
    designation=input("\n\n\t\t\t Enter your designation:")
    on_roll=input("\n\n\t\t\t Enter the employee on_roll:")
    off_roll=input("\n\n\t\t\t Enter the employee off_roll:")
    branch=input("\n\n\t\t\t Enter the branch:")
    grade=input("\n\n\t\t\t Enter the grade:")
    payskill=input("\n\n\t\t\t Enter the payskill:")
    department=input("\n\n\t\t\t Enter the department:")
    salary=input("\n\n\t\t\t Enter salary:")
    date_join=input("\n\n\t\t\t Enter the joining date of employee:")
    pin=random.randint(1111,9999)
    cmd="insert into admins values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id_no,name,fname,relative_name,dob,address,office_add,mobile_no,alter_mob_no,bgroup,mail_id,designation,on_roll,off_roll,branch,grade,payskill,department,salary,date_join,pin)
    c.execute(cmd)
    db.commit()
    print("\n\n\n\t\t\t\t\t YOU ARE SUCCESSFULLY ADD THE EMPLOYEE.....")
    print("\n\n\n\t\t\t\t\t YOUR NEW EMPLOYEE PASSWORD IS:",pin)
    print("\n\n\n\t\t\t WELCOME NEW EMPLOYEE IN APNA BANK.......THANKS BE A PART OF THIS BANK")

def edit_profile():
    print("\n\n\n\t\t\t\t WELCOME IN APNA BANK EDITING PROFILE MENU...")
    print("\n\t\t\t Press 1 for edit the name:\t\t\t\t Press 2 for edit fname:")
    print("\n\t\t\t Press 3 for edit the ref_name:\t\t\t\t Press 4 for edit dob:")
    print("\n\t\t\t Press 5 for edit the address:\t\t\t\t Press 6 for edit mobile_no:")
    print("\n\t\t\t Press 7 for edit the mail_id:\t\t\t\t Press 8 for edit office_add:")
    print("\n\t\t\t Press 9 for edit the joining_date:\t\t\t Press 10 for edit alter_m_no:")
    print("\n\t\t\t Press 11 for edit the designation:\t\t\t Press 12 for edit bgroup:")
    print("\n\t\t\t Press 13 for edit the id_no:\t\t\t\t Press 14 for edit branch:")
    print("\n\t\t\t Press 15 for edit the payskill:\t\t\t Press 16 for edit grade:")
    print("\n\t\t\t Press 17 for edit the salary:\t\t\t\t Press 18 for edit department:")
    x=int(input("\n\n\t\t\t Enter your choice:"))
    if x==1:
        edit_name()
    if x==2:
        edit_fname()
    if x==3:
        edit_rel_name()
    if x==4:
        edit_dob()
    if x==5:
        edit_add()
    if x==6:
        edit_mobile()
        
    if x==7:
        edit_mail()
    if x==8:
        edit_off_add()
    if x==9:
        edit_joindate()
    if x==10:
        edit_alter_no()
    if x==11:
        edit_designation()
    if x==12:
        edit_bgroup()
    if x==13:
        edit_id_no()
    if x==14:
        edit_branch()
    if x==15:
        edit_payskill()
    if x==16:
        edit_grade()
    if x==17:
        edit_salary()
    if x==18:
        edit_depart()
    
    
def edit_name():
    
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("hello")
    i=input("\n\t\t\t\t Enter your new name:")
    
    cmd="update admins set name=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM ...........")

def edit_fname():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your fname:")
    
    cmd="update admins set fname=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM ............")

def edit_rel_name():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter the rel_name:")
    
    cmd="update admins set relative_name=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM ...........")

def edit_dob():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your dob:")
    
    cmd="update admins set dob=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM ..........")

def edit_add():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your new address:")
    cmd="update admins set address=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM BANKING")

def edit_mail():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                    print("HELLO")
    i=input("\n\t\t\t\t Enter your new mail_id:")
    
    cmd="update admins set mail_id=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM..........")

def edit_mobile():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your new mobile_no:")
    cmd="update admins set mobile_no=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM..........")


def edit_alter_no():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your another mobile_no:")
    cmd="update admins set alter_mob_no=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .........")

def edit_off_add():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your new office_address:")
    cmd="update admins set office_add=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .........")

def edit_joindate():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your new join_date:")
    cmd="update admins set date_join=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM..........")



def edit_depart():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your new department:")
    cmd="update admins set department=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM ..........")



def edit_designation():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your new designation:")
    cmd="update admins set designation=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM ......")

def edit_id_no():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee name:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter your new id_no:")
    cmd="update admins set id_no=('{}') where name=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .......")

def edit_salary():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter the employee salary:")
    cmd="update admins set salary=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .......")


def edit_grade():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter the employee grade:")
    cmd="update admins set id_no=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .......")

def edit_payskill():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t\t Enter the employee skill:")
    cmd="update admins set payskill=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .......")


def edit_branch():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORATL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
    i=input("\n\t\t\t Enter the employee branch:")
    cmd="update admins set branch=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .......")


def edit_bgroup():
    print("\n\n\t\t\t\t\t WELCOME IN EDITING MENU IN ADMINISTRATION PORTAL....")
    x=input("\n\t\t\t\t Enter the employee id_no:")
    p=input("\n\t\t\t\t Please give your password:")
    cmd="select pin from admins where id_no=('{}')".format(p)
    c.execute(cmd)
    y=c.fetchall()
    for var in y:
        for z in var:
            if z==p:
                print("HELLO")
            
    i=input("\n\t\t\t\t Enter the bgroup:")
    cmd="update admins set bgroup=('{}') where id_no=('{}')".format(i,x)
    c.execute(cmd)
    db.commit()
    print("\n\n\t\t\t\t\t THANKS FOR USING THIS ATM .......")

def main():    
    print("\n\n\n\t\t\t\t  W_E_L_C_O_M_E   I_N   A_P_N_A   B_A_N_K   A_T_M..........")
    print("\n\t Press 1 for ATM:\t\t\t Press 2 for BANKING:\t\t\t Press 3 for ADMIN:")
    x=int(input("\n\n Enter your choice:"))
    if x==1:
        display()
    if x==2:
        display_1()
    if x==3:
        admin()
    i=int(input("\n\n\t\t IF YOU WANT TO CONTINUE PRESS 1:\t\t IF YOU WANT TO EXIT PRESS 2:"))
    if i==1:
        main()
    elif i==2:
        print("\n\n\t\t\t\t\t BYE BYE......")
        print("\n\n\t\t\t\t\t THANKS FOR USING THIS APPLICATION.........")
main()



