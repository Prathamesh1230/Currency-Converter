def convert_currency(amount, rate):
    try:
        return round(float(amount) * float(rate), 2)
    except ValueError:
        return None
