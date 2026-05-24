# This returns the consensus string and profile matrix.

from Bio import SeqIO
from collections import Counter

consensus = []
columns = []
nucleotides = ["A", "C", "G", "T"]

sequences = [str(record.seq) for record in SeqIO.parse("consensus.fasta", "fasta")]

for column in zip(*sequences):
    consensus.append(Counter(column).most_common(1)[0][0])
    columns.append(dict(Counter(column)))

print("".join(consensus))

for nt in nucleotides:
    print(nt, end=": ")
    for column in columns:
        print(column.get(nt, 0),end=" ")
    print()