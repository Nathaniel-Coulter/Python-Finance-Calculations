def calculate_present_value(fv, r, n):
    """
    Calculates (PV)

    """
    return fv / (1 + r)**n


future_value = 1500.0
annual_rate = 0.05
periods = 10

present_value = calculate_present_value(future_value, annual_rate, periods)
print(f"The present value is: ${present_value:.2f}")