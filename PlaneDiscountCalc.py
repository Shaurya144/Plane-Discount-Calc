# for a "Super Summer Sales", all flights above 1000 miles have a discount applied to the normal price 
# 15% for standard class and 30% for first class. Flight travelling 1000 miles or less hae a 7.5% discount
# for standard and 10% for first class.
Statement = """
    ----------- PLEASE TYPE WHAT'S IN THE BRACKETS -----------------
    DESTINATIONS              -      PRICES(£)          -      DISTANCE(miles)
                              -  (STA)      (FST)       -
    Alesund Vigra      (AES)  -  106        -x-N/A-x-   -        700
    Shanghai Hongqiao  (SHA)  -  1000       2200        -        5700
    Bucharest Otopeni  (OTP)  -  95         190         -        1400
    TOulouse           (TLS)  -  115        210         -        690
    ----------------------------------------------------------------
"""
print(Statement)

#                     first we need to ask where they are going 
PlaneDestination = input("Hello, welcome to MyAirlines. Where would you like to go? ")
 # if they are not going to one of the destinations on the table then we can just ask them how far are they travelling and work out the discount from there
PlaneTypeClass = input("AAaannd, which type of ticket would you like: First Class or Standard Class? ")

#                      now we need to apply the discounts
if PlaneDestination == "AES" and PlaneTypeClass == "FST":
    ticketType = input("Sorry There are no First class tickets to Alesund Vigra. Would you like a Standard ticket? TYPE Y OR N")
    if ticketType == "Y":
        # as this trip is less than 1000 miles then can only give a discount of 7.5%
        ticketPrice = 106 * 0.925
        print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
    elif ticketType == "N":
        print("OK, No problem! See you soon!")
    else:
        print("Next time type either Y or N for Yes and No respectfully")
elif PlaneDestination == "AES" and PlaneTypeClass == "STA":
    ticketPrice = 106 * 0.925
    print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))

elif PlaneDestination == "SHA" and PlaneTypeClass == "FST":
    ticketPrice = 2200 * 0.7 # all flight first class above 1000 miles have a 30% discount
    print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
elif PlaneDestination == "SHA" and PlaneTypeClass == "STA":
    ticketPrice = 1000 * 0.85 # all flights standard class above 1000 miles have 15% discount
    print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))

elif PlaneDestination == "OTP" and PlaneTypeClass == "FST":
    ticketPrice = 190 * 0.7
    print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
elif PlaneDestination == "OTP" and PlaneTypeClass == "STA":
    ticketPrice = 95 * 0.85
    print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))

elif PlaneDestination == "TLS" and PlaneTypeClass == "FST":
    ticketPrice = 210 * 0.9 # first class flights less than 1000 get a dicount of 10%
    print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
elif PlaneDestination == "TLS" and PlaneTypeClass == "STA":
    ticketPrice = 115 * 0.925
    print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))


else:
    planeDistance = int(input("We could not find your flight on the board maybe you could tell us how far your flight will be traveling in miles: "))
    planeType = input("And your plane Type STA for standard and FST for first class: ")
    planeStandardPrice = int(input("What is the standard price of this ticket"))
    if planeDistance > 1000 and planeType == "FST":
        ticketPrice = planeStandardPrice * 0.7
        print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
    elif planeDistance <= 1000 and planeType == "FST":
        ticketPrice = planeStandardPrice * 0.9
        print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
    elif planeDistance > 1000 and planeType == "STA":
        ticketPrice = planeStandardPrice * 0.85
        print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
    elif planeDistance <= 1000 and planeType == "STA":
        ticketPrice = planeStandardPrice * 0.925
        print("Your ticket price after a discount is £" + str(round(ticketPrice, 2)))
    else:
        print("PLEASE TYPE IN THE CORRECT VALUES!")