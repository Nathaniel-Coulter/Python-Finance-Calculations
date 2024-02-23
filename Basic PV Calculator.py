def calculate_present_value(fv, r, years):
    """
    Calculates (PV)

    """
    return fv / (1 + r/years)**(years*1)


future_value = 10000.0
annual_rate = 0.07
years = 10

present_value = calculate_present_value(future_value, annual_rate, years)
print(f"The present value is: ${present_value:.2f}")