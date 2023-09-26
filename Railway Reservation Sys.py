#Aim: To create a Railway Reservation System.
print("Aim: To create a Railway Reservation System.")

print("---------------------------------------------------------------------------------------")
print("                             WELCOME TO RAILWAY RESERVATION PORTAL                     ")
print("---------------------------------------------------------------------------------------")
print("                                       DASHBOARD                                       ")
print("---------------------------------------------------------------------------------------")
print("1.Book Tickets")
print("2.See Available Trains")
print("3.Cancel Tickets")
print("4.Exit")
print("---------------------------------------------------------------------------------------")

x = int(input("Please enter your choice: "))

if x==1:
        print("\nPlease create your account to continue.....")
        name = input("Please enter your Name: ")
        age  = int(input("Please enter your Age: "))
        gen  = input("Please enter your Gender: ")
        mail = input("Please enter your Email: ")
        pword = input("Please enter your Password: ")
        cnum = int(input("Please enter your phone number: "))
        pnr  = str(cnum)+str(age)
        print("ACCOUNT CREATED SUCESSFULLY")
        print("Your username is:",name)
        print("Your password is:",pword)
        print("Your PNR Number is:",pnr)
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                     AVAILABLE TRAINS                                                               ")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("  TrainNumber    From        To         Departure   Arrival     Station    Duration   Bookings    Days           StaffVaccination   ")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("    1          NAGPUR       MUMBAI       04:00 pm   05:45 am    NGP-CSMT   13h50m      OPEN     M/TU/W/TH/F      Fully Vaccinated   ")
        print("    2          DELHI        CHENNAI      12:40 pm   03:05 am    AVS-MS     14h25m      OPEN     M/TU/W/SA/SU     Fully Vaccinated   ")
        print("    3          KOLKATA      PATNA        11:55 pm   09:55 am    HWH-PNBE   10h05m     CLOSED    M/TU/TH/F/S/S    Not   Vaccinated   ")
        print("    4          LUCKNOW      AGRA         10:30 am   05:05 pm    ASH-AGC    06h35m     CLOSED    TU/W/TH/F/S      Not   Vaccinated   ")
        print("    5          BANGALORE    MYSORE       08:30 pm   11:00 pm    SBC-MYS    02h30m      OPEN     M/TU/W/SA/SU     Fully Vaccinated   ")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        ask1 = int(input("Please enter the train number you wish to book: "))
        if ask1 == 1 or 2 or 5:
            print("-------------------------------------------------------------------------------------------")
            print(   "AVAILABLE CLASSES:             PRICE                         SEATS AVAILABLE            ")
            print("-------------------------------------------------------------------------------------------")
            print(   "1.AC FIRST CLASS          RS.1000 per ticket          11c/11e/11f/11g/11h/11n/11k/11t   ")
            print(   "2.AC SECOND CLASS         RS.800  per ticket          12a/12b/12k/12r/12d/12p/12k/12t   ")
            print(   "3.AC THIRD CLASS          RS.350  per ticket          13m/13e/13w/13r/13h/13p/12g/13f   ")
            print(   "4.SLEEPER CLASS           RS.150  per ticekt          14q/14h/14e/14m/14s/14t/14d/14k   ")
            print("-------------------------------------------------------------------------------------------")
            cs = int(input("Please enter your class: "))
            if cs==1:
                cs_1="AC FIRST CLASS"
            if cs==2:
                cs_1="AC SECOND CLASS"
            if cs==3:
                cs_1="AC THIRD CLASS"
            if cs==4:
                cs_1="SLEEPER CLASS"
            if cs==1:
                tb_1=1000
            if cs==2:
                tb_1=800
            if cs==3:
                tb_1=350
            if cs==4:
                tb_1=150
            sc = input("Please select your seat: ")
            day = input("Please enter your day of travel: ")
            ask2 = input("Would you like to avail the food services offered by the train (Y/N): ")
            if ask2=="Y"or "y":
                print("      MENU             PRICE   ")
                print("  1.NORTH INDIAN       RS.100  ")
                print("  2.SOUTH INDIAN       RS.100  ")
                print("  3.CHINESE            RS.100  ")
                fs = int(input("Please enter your preffered menu: "))
                if fs==1:
                    tb_2=100
                if fs==2:
                    tb_2=100
                if fs==3:
                    tb_2=100
                tb = tb_1+tb_2
                print("Your total bill is: RS.",tb)
                print("PAYMENT DETAILS")
                ask3 = int(input("Please enter your card number: "))
                ask4 = input("Please enter card holder name: ")
                import random
                otp = random.randint(1000,9999)
                print("Your OTP is: ",otp)
                ask5 = int(input("Please enter your OTP: "))
                if ask5==otp:
                    print("PROCESSING TRANSACTION...............")
                    import random
                    tid = random.randint(100000,999900)
                    print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                    print("YOUR TICKET HAS BEEN BOOKED SUCESFULLY.     TRANSACTION ID:",tid)
                    print("THANK YOU FOR USING OUR PORTRAL.")
                else:
                    print("WRONG OTP!!!!!!")
                    ask5 = int(input("Please enter your OTP again: "))
                    if ask5==otp:
                        print("PROCESSING TRANSACTION...............")
                        import random
                        tid = random.randint(100000,999900)
                        print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                        print("YOUR TICKET HAS BEEN BOOKED SUCESSFULLY.     TRANSACTION ID:",tid)
                        print("THANK YOU FOR USING OUR PORTRAL.")
            if ask2=="N":
                tb = tb_1
                print("Your total bill is: RS.",tb)
                print("PAYMENT DETAILS")
                ask3 = int(input("Please enter your card number: "))
                ask4 = input("Please enter card holder name: ")
                import random
                otp = random.randint(1000,9999)
                print("Your OTP is: ",otp)
                ask5 = int(input("Please enter your OTP: "))
                if ask5==otp:
                     print("PROCESSING TRANSACTION...............")
                     import random
                     tid = random.randint(100000,999900)
                     print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                     print("YOUR TICKET HAS BEEN BOOKED SUCESSFULLY.     TRANSACTION ID:",tid)
                     print("THANK YOU FOR USING OUR PORTRAL.")
                else:
                    print("WRONG OTP!!!!!!")
                    ask5 = int(input("Please enter your OTP again: "))
                    if ask5==otp:
                        print("PROCESSING TRANSACTION...............")
                        import random
                        tid = random.randint(100000,999900)
                        print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                        print("YOUR TICKET HAS BEEN BOOKED SUCESSFULLY.     TRANSACTION ID:",tid)
                        print("THANK YOU FOR USING OUR PORTRAL.")
            if ask1==1:
                dc="NAGPUR"
                ac="MUMBAI"
                dt="04:00 pm"
                at="05:45 am "
                st="NGP-CSMT"
                du="13h50m"
                sv="Fully Vaccinated"
                print("*******************-----YOUR TICKET-----********************")
                print("Name:",name)
                print("Age:",age)
                print("PNR Number:",pnr)
                print("Transaction ID:",tid)
                print("Train Number:",ask1)
                print("Class Booked:",cs_1)
                print("Seat Booked",sc)
                print("Day of Travel: Coming",day)
                print("Departure City:",dc)
                print("Arrival   City:",ac)
                print("Departure Time:",dt)
                print("Arrival   Time:",at)
                print("Station:",st)
                print("Staff Vaccination:",sv)
                print("Thank You for choosing us!!")
                print("********************---------------------********************")

            if ask1==2:
                dc="DELHI"
                ac="CHENNAI"
                dt="12:40 pm"
                at="03:05 am "
                st="AVS-MS"
                du="14h25m"
                sv="Fully Vaccinated"
                print("*******************-----YOUR TICKET-----********************")
                print("Name:",name)
                print("Age:",age)
                print("PNR Number:",pnr)
                print("Transaction ID:",tid)
                print("Train Number:",ask1)
                print("Class Booked:",cs_1)
                print("Seat Booked",sc)
                print("Day of Travel: Coming",day)
                print("Departure City:",dc)
                print("Arrival   City:",ac)
                print("Departure Time:",dt)
                print("Arrival   Time:",at)
                print("Station:",st)
                print("Staff Vaccination:",sv)
                print("Thank You for choosing us!!")
                print("********************---------------------********************")

            if ask1==5:
                dc="BANGALORE"
                ac="MYSORE"
                dt="08:30 pm"
                at="11:00 pm "
                st="SBC-MYS"
                du="2h30m"
                sv="Fully Vaccinated"
                print("*******************-----YOUR TICKET-----********************")
                print("Name:",name)
                print("Age:",age)
                print("PNR Number:",pnr)
                print("Transaction ID:",tid)
                print("Train Number:",ask1)
                print("Class Booked:",cs_1)
                print("Seat Booked",sc)
                print("Day of Travel: Coming",day)
                print("Departure City:",dc)
                print("Arrival   City:",ac)
                print("Departure Time:",dt)
                print("Arrival   Time:",at)
                print("Station:",st)
                print("Staff Vaccination:",sv)
                print("Thank You for choosing us!!")
                print("********************---------------------********************")
        ask7 = input("\nWould you like to cancel you ticekts(Y/N): ")
        if ask7=="Y":
            ask8 = input("Please enter you PNR Number: ")
            if ask8==pnr:
                 print("YOUR TICKET HAS BEEN CANCELLED SUCCESFULLY.")
                 print("YOU WILL RECEIVE 50% OF YOUR PAID AMOUNT ACCORDING TO THE REFUND POLICY IN 2-3 DAYS.")
                 print("THANK YOU FOR CHOOSING US.")
            if ask8!=pnr:
                 print("WRONG PNR NUMBER!!!!")
                 ask8 = input("Please enter you PNR Number again to cancel the tickets: ")
                 if ask8==pnr:
                     print("YOUR TICKET HAS BEEN CANCELLED SUCCESFULLY.")
                     print("YOU WILL RECEIVE 50% OF YOUR PAID AMOUNT ACCORDING TO THE REFUND POLICY IN 2-3 DAYS.")
                     print("THANK YOU FOR CHOOSING US.")
        if ask7=="N":
            print("OK....")
            print("THANK YOU FOR CHOOSING US FOR BOOKING THE TICKETS.")
            print("HAPP JOURNEY......LOOKING FORWAARD TO SEEING YOU AGAIN.")
             
             
if x==2:
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                     AVAILABLE TRAINS                                                               ")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("  TrainNumber    From        To         Departure   Arrival     Station    Duration   Bookings    Days           StaffVaccination   ")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("    1          NAGPUR       MUMBAI       04:00 pm   05:45 am    NGP-CSMT   13h50m      OPEN     M/TU/W/TH/F      Fully Vaccinated   ")
    print("    2          DELHI        CHENNAI      12:40 pm   03:05 am    AVS-MS     14h25m      OPEN     M/TU/W/SA/SU     Fully Vaccinated   ")
    print("    3          KOLKATA      PATNA        11:55 pm   09:55 am    HWH-PNBE   10h05m     CLOSED    M/TU/TH/F/S/S    Not   Vaccinated   ")
    print("    4          LUCKNOW      AGRA         10:30 am   05:05 pm    ASH-AGC    06h35m     CLOSED    TU/W/TH/F/S      Not   Vaccinated   ")
    print("    5          BANGALORE    MYSORE       08:30 pm   11:00 pm    SBC-MYS    02h30m      OPEN     M/TU/W/SA/SU     Fully Vaccinated   ")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    ask6 = input("Would you like to continue(Y/N): ")
    if ask6=="Y":
        print("\nPlease create your account to continue.....")
        name = input("Please enter your Name: ")
        age  = int(input("Please enter your Age: "))
        gen  = input("Please enter your Gender: ")
        mail = input("Please enter your Email: ")
        pword = input("Please enter your Password: ")
        cnum = int(input("Please enter your phone number: "))
        pnr  = str(cnum)+str(age)
        print("ACCOUNT CREATED SUCESSFULLY")
        print("Your username is:",name)
        print("Your password is:",pword)
        print("Your PNR Number is:",pnr)
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                     AVAILABLE TRAINS                                                               ")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("  TrainNumber    From        To         Departure   Arrival     Station    Duration   Bookings    Days           StaffVaccination   ")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("    1          NAGPUR       MUMBAI       04:00 pm   05:45 am    NGP-CSMT   13h50m      OPEN     M/TU/W/TH/F      Fully Vaccinated   ")
        print("    2          DELHI        CHENNAI      12:40 pm   03:05 am    AVS-MS     14h25m      OPEN     M/TU/W/SA/SU     Fully Vaccinated   ")
        print("    3          KOLKATA      PATNA        11:55 pm   09:55 am    HWH-PNBE   10h05m     CLOSED    M/TU/TH/F/S/S    Not   Vaccinated   ")
        print("    4          LUCKNOW      AGRA         10:30 am   05:05 pm    ASH-AGC    06h35m     CLOSED    TU/W/TH/F/S      Not   Vaccinated   ")
        print("    5          BANGALORE    MYSORE       08:30 pm   11:00 pm    SBC-MYS    02h30m      OPEN     M/TU/W/SA/SU     Fully Vaccinated   ")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        ask1 = int(input("Please enter the train number you wish to book: "))
        if ask1 == 1 or 2 or 5:
            print("-------------------------------------------------------------------------------------------")
            print(   "AVAILABLE CLASSES:             PRICE                         SEATS AVAILABLE            ")
            print("-------------------------------------------------------------------------------------------")
            print(   "1.AC FIRST CLASS          RS.1000 per ticket          11c/11e/11f/11g/11h/11n/11k/11t   ")
            print(   "2.AC SECOND CLASS         RS.800  per ticket          12a/12b/12k/12r/12d/12p/12k/12t   ")
            print(   "3.AC THIRD CLASS          RS.350  per ticket          13m/13e/13w/13r/13h/13p/12g/13f   ")
            print(   "4.SLEEPER CLASS           RS.150  per ticekt          14q/14h/14e/14m/14s/14t/14d/14k   ")
            print("-------------------------------------------------------------------------------------------")
            cs = int(input("Please enter your class: "))
            if cs==1:
                cs_1="AC FIRST CLASS"
            if cs==2:
                cs_1="AC SECOND CLASS"
            if cs==3:
                cs_1="AC THIRD CLASS"
            if cs==4:
                cs_1="SLEEPER CLASS"
            if cs==1:
                tb_1=1000
            if cs==2:
                tb_1=800
            if cs==3:
                tb_1=350
            if cs==4:
                tb_1=150
            sc = input("Please select your seat: ")
            day = input("Please enter your day of travel: ")
            ask2 = input("Would you like to avail the food services offered by the train (Y/N): ")
            if ask2=="Y":
                print("      MENU             PRICE   ")
                print("  1.NORTH INDIAN       RS.100  ")
                print("  2.SOUTH INDIAN       RS.100  ")
                print("  3.CHINESE            RS.100  ")
                fs = int(input("Please enter your preffered menu: "))
                if fs==1:
                    tb_2=100
                if fs==2:
                    tb_2=100
                if fs==3:
                    tb_2=100
                tb = tb_1+tb_2
                print("Your total bill is: RS.",tb)
                print("PAYMENT DETAILS")
                ask3 = int(input("Please enter your card number: "))
                ask4 = input("Please enter card holder name: ")
                import random
                otp = random.randint(1000,9999)
                print("Your OTP is: ",otp)
                ask5 = int(input("Please enter your OTP: "))
                if ask5==otp:
                    print("PROCESSING TRANSACTION...............")
                    import random
                    tid = random.randint(100000,999900)
                    print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                    print("YOUR TICKET HAS BEEN BOOKED SUCESFULLY.     TRANSACTION ID:",tid)
                    print("THANK YOU FOR USING OUR PORTRAL.")
                else:
                    print("WRONG OTP!!!!!!")
                    ask5 = int(input("Please enter your OTP again: "))
                    if ask5==otp:
                        print("PROCESSING TRANSACTION...............")
                        import random
                        tid = random.randint(100000,999900)
                        print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                        print("YOUR TICKET HAS BEEN BOOKED SUCESSFULLY.     TRANSACTION ID:",tid)
                        print("THANK YOU FOR USING OUR PORTRAL.")
            if ask2=="N":
                tb = tb_1
                print("Your total bill is: RS.",tb)
                print("PAYMENT DETAILS")
                ask3 = int(input("Please enter your card number: "))
                ask4 = input("Please enter card holder name: ")
                import random
                otp = random.randint(1000,9999)
                print("Your OTP is: ",otp)
                ask5 = int(input("Please enter your OTP: "))
                if ask5==otp:
                     print("PROCESSING TRANSACTION...............")
                     import random
                     tid = random.randint(100000,999900)
                     print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                     print("YOUR TICKET HAS BEEN BOOKED SUCESSFULLY.     TRANSACTION ID:",tid)
                     print("THANK YOU FOR USING OUR PORTRAL.")
                else:
                    print("WRONG OTP!!!!!!")
                    ask5 = int(input("Please enter your OTP again: "))
                    if ask5==otp:
                        print("PROCESSING TRANSACTION...............")
                        import random
                        tid = random.randint(100000,999900)
                        print("AMOUNT HAS BEEN SUCESSFULLY DEDUCTED FROM YOUR ACCOUNT.")
                        print("YOUR TICKET HAS BEEN BOOKED SUCESSFULLY.     TRANSACTION ID:",tid)
                        print("THANK YOU FOR USING OUR PORTRAL.")
            if ask1==1:
                dc="NAGPUR"
                ac="MUMBAI"
                dt="04:00 pm"
                at="05:45 am "
                st="NGP-CSMT"
                du="13h50m"
                sv="Fully Vaccinated"
                print("*******************-----YOUR TICKET-----********************")
                print("Name:",name)
                print("Age:",age)
                print("PNR Number:",pnr)
                print("Transaction ID:",tid)
                print("Train Number:",ask1)
                print("Class Booked:",cs_1)
                print("Seat Booked",sc)
                print("Day of Travel: Coming",day)
                print("Departure City:",dc)
                print("Arrival   City:",ac)
                print("Departure Time:",dt)
                print("Arrival   Time:",at)
                print("Station:",st)
                print("Staff Vaccination:",sv)
                print("Thank You for choosing us!!")
                print("********************---------------------********************")

            if ask1==2:
                dc="DELHI"
                ac="CHENNAI"
                dt="12:40 pm"
                at="03:05 am "
                st="AVS-MS"
                du="14h25m"
                sv="Fully Vaccinated"
                print("*******************-----YOUR TICKET-----********************")
                print("Name:",name)
                print("Age:",age)
                print("PNR Number:",pnr)
                print("Transaction ID:",tid)
                print("Train Number:",ask1)
                print("Class Booked:",cs_1)
                print("Seat Booked",sc)
                print("Day of Travel: Coming",day)
                print("Departure City:",dc)
                print("Arrival   City:",ac)
                print("Departure Time:",dt)
                print("Arrival   Time:",at)
                print("Station:",st)
                print("Staff Vaccination:",sv)
                print("Thank You for choosing us!!")
                print("********************---------------------********************")

            if ask1==5:
                dc="BANGALORE"
                ac="MYSORE"
                dt="08:30 pm"
                at="11:00 pm "
                st="SBC-MYS"
                du="2h30m"
                sv="Fully Vaccinated"
                print("*******************-----YOUR TICKET-----********************")
                print("Name:",name)
                print("Age:",age)
                print("PNR Number:",pnr)
                print("Transaction ID:",tid)
                print("Train Number:",ask1)
                print("Class Booked:",cs_1)
                print("Seat Booked",sc)
                print("Day of Travel: Coming",day)
                print("Departure City:",dc)
                print("Arrival   City:",ac)
                print("Departure Time:",dt)
                print("Arrival   Time:",at)
                print("Station:",st)
                print("Staff Vaccination:",sv)
                print("Thank You for choosing us!!")
                print("********************---------------------********************")
        ask7 = input("\nWould you like to cancel you ticekts(Y/N): ")
        if ask7=="Y":
            ask8 = input("Please enter you PNR Number: ")
            if ask8==pnr:
                 print("YOUR TICKET HAS BEEN CANCELLED SUCCESFULLY.")
                 print("YOU WILL RECEIVE 50% OF YOUR PAID AMOUNT ACCORDING TO THE REFUND POLICY IN 2-3 DAYS.")
                 print("THANK YOU FOR CHOOSING US.")
            if ask8!=pnr:
                 print("WRONG PNR NUMBER!!!!")
                 ask8 = input("Please enter you PNR Number again to cancel the tickets: ")
                 if ask8==pnr:
                     print("YOUR TICKET HAS BEEN CANCELLED SUCCESFULLY.")
                     print("YOU WILL RECEIVE 50% OF YOUR PAID AMOUNT ACCORDING TO THE REFUND POLICY IN 2-3 DAYS.")
                     print("THANK YOU FOR CHOOSING US.")
        if ask7=="N":
            print("OK....")
            print("THANK YOU FOR CHOOSING US FOR BOOKING THE TICKETS.")
            print("HAPP JOURNEY......LOOKING FORWAARD TO SEEING YOU AGAIN.")
            
    if ask6=="N":
        print("Thank you for using our portal.")

if x==3:
    ask9 = input("Have you booked the tickets(Y/N): ")
    if ask9=="N":
        print("SORRY!!")
        print("THE TICKETS CANNOT BE CANCELLED AS YOU HAVE NOT BOOKED THE TICKETS.")
        print("THANK YOU.")
    if ask9=="Y":
        name = input("Please enter your Name: ")
        age  = int(input("Please enter your Age: "))
        cnum = int(input("Please enter your phone number: "))
        pnr  = str(cnum)+str(age)
        print("Your PNR Number is:",pnr)
        print("TICEKT CANCELLATION")
        ask8 = input("Please enter you PNR Number: ")
        if ask8==pnr:
            print("YOUR TICKET HAS BEEN CANCELLED SUCCESFULLY.")
            print("YOU WILL RECEIVE 50% OF YOUR PAID AMOUNT ACCORDING TO THE REFUND POLICY IN 2-3 DAYS.")
            print("THANK YOU FOR CHOOSING US.")
        if ask8!=pnr:
            print("WRONG PNR NUMBER!!!!")
            ask8 = input("Please enter you PNR Number again to cancel the ticket: ")
            if ask8==pnr:
                print("YOUR TICKET HAS BEEN CANCELLED SUCCESFULLY.")
                print("YOU WILL RECEIVE 50% OF YOUR PAID AMOUNT ACCORDING TO THE REFUND POLICY IN 2-3 DAYS.")
                print("THANK YOU FOR CHOOSING US.")

if x==4:
    print("YOU HAVE CHOSEN TO EXIT THE PORTAL.")
    print("THANK YOU FOR VISITING US.")

    
                 
                 
        
        
        
            
             

           



    
            
            
    
        
    
        
        
    
        
    
    
        
                    
                        
                            
                       
                    
                    
                
            
                
            
            
         
                
                
                       
            
            
            
            
        
        
            
        
                  
        
        
        
        
        
        
            
            

            
        
    
        

    
    
    

    
    
    
        


