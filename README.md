Here’s a professional README.md draft for your project that you can use on GitHub:


---

Loan Calculator

A simple command-line tool written in Python for calculating loan repayments.
It supports annuity and differentiated payment methods and helps determine loan principal, monthly payments, number of periods, and overpayment.


---

Features

Supports two types of payment calculation:

Annuity payments (--type=annuity)

Differentiated payments (--type=diff)


Calculates:

Loan principal

Monthly payment

Number of months/years to repay

Overpayment


Input validation for incorrect or missing parameters



---

Installation

Clone this repository and navigate into it:

git clone https://github.com/lekslen/Python-Loan-Calculator.git
cd Python-Loan-Calculator

No additional dependencies are required beyond the Python standard library.


---

Usage

Run the script from the command line with arguments:

python LoanCalculator.py --type <payment_type> --principal <amount> --periods <months> --interest <rate> [--payment <amount>]

Arguments

--type : Type of payment (annuity or diff)

--principal : Loan principal (the amount borrowed)

--periods : Number of months to repay the loan

--interest : Annual interest rate (as a percentage, without %)

--payment : Monthly payment amount (optional, depending on calculation type)



---

Examples

1. Calculate number of months to repay (Annuity)

python LoanCalculator.py --type=annuity --principal=1000000 --payment=15000 --interest=10

Output:

It will take 6 years and 7 months to repay this loan!
Overpayment = 185000

2. Calculate differentiated payments

python LoanCalculator.py --type=diff --principal=500000 --periods=8 --interest=7.8

Output:

Month 1: payment is 65750
Month 2: payment is 65344
...
Month 8: payment is 62711
Overpayment = 14621

3. Calculate monthly payment (Annuity)

python LoanCalculator.py --type=annuity --principal=1000000 --periods=60 --interest=10

Output:

Your monthly payment = 21248
Overpayment = 274880

4. Calculate loan principal

python LoanCalculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6

Output:

Your loan principal = 800018!
Overpayment = 246622


---

Error Handling

The program prints:

Incorrect parameters

if the input arguments are invalid, missing, or inconsistent.


---

License

This project is licensed under the MIT License. Feel free to use and modify it.


---

Do you want me to also prepare a shorter, polished version (with just intro + usage) for quick GitHub overview, or should I keep this detailed one?

