import webbrowser 
import sys

url="www.hustlerfund.co.ke"

#hustler fund 

display_this=input("Welcome to the Financial Inclusion Platform, Please select,\n1.Hustler Fund.\n")
hustler_fund=["1.Personal Loan","2.Hustler Groups", "#.Home", "*.Back"]
personal_loan=["1.Loan","2.Savings", "3.About Hustler Fund","#.Home", "*.Back"]
hustler_groups=["1.MSEA","2.Unregistered(Create Group)","3.View Group Invite","#.Home","*.Back"]
savings_acc=["1.Long-Term Savings","2.Short-Term Savings", "#.Home","*.Back"]
loan_sel_opts=["1.Request My Loan","2.Repay My Loan","3.Check Loan Status","4.Opt Out","#.Home","*.Back"]
about_hustler=["1.What is Hustler Fund?","2.How Do I Qualify?","3.Get Bigger Loan","4.Interest Rate","5.Can I Get More Than one Loan?","#.Home","*.Back"]


user_pin=[]
#create a list to store phone numbers
phone_number_list=[]
#create a list to store group names
group_name_list=[]
#create a list to store ID numbers
id_no_list=[]

#function to store group name and prompt if already exists
def store_group_names():
    group_name=input("\nEnter a group name.")

    #check if group name already exists
    if group_name in group_name_list:
        print("\nGroup already Exists.Try Again Later.")
    #add group name to list
    else:
        group_name_list.append(group_name) 
        print("\nRegistration Success.")   
#function to store id numbers
def store_id_number():
    id=input("\nEnter your Identification Number to proceed.")

    #check if id exists
    if id in id_no_list:
        print("\nUser is already Registered.") 
    else:
        id_no_list.append(id)  
        print("\nRegistration Successful.\n")         
def store_phone_numbers():
    phone_number=input("\nEnter your phone number to proceed.")

    #check if phone number exists
    if phone_number in phone_number_list:
        print("\nSorry.This User Is Alredy Registered.")
    else:
        phone_number_list.append(phone_number) 
        print("\nRegistration Success. ") 
        print("\nInstructions will Be send shortly to continue.")  

if display_this=="1":
    print("\nEnter Your PIN:\n")
    pin=int(input("\n\n"))
    print("\nWelcome To Hustler Fund, Please Select:")
    print("\n".join(hustler_fund))
    hustler_sel=input("\nWelcome to Hustler Fund.\n")
    if hustler_sel=="1":
        print("\n".join(personal_loan))
        loan_sel=input("\nHustler Fund Loan.\n")
        if loan_sel=="1":
            print("\n".join(loan_sel_opts))

            #loan acquirement
            loan_acq=input("\nPlease Select to continue:\n")
            if loan_acq=="1":
                id_no=input("\nEnter your ID number to proceed\n")
                #call the id function
                store_id_number()
                #continue
                print(f"\nVisit {url} for more info.")
                cont=int(input("\nDo You Want To Continue?\n"))
                if cont==1:
                    webbrowser.open(url)
                else:
                    sys.exit()    

            elif loan_acq=="2":
                print("\nDo You Want To Pay Your Hustler Fund Loan?\n")

                #confirm payment
                conf=["1.Yes","2.NO"]   
                print("\n".join(conf)) 

                conf_input=input("\n")

                if conf_input=="1":
                    pay=int(input("\nEnter Your Pin To Complete this Transaction.\n"))
                    if pay==pin:
                        print("\nTransaction Success.\n")
                    else:
                        print("\nWrong PIN.Try Again Later.\nThanks for using Hustler Fund.\n")
                elif conf_input=="2":
                    sys.exit()            

              

        elif loan_sel=="2":
            print("\nSelect Account.\n") 
            print("\n".join(savings_acc))
            savings_acc_sel=input("\n")
            send_instructions=["1.Check Balance", "2.Mini Statement"]
            if savings_acc_sel=="1":
                print("\n".join(send_instructions))
                send_instructions_sel=input("\n")
                if send_instructions_sel=="1":
                    print("\nEnter Your PIN To Authorize.\n")
                    #enter pin
                    pin_conf=int(input("\n"))
                    if pin_conf==user_pin:
                        
                        webbrowser.open(url)
                    else:
                        print("\nConnection or Invalid PIN.Try Again Later.")  
                else:
                    print("\nComing Soon.") 
            elif savings_acc_sel=="2":
                short_term_send_instructions=["1.Check Balance","2.Deposit","3.Withdraw Funds","4.Transfer To Long Term Savings","5.Mini Statement"] 
                print("\n".join(short_term_send_instructions)) 
                #user input--either 
                short_term_input=input("\nSend Instructions\n")  

                #short term cont
                if short_term_input=="1":
                    print("\nEnter Your PIN To Continue.")  
                    #user pin confirmation
                    pin_conf=int(input("\n")) 

                    if pin_conf==user_pin:
                        print("\nTransaction Success. Kindly Wait for redirection.\n")
                    else:
                        print("\nWrong PIN or Timeout......")
                        sys.exit()  
                elif short_term_input=="2": 
                    amount=int(input("\nEnter the amount to deposit into your short term savings.\n"))


        elif loan_sel=="3":
            print("\n".join(about_hustler))

            abt_hustler_sel=input("\n")
            if abt_hustler_sel=="1":
                print("\nA digital financial inclusion initiative to improve financial access to responsible finance for \npersonal , micro, small, and medium-sized enterprises(MSMEs) in Kenya.")
            else:
                print("\nSyntax Error!")  
    elif hustler_sel=="2":
        print("\nSelect Registration Body\n")
        print("\n".join(hustler_groups))
        body_reg_sel=input("\n")
        if body_reg_sel=="1":
            print("\nBy giving this information,you are confirming that you are a group chair:\nEnter Your Group Registration Number\n")
            reg_no_inp=int(input("\n"))
        elif body_reg_sel=="2":
            print("\nSelect Your Role in the group\n")
            group_roles=["1.Chairperson","2.Treasurer","3.Secretary","# Home","* Back"]  
            print("\n".join(group_roles)) 
            group_role_inp=input("\n") 
            if group_role_inp=="1":
                print("\nSend Instructions\n\n")  
                store_group_names()
            elif group_role_inp=="2":
                print("\nSend Instructions\n\n")
                store_group_names()
            elif group_role_inp=="3":
                print("\nSend Instructions\n\n") 
                store_group_names()
            elif group_role_inp=="#":
                print("\n".join(hustler_fund))  
            elif group_role_inp=="*":
                print("\n".join(hustler_groups))  
            else:
                sys.exit()  
    elif hustler_sel=="3":
        print("Site Under Mantainence.Coming soon.")
else:
    print("Syntax Error!")  