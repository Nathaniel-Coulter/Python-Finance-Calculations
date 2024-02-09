#A real risk-free rate is the interest rate that would exist on a risk-free security if no inflation were expected over the holding period of a security
#(Fisher effect) Formula: i = RFR + E(IP), where [E(IP)] = the expected rate of inflation and i = the nominal interest rate rate = 
#for this example i=6.0% or (0.060) | [E(IP)]=5.5% or (0.0550)

def real_risk_free_rate(expected_rate_of_inflation, nominal_interest_rate):
    """
    The real risk-free rate (RFR) is also called the Fisher effect formula...
    """
    #i = RFR + E(IP)
    real_risk_free_rate = nominal_interest_rate - expected_rate_of_inflation
    return real_risk_free_rate

# E(IP) + (i)
expected_rate_of_inflation = 0.0550 #5.5%
nominal_interest_rate = 0.0600 # 6.0%

# Formula as python
real_risk_free_rate = real_risk_free_rate(expected_rate_of_inflation, nominal_interest_rate)

print(f"The real risk-free rate (RFR) is: {real_risk_free_rate:.4f}")

#The real risk-free rate (RFR) is: 0.0050

#[Done] exited with code=0 in 0.105 seconds