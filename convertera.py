def cm_to_inches(length_cm):
    if length_cm < 0:
        return -1 * cm_to_inches(-length_cm)
    inches = length_cm / 2.54
    return round(inches, 2)
