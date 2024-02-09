#Formula for The Future Value of an Anuunity Due (below)
#P = PMT × ((1 + r)^n - 1) / r

def future_value_of_annuity_due(pmt, r, n):
    """
    Remember this is the future value of an annuity due. 
    For an ordinary annuity remove the *(1+r) 
    """
    # FVAD...
    p = pmt * ((1 + r)**n - 1) / r
    return p

# Annual payment PMT = 100
#interest rate r = 5.0% 
#number of periods n = 5

pmt = 100
r = 0.05
n = 5

p = future_value_of_annuity_due(pmt, r, n)

print(f"The future value of the annuity is: {p:.4f}")

#The future value of the annuity is: 552.5631
