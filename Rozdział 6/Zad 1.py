def ask_number(question = "?", low = 0, high = 8, step = 1):
    """Poproś o podanie liczby z odpowiedniego zakresu."""    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
