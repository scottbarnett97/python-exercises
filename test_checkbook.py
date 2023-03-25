import os


# create ledger file if it does not exist


if not os.path.exists('ledger.txt'):
    with open('ledger.txt','w') as z:
        z.write('0')

def total_balance():
    with open('ledger.txt','r') as z:
        balance = float(z.read())
       # balance = "{:.2f}".format(balance)
    print(f'Deposit successful, new balance is: ${balance:.2f}')
    
    
def a_debit():
    value = input("How much is the debit (withdraw)?\n Format = ####.## no comma or $\n" )
    try:
        value = float(value)
        if value < 0:
            raise ValueError
    except ValueError:
        print('Please check format and try again')
        a_debit()
        return
    with open('ledger.txt','r') as z:
        balance = float(z.read())
    if value > balance:
        print('You dont have that much $$')
        return
    balance -= value
    with open('ledger.txt','w') as z:
        z.write(str(balance))
        print(f'Withdraw successful, new balance is: ${balance:.2f}')

def a_credit():
    value = input("How much is the credit (deposit)?\n Format = ####.## no comma or $\n" )
    try:
        value = float(value)
        if value < 0:
            raise ValueError
    except ValueError:
        print('Please check format and try again')
        a_credit()
        return
    with open('ledger.txt','r') as z:
        balance = float(z.read())
    balance += value
    with open('ledger.txt','w') as z:
        z.write(str(balance))
        print(f'Deposit successful, new balance is: ${balance:.2f}')
    

while True:
    choice = input("   ---  Welcome to your terminal checkbook!  --- \n\nWhat would you like to do?\n\nMake a selection using 1-4\n  1) view current balance\n  2) record a debit (withdraw)\n  3) record a credit (deposit)\n  4) exit\nYour choice (1-4)?: ")
    if choice == '1':
        total_balance() 
    elif choice == '2':
        a_debit()
    elif choice == '3':
        a_credit()
    elif choice == '4':
        print("Have a good day!")
        quit()
    else:
        print("Please try again, something is wrong with your input")