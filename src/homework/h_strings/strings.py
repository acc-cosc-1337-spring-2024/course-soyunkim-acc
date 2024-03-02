def get_hamming_distance(dna1, dna2):

    L = len(dna1)
    distance = 0

    for n in range(L):
        if dna1[n] != dna2[n]:
            distance += 1
    return distance

def get_dna_complement(dna):

    complementary_string = dna.replace("A", "t").replace("C", "g").replace("T", "a").replace("G", "c")
    complementary_string = complementary_string.upper()
    complementary_string = complementary_string[::-1]

    return complementary_string