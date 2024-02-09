def get_options_ratio(options, total):
    ratio = options / total
    return ratio

def get_faculty_rating(ratio):
    if(ratio >= 0.9 and ratio <= 1):
        result = "Excellent"
    elif(ratio >= 0.8 and ratio < 0.9):
        result = "Very Good"
    elif(ratio >= 0.7 and ratio < 0.8):
        result = "Good"
    elif(ratio >= 0.6 and ratio < 0.7):
        result = "Needs Improvement"
    elif(ratio >= 0 and ratio < 0.6):
        result = "Unacceptable"
    else:
        result = "Invalid values for rating"

    return result