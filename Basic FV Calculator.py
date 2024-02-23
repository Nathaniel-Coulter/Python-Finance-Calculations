def calculate_future_value(pv, r, n):
    """
    Calculates FV
    """
    return pv * (1 + r)**n

# Ex
present_value = 1000.0
annual_rate = 0.05
periods = 10

future_value = calculate_future_value(present_value, annual_rate, periods)
print(f"The future value is: ${future_value:.2f}")