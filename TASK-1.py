def show_balance():
  print("**************************************")
  print(f"Your balance is {balance:.2f} rupees")
  print("**************************************")
def deposit():
  amount = float(input("   Enter an amount to be deposited:   "))
 
  if amount < 0:
      print("***************************")
      print("That is not a valid amount")
      print("****************************")
  else:
      return amount
def withdraw():
  amount = float(input("  Enter an amount to be withdrawn:  "))
 
  if amount > balance :
      print("********************")
      print("Insufficient funds")
      print("*******************")
      return 0
  elif amount < 0:
      print("*****************************")
      print("Amount must be greater than 0")
      print("*****************************")
      return 0
  else:
      return amount
 
balance = 0
is_running = True
 
 
while is_running:
     print("***************************")
     print("ATM INTERFACE USING PYTHON")
     print("1.Show Balance")
     print("2.Deposit")
     print("3.Withdraw")
     print("4.Exit")
     print("***************************")
     
     choice = input("Enter your choice (1-4): ")
     
     if choice == '1':
         show_balance()
     elif choice == '2':
         balance +=  deposit()
     elif choice == '3':
         balance -=  withdraw()
     elif choice == '4':
         is_running = False
     else:
         print("That is not valid choice")
