def bank_min():
    capital=int(input("Enter capital: "))
    
    turn_no= int(input("Enter turn_no: "))
    bank_min=((capital*(2**turn_no))-capital)
    print(bank_min)
bank_min()
