import math
import argparse

parser = argparse.ArgumentParser(description="Run with arguments through command line")
parser.add_argument("--type", help="Indicating the type of payment: 'annuity' or 'diff' (differentiated)", nargs="?", default=None)
parser.add_argument("--payment", help="Monthly payment amount", nargs="?", default=None)
parser.add_argument("--principal", type=int, help="Amount of money borrowed", nargs="?", default=None)
parser.add_argument("--periods", help="The number of months to repay the loan", nargs="?", default=None)
parser.add_argument("--interest", help="Interest without percent sign", nargs="?", default=None)

args = parser.parse_args()

#print(vars(args))
#For differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided
data_dictionary = vars(args)

count_none = sum(1 for k, v in data_dictionary.items() if v is None)
#print("Количество ключей со значением None:", count_none)
if count_none > 1:
    print("Incorrect parameters")
    exit()

#Chacking if all needed parameters are passed
if args.type is None or (args.type != "annuity" and args.type != "diff") :
    print("Incorrect parameters")
    exit()
    
#For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid
if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()

#Our loan calculator can't calculate the interest, so it must always be provided
if args.interest is None:
    print("Incorrect parameters")
    exit()

# Converting string values in arguments to integers
if args.payment is not None:
    args.payment = float(args.payment)
if args.principal is not None:
    args.principal = float(args.principal)
if args.periods is not None:
    args.periods = float(args.periods)
if args.interest is not None:
    args.interest = float(args.interest)
    monthly_interest = args.interest / 12 / 100

#Negative values should not be provided
if (args.payment is not None and args.payment <=0) or (args.principal is not None and args.principal <= 0) or (args.periods is not None and args.periods <= 0) or (args.interest is not None and args.interest <=0):
    print("Incorrect parameters")
    exit()

if args.periods is None and args.type == "annuity":
    # Calculating how many months and years to repay
    args.periods = math.ceil(math.log(args.payment / (args.payment - monthly_interest * args.principal)) / math.log(1 + monthly_interest))
    
    print(f"It will take {args.periods // 12} years and {args.periods % 12} months to repay this loan!")
    print(f"Overpayment = {int((args.payment * args.periods) - args.principal)}")
elif args.type == "diff" and args.payment is None:
    #calculating differentiated payments
    payments = []
    for i in range(1, int(args.periods) + 1):
        args.payment = math.ceil((args.principal / args.periods) + monthly_interest * (args.principal - ((args.principal * (i - 1)) / args.periods)))
        print(f"Month {i}: payment is {args.payment}")
        payments.append(args.payment)
    print(f"Overpayment = {int(sum(payments) - args.principal)}")
elif args.type == "annuity" and args.payment is None:
    # Calculating how much is monthly payment
    args.payment = math.ceil(args.principal * (monthly_interest * pow(1 + monthly_interest, args.periods) / (pow(1 + monthly_interest, args.periods) - 1)))
    print(f"Your monthly payment = {args.payment}")
    print(f"Overpayment = {int((args.payment * args.periods) - args.principal)}")
elif args.principal is None and args.type == "annuity":
    # Calculating the sum was borrowed
    args.principal = int(args.payment / ((monthly_interest * pow(1 + monthly_interest, args.periods)) / (pow(1 + monthly_interest, args.periods) - 1)))
    print(f"Your loan principal = {args.principal}!")
    print(f"Overpayment = {int((args.payment * args.periods) - args.principal)}")

#if args.payment is None and args.principal is None and args.periods is None and args.interest is None:
#    print("Enter the loan principal:")
#    principal = int(input())

#    print()
#    print("What do you want to calculate?")
#    print('type "m" for number of monthly payments,')
#    print('type "p" for the monthly payment:')
#    choice = input()
#    print()

#    if choice == 'm':
#        print("Enter the monthly payment:")
#        m_payment = int(input())
#        repay_months = math.ceil(principal/m_payment)
#        print()
#        print(f"It will take {repay_months} months to repay the loan")
#    else:
#        print()
#        print("Enter the number of months:")
#        months = int(input())
#        m_payment = principal / months
#    
#        if m_payment % 1 != 0:
#            #print("Есть дробная часть")
#            m_payment = math.ceil(m_payment)
#            print(f"Your monthly payment = {m_payment} and the last payment = {principal-(months-1)*m_payment}.")
#        else:
#        #print("Целое число")
#            print(f"Your monthly payment = {int(m_payment)}")