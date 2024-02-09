    # Default-risk premium formula: DRPj = ijt - iTt
    # DRPj = default risk premium for security (jt)
    # ijt = the interest rate on security (jt)
    # iTt = interest rate on the Treasury security Tt

def default_risk_premium(interest_rate_security_jt, interest_rate_treasury_security_tt):
    """
    DRPj ( calculator in Python)
    """

    default_risk_premium = interest_rate_security_jt - interest_rate_treasury_security_tt
    return default_risk_premium

#For our example the inputs are...
# jt = 7.0% 
# Tt = 5.0%

interest_rate_security_jt = 0.0700
interest_rate_treasury_security_tt = 0.0500

# formula in python code
default_risk_premium = default_risk_premium(interest_rate_security_jt, interest_rate_treasury_security_tt)

print(f"The default risk premium (DRPj) for the security is: {default_risk_premium:.4f}")

#The default risk premium (DRPj) for the security is: 0.0200
