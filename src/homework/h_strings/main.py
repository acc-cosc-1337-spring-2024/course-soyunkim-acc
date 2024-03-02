import strings

def homework_5_menu():
    print('Menu\n'
          '1 - Hamming Distance\n'
          '2 - DNA Complement\n'
          '3 - Exit')

option = 0   

while option != 3:

    homework_5_menu()
    option = int(input("Enter the number for needed function: "))

    if option == 1:

        dna1 = str(input("Enter the first DNA strand: "))
        dna2 = str(input("Enter the second DNA strand: "))

        hamming_distance = strings.get_hamming_distance(dna1, dna2)

        print("Hamming distance: ", hamming_distance)

    elif option == 2:

        dna = str(input("Enter the original DNA for the complementary strand: "))

        complementary_dna = strings.get_dna_complement(dna)

        print("Complementary DNA strand: ", complementary_dna)

    elif option == 3:
        print("Exiting...")