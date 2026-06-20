print("===========================")
print("   BIOINFORMATICS TOOLKIT  ")
print("===========================")
dna = ""

def dna_analyzer():
    dna = ""
    dna = input("enter a dna sequence: ").upper()


    is_valid = True
    for nucleotide in dna:
        if nucleotide not in "ATGC":
            print("invalid nucleotide:", nucleotide)
            is_valid = False
            break
        if not is_valid:
            quit()

    print("DNA Analysis Results")
    A = 0
    T = 0 
    G = 0 
    C = 0
    for nucleotide in dna:
        if nucleotide == "A":
            A = A + 1
        if nucleotide =="T":
            T = T + 1
        if nucleotide == "G":
            G = G + 1
        if nucleotide == "C":
            C = C + 1
    print("A:",A)
    print("T:",T)
    print("G:",G)
    print("C:",C)
    print("Length:", len(dna))
    gc = (G+C) / len(dna) *100
    print("GC%:",round(gc,2))
    at = (A+T) / len(dna) *100
    print("AT%:",round(at,2))
    if gc>at:
        print("DNA rich in GC")
    else:
        print("DNA rich in AT")
    if (A+T+G+C) == len(dna):
        print("valid sequence")
    else:
        print("invalid sequence")


def reverse_complement():
    dna = input("enter a dna sequence:").upper()

    complement = ""
    for nucleotide in dna:
        if nucleotide == "A":
            complement = complement + "T"
        if nucleotide == "T":
            complement = complement + "A"
        if nucleotide == "G":
            complement = complement + "C"
        if nucleotide == "C":
            complement = complement + "G"
    print("sequence complemntaire:",complement)
    reverse_complement = complement [::-1]
    print("Reverse complement:",reverse_complement)

def dna_to_rna():
    dna = input("enter a dna sequence:").upper()

    RNA = ""

    for nucleotide in dna:

        if nucleotide == "T":
            RNA = RNA + "U"

        if nucleotide == "G":
            RNA = RNA + "G"

        if nucleotide == "A":
            RNA = RNA + "A"

        if nucleotide == "C":
            RNA = RNA + "C"

    print("RNA:", RNA)

def mutation_detector():
    seq1 = input("enter first sequence:").upper()
    seq2 = input("enter second sequence:").upper()

    if len(seq1) != len(seq2):
        print("Sequences must have the same length")
        quit()
    for i in range(len(seq1)):
        if (seq1[i]) != seq2[i]:
            print("Muatation Detected")
            print("position:",i + 1)
            print(seq1[i], "->" , seq2[i])

print("1. DNA Analyzer")
print("2. Reverse Complement")
print("3. DNA to RNA")
print("4. Mutation Detector")
print("5. Exit")

choice = input("Select an option:")

if choice == "1":
    dna_analyzer()
if choice == "2":
    reverse_complement()
if choice == "3":
    dna_to_rna()
if choice == "4":
    mutation_detector()
if choice == "5":
    print("Goodbye")