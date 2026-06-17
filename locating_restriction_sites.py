# This returns the starting position and length of every reverse palindrome of length 4 to 12 in the DNA sequence.

from Bio import SeqIO

sequence = ""

for record in SeqIO.parse("input.fasta", "fasta"):
    sequence = str(record.seq)

fragments = []

for i in range(len(sequence)):

    for j in range(i + 1, len(sequence) + 1):
        fragment = sequence[i:j]

        if 4 <= len(fragment) <= 12:
            fragments.append((fragment, i))

table = str.maketrans("ATCG", "TAGC")

for fragment_info in fragments:
    frag = fragment_info[0]
    position = fragment_info[1]

    reverse = frag[-1::-1]
    reverse_complement = reverse.translate(table)

    if reverse_complement == frag:
        print(position + 1, len(frag))