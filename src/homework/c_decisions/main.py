import decisions

options = float(input("Enter options: "))
total = float(input("Enter total: "))

result = decisions.get_options_ratio(options, total)

Rating = decisions.get_faculty_rating(result)

print ("Rating: ", Rating)