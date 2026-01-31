def reverse_complement(seq):
    table = str.maketrans("ATCG", "TAGC")
    return seq[::-1].translate(table)

print(reverse_complement("ATCGGCTA"))  # TAGCCGAT
