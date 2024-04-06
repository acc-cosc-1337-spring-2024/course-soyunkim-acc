def get_students_who_took_prog1_and_prog2(prog1, prog2):
    prog1 = set(prog1)
    prog2 = set(prog2)
    return prog1.intersection(prog2)

def get_students_who_took_prog1_or_prog2(prog1, prog2):
    prog1 = set(prog1)
    prog2 = set(prog2)
    return prog2.union(prog1)

def get_students_who_took_prog1_not_prog2(prog1, prog2):
    prog1 = set(prog1)
    prog2 = set(prog2)    
    return prog1.difference(prog2)

def get_students_who_took_prog2_not_prog1(prog1, prog2):
    prog1 = set(prog1)
    prog2 = set(prog2)    
    return prog2.difference(prog1)
