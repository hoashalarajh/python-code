'''
This is an algorithm for determining the cost of electricity for a domestic customer
Inputs are : Present date, Last meter reading date and number of units for the period
Output : The electricity cost for the period in rupees

'''

from datetime import date
anotherEntry = 1

# Welcome message
print ('\n======================================================================================================================================================================================\n')
print ('\n=================================================================== THIS IS ELECTRICTY BILL CALCULATOR - NEW VERSION =================================================================\n')
print ('\n======================================================================================================================================================================================\n')
while anotherEntry != 0 :

    # getting present date
    while True:
        try:
            presentDate = input("\nEnter the present date in the format of [DD/MM/YYYY] format.....  ")
            day_p,month_p,year_p = presentDate.split('/')
            day_p = int(day_p)
            month_p = int(month_p)
            year_p = int(year_p)
            presentDate = date(year_p, month_p, day_p)
            break
        except ValueError:
            print ('\nEntered Date is INVALID!!!!!!!!\nPlease Enter the date ONLY AS IN THE MENTIONED FORMAT.........\n')
    
    # getting last meter reading date
    while True:
        try:
            lastDate = input("\nEnter the last meter reading date in [DD//MM/YYYY] format.......  ")
            day_l,month_l,year_l = lastDate.split('/')
            day_l = int(day_l)
            month_l = int(month_l)
            year_l = int(year_l)
            lastDate = date(year_l, month_l, day_l)
            break
        except ValueError:
            print ('\nEntered Date is INVALID!!!!!!!!\nPlease Enter the date ONLY AS IN THE MENTIONED FORMAT.........\n')

    # getting the difference between two dates
    numberOfDays = presentDate - lastDate
    numberOfDays = numberOfDays.days

    # computing Domestic Increasing Block Tariff
    units = int(input("\nEnter the number units for the period : "))

    if (units > 0) and (numberOfDays > 0):
        # determing fixed charge for the block
        fixedCharge = 0
        if units > (180*numberOfDays/30):
            fixedCharge = 1500
        elif units > (120*numberOfDays/30):
            fixedCharge = 960
        elif units > (90*numberOfDays/30):
            fixedCharge = 960
        elif units > (60*numberOfDays/30):
            fixedCharge = 360
        elif units > (30*numberOfDays/30):
            fixedCharge = 240
        else:
            fixedCharge = 120
            
        # determining kWh charge
        kWhCharge = 0
        if units > (180*numberOfDays/30):
            kWhCharge = (units - (180*numberOfDays/30))*75 + ((180*numberOfDays/30) - (120*numberOfDays/30))*50 + ((120*numberOfDays/30) - (90*numberOfDays/30))*50 + ((90*numberOfDays/30) - (60*numberOfDays/30))*16 + ((60*numberOfDays/30) - (0*numberOfDays/30))*16
        elif units > (120*numberOfDays/30):
            kWhCharge = (units - (120*numberOfDays/30))*50 +  ((120*numberOfDays/30) - (90*numberOfDays/30))*50 + ((90*numberOfDays/30) - (60*numberOfDays/30))*16 + ((60*numberOfDays/30) - (0*numberOfDays/30))*16
        elif units > (90*numberOfDays/30):
            kWhCharge = (units - (90*numberOfDays/30))*50 + ((90*numberOfDays/30) - (60*numberOfDays/30))*16 + ((60*numberOfDays/30) - (0*numberOfDays/30))*16
        elif units > (60*numberOfDays/30):
            kWhCharge = (units - (60*numberOfDays/30))*16 + ((60*numberOfDays/30) - (0*numberOfDays/30))*16
        elif units > (30*numberOfDays/30):
            kWhCharge = (units - (30*numberOfDays/30))*10 + ((30*numberOfDays/30) - (0*numberOfDays/30))*8
        else:
            kWhCharge = units * 8 

        # summing up fixed charges and kWh charges for determining final cost
        finalCost = fixedCharge + kWhCharge

        # Displaying the final cost for electrcity bill
        print ("\n=====================================================================================================================================")
        print ("=====================================================================================================================================") 
        print (f"\n\n\t\t\t\tThe number of days considered for billing is : {numberOfDays} Days\n")
        print (f"\t\t\t\tThe units of electricty consumption for the period is : {units} Units\n")
        print ("\t\t\t\tThe fixed charge is : Rs.{:.2f}\n".format(fixedCharge))
        print ("\t\t\t\tThe kWh Charge is : Rs.{:.2f}\n".format(kWhCharge))
        print ("\t\t\t\tThe total cost of the electricity is : Rs.{:.2f}\n".format(finalCost))
        print ("=====================================================================================================================================")
        print ("=====================================================================================================================================")
    elif (units <= 0) and (numberOfDays > 0):
        print ("\n=====================================================================================================================================")
        print ("=====================================================================================================================================")
        print ('\n\t\t################################   AN ERROR FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!  ###############################\n')
        print ("\t\t################################ Please check the number of units you entered ##################################\n")
        print ("\t\t##################### Please also make sure that the number of units you are entering is only positive #######\n")
        print ("=====================================================================================================================================")
        print ("=====================================================================================================================================")
    elif (units > 0) and (numberOfDays <= 0):
        print ("\n=====================================================================================================================================")
        print ("=====================================================================================================================================")
        print ('\n\t\t################################   AN ERROR FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!  ###############################\n')
        print ("\t\t################################ Please check the date entry you entered #######################################\n")
        print ("\t\t###### Please make sure that you are not interchanging present date with lastmeter reading date ################\n")
        print ("=====================================================================================================================================")
        print ("=====================================================================================================================================")
    else:
        print ("\n=====================================================================================================================================")
        print ("=====================================================================================================================================")
        print ('\n\t\t################################   AN ERROR FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!  ###############################\n')
        print ("\t\t########################## Please check the date entry and the number of units you entered #####################\n")
        print ("\t\t###### Please make sure that you are not interchanging present date with lastmeter reading date ################\n")
        print ("\t\t############# Please make sure that the number of units you are entering is only positive ######################\n")
        print ("=====================================================================================================================================")
        print ("=====================================================================================================================================")
    
    anotherEntry = int(input("\nDo you want to continue with another Entry ????? 1 [Yes] / 0 [No] "))
    print ('\n')
