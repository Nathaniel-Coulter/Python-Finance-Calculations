def calculate_future_value(pv, r, n, t):
    """
    Calculates FV
    """
    return pv * (1 + r/n)**(n*t)

# Ex
present_value = 500.0
annual_rate = 0.08
periods = 15
time = 10

future_value = calculate_future_value(present_value, annual_rate, periods, time)
print(f"The future value is: ${future_value:.2f}")