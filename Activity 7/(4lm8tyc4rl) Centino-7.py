class Office:
    
    def __init__(self,it,acct,hr):
    # Initialize years of service for each department
        self.it = it
        self.acct = acct
        self.hr = hr
    
    def years(self):
      # Display years of service in each department
        print("Years of service rendered in IT Department: ", self.it)
        print("Years of service rendered in ACCT Department: ", self.acct)
        print("Years of service rendered in HR: ", self.hr)
      
      
 # List to store employee office information   
listOf_IT_ACCT_HR = []


# Loop to get input for multiple employees
while True:
    
    yearsOfIT = float(input("Years of service rendered in IT Department: "))
    yearsOfACCT = float(input("Years of service rendered in ACCT Department: "))
    yearsOfHR = float(input("Years of service rendered in HR: "))
    print("\n")
  

  # Calculate and display bonus for IT department
    if yearsOfIT >=10:
    
        _itbonus = 10000
        print ("IT Department Bonus: 10000")

    elif yearsOfIT <10 and yearsOfIT> 0:
    
        _itbonus = 5000
        print ("IT Department Bonus: 5000")
   
    else:
        _itbonus = 0
        print ("NO BONUS IN IT!")
        
    print("\n")
  

   # Calculate and display bonus for Accounting department
    if yearsOfACCT >=10:
    
        _acctbonus = 12000
        print("ACCT Department Bonus: 12000")
    
    elif yearsOfACCT <10 and yearsOfACCT> 0:
    
        _acctbonus = 6000
        print("ACCT Department Bonus: 6000")
    
    else:
        _acctbonus = 0
        print("NO BONUS IN ACCT!")
        
    print("\n")

  
    # Calculate and display bonus for HR department
    if yearsOfHR >=10:
    
        _hrbonus = 15000
        print("HR Department Bonus: 15000")
    
    elif yearsOfHR <10 and yearsOfHR> 0:
    
        _hrbonus = 7500
        print("HR Department Bonus: 7500")
    
    else:
        _hrbonus = 0
        print("NO BONUS IN HR")
    
    print("\n")

   # Calculate the total bonus by summing individual department bonuses
    total_bonus = _itbonus + _acctbonus + _hrbonus

   # Display the total bonus
    print(f"THE TOTAL BONUS IS: {total_bonus}")

  # Add an empty line for better readability
    print("\n")
    

  # Ask the user if they want to create another employee record
    choice = input("CREATE ANOTHER EMPLOYEE? [Y/ANY EMPLOYEE]: ")
    if choice =="Y" or choice =="y":
        pass # Continue to the next iteration to input another employee
    
    else:
        break # Exit the loop if the user does not want to add another employee
      
    print("\n")
    
