#Made By Ashish And Shivang 
#PROPERTY DEALING MANAGEMNET PROJECT
def pattern(n):
    k = 2*n -2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")                                          # This whole coding will create a pattern in the execution
        k = k +1
        for j in range(0, i+1):
            print("*", end=" ")
            print("\r")

a=[]                  #List For Storing Namesdfsdaf
b=[]                  #List For Storing Adress
c=[]                  #List For Storing Mobile no.
d=[]                  #List For Storin Nationality
q=[]                  #List For Storing Adhar Card No.
e=[]                  #List For Storing Type Of Apartment In NSG
f=[]                  #List For Storing Facing Of Apartment In NSG                                                          **NSG=NEW SUNRISE GREENS**
S=[]                  #List For Storing Type Of Apartment In DC                                                              **DC=DIAMOND CITY**
T=[]                  #List For Storing Facing Of Apartment In DC
U=[]                  #List For Storing Area Of Plot In DC
V=[]                  #List For Storing Cost Of Plot In DC
Y=[]                  #List For Storing Area Of Plot In NSG
Z=[]                  #List For Storing Cost Of Plot In NSG
p=[]                  #List For Storing Choice Of User (Selecting NSG OR DC)
while(True):
    print("----------------------------------------Welcome to BIG BRO's Property Dealer Management System----------------------------------------")
    print("______________________________________________________________________________________________________________________________________\n\n")

    print("PLEASE PROVIDE THE INFORMATION BELOW CORRECTLY :-")
    inq1=str(input("Full Name      ==> \t"))
    inq2=str(input("Current Adress ==> \t"))
    inq3=int(input("Mobile No.     ==> \t"))
    inq4=str(input("Nationality    ==> \t"))
    inq5=int(input("ADHAR CARD NO. ==> \t"))
    a.append(inq1)
    b.append(inq2)
    c.append(inq3)
    d.append(inq4)
    q.append(inq5)
    #Asking user for area in which he wants to buy a land or flat or other choices
    print("\n\nPLEASE SELECT AN AREA :-")
    print("\t1.NEW SUNRISE GREENS \n\t\tOR\n\t2.DIAMOND CITY\n\n")

    choice1=int(input("ENTER PLACE CHOICE ==> \t"))
    p.append(choice1)
    print(" ")
    
    if choice1==1:
        choice1= 1
        print("\t\t Welcome to SUNRISE GREEN CORPORATION\n")    #Script for New Sunrise Greens                           

        print("\t\t Note ==> Here All The Property Is ADA Aprooved")
        print("__________________________________________________________________________________________________________")
        print("\t\tRegistry charges are not included in Total cost of apratment or plot\n\n")
        print(""" WHAT DO YOU WANT TO BUY
              1.A Apartment
               OR
              2.Empty Land  """)
        choice2=str(input(" ENTER YOUR CHOICE HERE  :-"))
        print(" ")

        if choice2=="1" :
            choice2="1"
            print("THANKS YOU ARE DONE NOW!")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")             
            print("******************************************************************************************************")
            print("""Which type of apartment do you want                                
                          1. 1 BHK
                          2. 2 BHK
                          3. 3 BHK
                          """)                                              #Script for choice of buying Apartments in NSG
                                             
            choice3=str(input("Enter your choice: "))                                            # All these special characters give attractive look to the program
            if choice3=="1" :
                print(" Cost of 1 BHK Apartment is 40.32 Lakh INR")
                print("Which Facing Do You Want")
                choice4=str(input(":-"))
                choice5=str(input("Are you sure to buy the appartment (Y/N):-"))
                e.append(choice3)
                f.append(choice4)                                   # To print Lists
                if choice5=="Y" or "y" :
                    print("All Your Info. Is Now Being Printed Below....")
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    print(q)
                    print(" 1 BHK APARTMENT ")
                    print(f)
                    print(" ")
                    print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                    print("")
                    print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                    print(" ")
                    
                     
                else :
                    print("THANKS COME BACK LATER")
                    break
                    
            elif choice3=="2":
                print(" Cost of 2 BHK Apartment is 51.55 Lakh INR")
                print("Which Facing Do You Want")
                choice4=str(input(":-"))
                e.append(choice3)
                f.append(choice4)
                choice5=str(input("Are you sure to buy the appartment (Y/N):-"))

                if choice5=="Y" or "y" :
                   print("All Your Info. Is Now Being Printed Below....")
                   print("")
                   print(a)
                   print(b)
                   print(c)
                   print(d)
                   print(q)
                   print(" 2 BHK APARTMENT ")
                   print(f)
                   print("")
                   print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                   print(" ")
                   print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                   print(" ")
                     
                else :
                    print("THANKS COME BACK LATER")
                    break
            else :
                print("Cost of 3 BHK Apartment is 72.33 Lakh INR")
                print("Which Facing Do You Want")
                choice4=str(input(":-"))
                f.append(choice4)
                choice5=str(input("Are you sure to buy the appartment (Y/N):-"))
                if choice5=="Y" or "y" :
                    print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                    print(" ")
                    print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                    print(" ")
                    print("All Your Info. Is Now Being Printed Below....")
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    print(q)
                    print("3 BHK APARTMENT ")
                    print(f)
                    print("")
                    print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                    print("")
                    print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                    print(" ")
                else :
                     print("THANKS COME BACK LATER")
                     break
                    
        elif choice2=="2" :
            print("*******************************************************************************************************************************")
            print(" ** PLOT RATES = Rs 12857 sq/yards** ")        #Script for choice of buying plot in NSG
            print(" ")
            inq5=int(input(" How much area of land do you want (sq/yards) :- "))
            cost=inq5*12857
            print("Cost of your",inq5,"sq/yards area is :",cost,"INR")
            choice5=str(input("Are you sure to buy the land (Y/N):-"))
            Y.append(inq5)
            Z.append(cost)
            if choice5=="Y" :
                print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                print(" ")
                print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                print(" ")
                print("All Your Info. Is Now Being Printed Below....")
                print(a)
                print(b)
                print(c)
                print(d)
                print(q)
                print(Y,"Sq/Yards")
                print(Z,"INR")
            else :
             print("THANKS COME BACK LATER")
             break

                                                                    #EXTRA SPACE IS GIVEN FOR EASY UNDERSTANDING OF PROGRAM SCRIPT

    elif choice1=="2":
        print("    ****** DIAMOND CITY CORPORATION PVT. LTD. ******    ")         # Script For Diamond City
        def pattern(n):
            k = 2 * n - 2
            for i in range(0, n):
                for j in range(0 , k):
                    print(end=" ")
                k = k - 1
                for j in range(0 , i + 1 ):
                    print("* ", end="")
                print("\r")
            k = n - 2
            for i in range(n , -1, -1):                                                   # This will create a pattern using asterisk in the beginning 
                for j in range(k , 0 , -1):
                    print(end=" ")
                k = k + 1
                for j in range(0 , i + 1):
                    print("* ", end="")
                print("\r")
 
        pattern(10)
        print(""" WHAT DO YOU WANT TO BUY
              1.A Apartment
               OR
              2.Empty Land  """)


        choice2=str(input(" ENTER YOUR CHOICE HERE  :-"))
        print(" ")
        if choice2=="1" :
            choice2="1"

            print("THANKS YOU ARE DONE NOW!")
            print("................................................................................................................................. ")
            print("""Which type of apartment do you want
                              1. 1 BHK
                              2. 2 BHK
                              3. 3 BHK
                              4. 4 BHK
                               """)                                      #Script for choice of buying Apartments in DC
            choice3=str(input("Enter your choice: "))

            if choice3=="1" :
                print("Cost of 1 BHK Apartment is 53.77 Lakh INR")
                print("Which Facing Do You Want")
                choice4=str(input(":-"))
                choice5=str(input("Are you sure to buy the appartment (Y/N) :-"))
                S.append(choice3)
                T.append(choice4)

                if choice5=="Y" or "y" :
                    print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                    print(" ")
                    print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                    print(" ")
                    print("All Your Info. Is Now Being Printed Below....")
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    print(q)
                    print(S)
                    print(T)
                else :
                    print("THANKS COME BACK LATER")
                    break
            elif choice3=="2" :
                print("Cost of 2 BHK Apartment is 62.8 Lakh INR")
                print("Which Facing Do You Want")
                choice4=str(input(":-"))
                S.append(choice3)
                T.append(choice4)
                choice5=str(input("Are you sure to buy the appartment (Y/N) :-"))

                if choice5=="Y" or "y" :
                    print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                    print(" ")
                    print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                    print(" ")
                    print("All Your Info. Is Now Being Printed Below....")
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    print(q)
                    print(S)
                    print(T)
                else :
                    print("THANKS COME BACK LATER")
                    break

            elif choice3=="3" :
                print("Cost of 3 BHK Apartment is 76.85 Lakh INR ")
                print("Which Facing Do You Want")
                choice4=str(input(":-"))
                S.append(choice3)
                T.append(choice4)
                choice5=str(input("Are you sure to buy the appartment (Y/N) :-"))

                if choice5=="Y" or "y" :
                    print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                    print(" ")
                    print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                    print(" ")
                    print("All Your Info. Is Now Being Printed Below....")
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    print(q)
                    print(S)
                    print(T)
                else :
                    print("THANKS COME BACK LATER")
                    break

            else :
                print("Cost of 4 BHK Apartment is 84.33 Lakh INR")
                print("Which Facing Do You Want")
                choice4=str(input(":-"))
                S.append(choice3)
                T.append(choice4)
                choice5=str(input("Are you sure to buy the land (Y/N) :-"))

                if choice5=="Y" :
                    print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                    print(" ")
                    print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                    print(" ")
                    print("All Your Info. Is Now Being Printed Below....")
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    print(q)
                    print(S)
                    print(T)
                else :
                    print("THANKS COME BACK LATER")
                    break
        elif choice2=="2":
            print("THANKS YOU ARE DONE NOW!")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")
            print(" ** PLOT RATES = Rs 18579 sq/yards** ")                                       #Script for choice of buying plot in DC
            print(" ")
            inq5=int(input(" How much area of land do you want (sq/yards) :- "))
            cost=inq5*18579
            V.append(inq5)
            U.append(cost)
            
            print("Cost of your",inq5,"sq/yards area is :",cost,"INR")
            choice5=str(input("Are you sure to buy the land (Y/N):-"))

            if choice5=="Y" :
                print("THANKS FOR MAKING A DEAL WITH US. HAVE A NICE DAY!!!")
                print(" ")
                print("PLEASE MAKE THE PAYMENT ON THE MAIN COUNTER")
                print(" ")
                print("All Your Info. Is Now Being Printed Below....")
                print(a)
                print(b)
                print(c)
                print(d)
                print(q)
                print(V,"Sq/Yards")
                print(U,"INR")
            else :
                print("THANKS COME BACK LATER")
                break


    else:
        print("Never Mind!!")
        break
            


       ######################################################################### END OF THE PROGRAM #################################################################


                                                                   #Under The Guidence OF Meetu Mam#
                                                                   ###K.V No-3 Agra Cantt###














































     


                 
