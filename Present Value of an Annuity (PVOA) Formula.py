def present_value_of_annuity(pmt, r, n):
    """
    PVOA (Present Value of an Annuity) Calculator...
    """
    # Formula: PVOA = PMT * [(1 – (1 / (1 + r)^n)) / r]
    pvoa = pmt * ((1 - (1 / (1 + r)**n)) / r)
    return pvoa

# Annual payment = PMT 
#interest rate = r 
#number of periods = n

pmt = 100             #|$100 in our example| 
r = 0.05              #|5.0%|
n = 5                 #|5 terms|

#PVOA
pvoa = present_value_of_annuity(pmt, r, n)

print(f"The present value of the annuity is: {pvoa:.4f}")

#The present value of the annuity is: 432.9477
