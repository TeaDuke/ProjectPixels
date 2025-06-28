def get_max_number_from_array(array):
    mx = -9999999
    for value in array:
        if value > mx:
            mx = value
    return mx