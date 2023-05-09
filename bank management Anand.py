#Bank management system
import mysql.connector
import datetime
conn=mysql.connector.connect(host='localhost',user='root',password='1234', database='anand')
if conn.is_connected():
    print("connection is established")
else:
    print("check connection....")
cur=conn.cursor()

#==============================================================================
def c_account():
    try:
        
        cur.execute("select * from account order by Acc_no asc")
        acid=cur.fetchall()
        if acid==[]:
            Cust_id='CID2345688'
            Acc_no=2345688
            First_name=input("\t ENTER FIRST NAME:")
            print("="*75)
            Last_name=input("\t ENTER LAST NAME :")
            print("="*75)
            while True:
                a=input("\t ENTER BIRTH YEAR :")
                print("="*75)
                if int(a)>1900 and int(a)<2022:
                    break
                else:
                    print("PLEASE PROVIDE VALID YEAR OF BIRTH...")
                    print("="*75)
            while True:
                b=input("\t ENTER THE MONTH OF BIRTH:")
                print("="*75)
                if int(b)<13 and int(b)>0:
                    break
                else:
                    print("PLEASE PROVIDE VALID BIRTH MONTH:")
                    print("="*75)
            while True:
                c=input("\t ENTER YOUR BITH DATE:")
                print("="*75)
                if int(c)>0 and int(c)<32:
                    break
                else:
                    print("PLEASE PROVIDE VALID DATE .......")
                    print("="*75)
                    

            Dob=a+'-'+b+'-'+c
            while True:
                Phone=input("\t ENTER MOBILE NUMBER:")
                print("="*75)
                if len(Phone)==10:
                    break
                else:
                    print("PLEASE ENTER VALID MOBILE NUMBER......")
                    print("="*75)
            Address=input("\t ENTER YOUR PERMANENT ADDRESS :")
            print("="*75)
            email=input("\t ENTER YOUR EMAIL ADDRESS :")
            print("="*75)
            while True:
            
                Acc_Type=input("\t ENTER ACCOUNT TYPE(SAVING/CURRENT):")
                print("="*75)
                l=["saving","current", "SAVING", "CURRENT"]
                if Acc_Type in l:
                    break
                else:
                    print("PLEASE PROVIDE VALID ACCOUNT TYPE....")
                    print("="*75)
            while True:
                Balance=int(input("\t ENTER BALANCE AMOUNT (>500):"))
                print("="*75)
                if Balance > 500:
                    break
                else :
                    print("...PLEASE PROVIDE SUFFICIENT BALANCE ....")
                    print("="*75)
            
            cur.execute("insert into customer values('{}','{}','{}','{}','{}','{}','{}')".format(Cust_id,First_name,Last_name,Dob,Phone,Address,email))
            cur.execute("insert into account values({},'{}','{}',{})".format(Acc_no,Cust_id,Acc_Type,Balance))
            conn.commit()
        else:
            ac1=acid.pop()
            ac2=ac1[0]
            ac3=ac2+2
            Acc_no=ac2+2
        

            Cust_id='CID'+str(Acc_no)
        
        

        
            First_name=input("\t ENTER FIRST NAME:")
            print("="*75)
            Last_name=input("\t ENTER LAST NAME :")
            print("="*75)
            while True:
                a=input("\t ENTER BIRTH YEAR :")
                print("="*75)
                if int(a)>1900 and int(a)<2022:
                    break
                else:
                    print("PLEASE PROVIDE VALID YEAR OF BIRTH...")
                    print("="*75)
            while True:
                b=input("\t ENTER THE MONTH OF BIRTH:")
                print("="*75)
                if int(b)<13 and int(b)>0:
                    break
                else:
                    print("PLEASE PROVIDE VALID BIRTH MONTH:")
                    print("="*75)
            while True:
                c=input("\t ENTER YOUR BITH DATE:")
                print("="*75)
                if int(c)>0 and int(c)<32:
                    break
                else:
                    print("PLEASE PROVIDE VALID DATE .......")
                    print("="*75)
                    

            Dob=a+'-'+b+'-'+c
            while True:
                Phone=input("\t ENTER MOBILE NUMBER:")
                print("="*75)
                if len(Phone)==10:
                    break
                else:
                    print("PLEASE ENTER VALID MOBILE NUMBER......")
                    print("="*75)
            Address=input("\t ENTER YOUR PERMANENT ADDRESS :")
            print("="*75)
            email=input("\t ENTER YOUR EMAIL ADDRESS :")
            print("="*75)
            while True:
            
                Acc_Type=input("\t ENTER ACCOUNT TYPE(SAVING/CURRENT):")
                print("="*75)
                l=["saving","current", "SAVING", "CURRENT"]
                if Acc_Type in l:
                    break
                else:
                    print("PLEASE PROVIDE VALID ACCOUNT TYPE....")
                    print("="*75)
            while True:
                Balance=int(input("\t ENTER BALANCE AMOUNT (>500):"))
                print("="*75)
                if Balance > 500:
                    break
                else :
                    print("...PLEASE PROVIDE SUFFICIENT BALANCE ....")
                    print("="*75)
        
            cur.execute("insert into customer values('{}','{}','{}','{}','{}','{}','{}')".format(Cust_id,First_name,Last_name,Dob,Phone,Address,email))
            cur.execute("insert into account values('{}','{}','{}',{})".format(Acc_no,Cust_id,Acc_Type,Balance))
            conn.commit()
        print("\t ACCOUNT CREATED....")
        print("\t YOUR ACCOUNT NUMBER IS:\t", Acc_no)
        print("\t CUSTOMER ID IS :\t\t", Cust_id)
        print("\t PLEASE DO NOT FORGET THE ACCOUNT NUMBER AND CUSTOMER ID")
        print("\t THANK YOU FOR VISITING...")
    except Exception as  e:
        print("DATABASE ERROR:\t ",e)
#=====================================================================================================================================================
def d_account():
    try:
        cur.execute("select *  from customer c ,account a where c.Cust_id=a.Cust_id;")
        data=cur.fetchall()
        
        for i in data:
            print("ACCOUNT NUMBER \t\t:",i[7])
            print("CUSTOMER ID \t\t:",i[0])
            print("FIRST NAME \t\t:",i[1])
            print("LAST NAME \t\t:",i[2])
            print("DATE OF BIRTH \t\t:",i[3])
            print("PHONE NUMBER \t\t:",i[4])
            print("ADDRESS \t\t:",i[5])
            print("EMAIL ID \t\t:",i[6])
            print("TYPE OF ACCOUNT \t:",i[9])
            print("BANK BALANCE \t\t:",i[10])
            print("="*75)
        
    except Exception as  e:
        print("database error",e)

#==============================================================================================================================================================
def m_account():
    try:
        Custid=input("enter  customer id whose details are to be updated:")

        First_name=input("enter updated first name:")
        Last_name=input("enter updated last name :")
        Dob=input("enter updated date of birth (yyyy-mm-dd):")
        Phone=input("enter updated phone number:")
        Address=input("enter updated address :")
        email=input("enter updated email id :")
        while True:
            
            Acc_Type=input("enter updated account type (saving/current):")
            l=["saving","current","SAVING","CURRENT"]
            if Acc_Type in l:
                break
            else:
                print("please provide valid account type....")
        cur.execute("update customer set Cust_id='{}',First_name='{}',Last_name='{}',Dob='{}',Phone='{}',Address='{}',email='{}' where Cust_id = '{}'".format(Custid,First_name,Last_name,Dob,Phone,Address,email,Custid))
        conn.commit()
        print("account details updated....")
    except Exception as  e:
        print("Please provide valid customer id.......")
    
#========================================================================================================================================================================    
def cl_account():
    try:

        Cust_id=input("enter  customer id whose account is to be closed:")
        
        cur.execute("delete from account where Cust_id='{}'".format(Cust_id))
        cur.execute("delete from customer where Cust_id='{}'".format(Cust_id))
        conn.commit()
        
        print("Account successfully deleted.......")
    except Exception as  e:
        print("please provide valid customer id...",e)
#==========================================================================================================================================================================        
def withdraw_amount():
    try:
        acno=int(input("Enter account number:"))
        wd=float(input("Enter amount to be withdrawn:"))
        dot=datetime.datetime.today()
        ttype="WD"
        cur.execute("select CUST_ID from account where ACC_NO='{}'".format(acno))
        nh=cur.fetchone()
        q=nh[0]
        cur.execute("select Balance from account where ACC_NO='{}'".format(acno))
        row=cur.fetchone()
        p=row[0]
        n=float(p)-wd
        if n<500:
            print("The transaction can't take place as the criteria of minimum balance will not be fulfilled")
        else:
            cur.execute("insert into transaction (CUST_ID, Amount, TRANS_TYPE, TRANS_DATE) values('{}',{},'{}','{}')".format(q, wd, ttype, dot))
            cur.execute("update account set balance = {} where ACC_NO='{}'".format(n, acno))
            conn.commit()
            print("The Amount is withdrawn")
    except Exception as e:
        print(e)
        
#==========================================================================================================================================================================        
def Deposit_amount():
    try:
        
        acno=int(input("Enter account number:"))
        dp=float(input("Enter amount to be deposited:"))
        dot=datetime.datetime.today
        ttype="DEPOSIT"
        cur.execute("select CUST_ID from account where ACC_NO='{}'".format(acno))
        nh=cur.fetchone()
        q=nh[0]
        cur.execute("select Balance from account where ACC_NO='{}'".format(acno))
        row=cur.fetchone()
        p=row[0]
        z=p+float(dp)
        cur.execute("insert into transaction(CUST_ID, Amount, TRANS_TYPE, TRANS_DATE) values('{}',{},'{}','{}')".format(q, dp, ttype, dot))
        cur.execute("update account set balance={} where ACC_NO='{}'".format(z, acno))
        conn.commit()
        print("Amount has been deposited successully!!!")
    except Exception as e:
        print(e)
        
#========================================================================================================================================================================== 
def balance_enquiry():
    try:
        acno=int(input("Enter the account number for which you want to check the amount"))
        cur.execute("select Balance from account where ACC_NO='{}'".format(acno))
        row=cur.fetchone()
        p=row[0]
        print("The balance in your account is:",p)
    except Exception as e:
        print(e)
#========================================================================================================================================================================== 
def show_cust_id():
    pan=input("ENTER THE FIRST NAME OF THE ACCOUNT HOLDER")
    while True:
        a=input("\t ENTER BIRTH YEAR :")
        if int(a)>1900 and int(a)<2022:
            break
        else:
            print("PLEASE PROVIDE VALID YEAR OF BIRTH...")
    while True:
        b=input("\t ENTER THE MONTH OF BIRTH:")
        if int(b) and int(b)>0:
            break
        else:
            print("PLEASE PROVIDE VALID BIRTH MONTH:")
    while True:
        c=input("\t ENTER YOUR BITH DATE:")
        if int(c)>0 and int(c)<32:
            break   
        else:
            print("PLEASE PROVIDE VALID DATE .......")
                    

    Dob=a+'-'+b+'-'+c
    cur.execute("select * from customer where first_name='{}' and dob='{}'".format(pan,Dob))
    acid=cur.fetchall()
    print("Your account details are:",acid)

def show_acc_no():
    pan=input("ENTER THE FIRST NAME OF THE ACCOUNT HOLDER")
    while True:
        a=input("\t ENTER BIRTH YEAR :")
        if int(a)>1900 and int(a)<2022:
            break
        else:
            print("PLEASE PROVIDE VALID YEAR OF BIRTH...")
    while True:
        b=input("\t ENTER THE MONTH OF BIRTH:")
        if int(b) and int(b)>0:
            break
        else:
            print("PLEASE PROVIDE VALID BIRTH MONTH:")
    while True:
        c=input("\t ENTER YOUR BITH DATE:")
        if int(c)>0 and int(c)<32:
            break
        else:
            print("PLEASE PROVIDE VALID DATE .......")
                    

    Dob=a+'-'+b+'-'+c
    cur.execute("select cust_id from customer where first_name='{}' and dob='{}'".format(pan,Dob))
    acid=cur.fetchall()
    n=acid[0][0]
                    

    Dob=a+'-'+b+'-'+c
    cur.execute("select acc_no from account where CUST_ID='{}'".format(n))
    nd=cur.fetchall()
    print("Your account number is:",nd)



#========================================================================================================================================================================== 
def bank_statement():
    pan=input("ENTER THE FIRST NAME OF THE ACCOUNT HOLDER")
    while True:
        CUST_ID=input("Enter the CUSTOMER ID of the account holder")
        cur.execute("select CUST_ID from customer")     
        new=cur.fetchall()
        m=1
        for i in new:  
            if i[0]==CUST_ID:
                m=2
        if m==2:
            break
        else:
            print("Enter a valid Customer ID")
    cur.execute('select * from transaction where CUST_ID="{}"'.format(CUST_ID))
    data=cur.fetchall()
    if data!=[]:
        
        for i in data:
            print("TRANSACTION ID \t\t:",i[0])
            print("CUSTOMER ID \t\t:",i[1])
            print("TRANSACTION TYPE \t:",i[2])
            print("TRANSACTION DATE \t:",i[3])
            print("AMOUNT \t\t\t:",i[4])

            print("="*75)
    else:
        print("No transaction has taken place with the given Account")
    
'''
while True:
    print("="*75)
    print("\t\t 1.create new account.")
    print("\t\t 2.Display all account holders.")
    print("\t\t 3.Close or delete an account.")
    print("\t\t 4.Modify your account.")
    print("\t\t 5.withdraw amount")
    print("\t\t 6.Deposit amount")
    print("\t\t 7.Balance enquiry")
    print("\t\t 8.exit")
    print("="*75)
    ch=int(input("input your choice:"))
    print("="*75)
    if ch==1:
        c_account()
    elif ch==9:
        show_cust_id()
    elif ch==10:
        show_acc_no()
    elif ch==2:
        d_account()
    elif ch== 4:
        m_account()
    elif ch==3:
        cl_account()
    elif ch==5:
        withdraw_amount()
    elif ch==6:
        Deposit_amount()
    elif ch==7:
        balance_enquiry()
    elif ch==8:
        break
    else :
        print("please provide valid input.....")
    
        
    
'''
while True:
    print("*"*80)
    print(" \t\t  ⚡⚡⚡ ANAND AND CO. BANK WELCOMES YOU ⚡⚡⚡ ")
    print("*"*80)
    print(" \t\t  ⚡⚡⚡ OUR BANK SERVICES ⚡⚡⚡ ")
    print("*"*80)
    
    print("\t\t 1.☞ CREATE NEW ACCOUNT  ")
    print("\t\t 2.☞ DISPLAY ALL ACCOUNT HOLDERS  ")
    print("\t\t 3.☞ CLOSE OR DELETE AN ACCOUNT ")
    print("\t\t 4.☞ MODIFY YOUR ACCOUNT ")
    print("\t\t 5.☞ WITHDRAW ACCOUNT " )
    print("\t\t 6.☞ DEPOSIT AMOUNT ")
    print("\t\t 7.☞ BALANCE ENQUIRY")
    print("\t\t 8.☞ CHECK YOUR CUSTOMER ID  ")
    print("\t\t 9.☞ CHECK YOUR ACCOUNT NUMBER  ")
    print("\t\t10.☞ PRINT CUSTOMER'S BANK STATEMENT  ")
    
    print("\t\t11.☞ EXIT  ")
    print("*"*80)
    ch=int(input("Input Your Choice:"))
    print("*"*80)
    if ch==1:
        c_account()
    elif ch==2:
        d_account()
    elif ch== 4:
        m_account()
    elif ch==3:
        cl_account()
    elif ch==5:
        withdraw_amount()
    elif ch==6:
        Deposit_amount()
    elif ch==7:
        balance_enquiry()
    elif ch==8:
        show_cust_id()
    elif ch==9:
        show_acc_no()
    elif ch==10:
        bank_statement()
    elif ch==11:
        print("Thank you For visiting ANAND CO. BANK")
        break
    else :
        print("Please Provide Valid Input.....")

    
    
