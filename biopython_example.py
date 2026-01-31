from Bio.Seq import Seq

dna = Seq("ATCGGCTA")
print(dna.reverse_complement())  # TAGCCGAT
