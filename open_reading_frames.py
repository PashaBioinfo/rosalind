from Bio import SeqIO
import re

codon_table = {
    "TTT":"F","TTC":"F",
    "TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I",
    "ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S","AGT":"S","AGC":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y",
    "CAT":"H","CAC":"H",
    "CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N",
    "AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D",
    "GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C",
    "TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G",
    "TAA":"Stop","TAG":"Stop","TGA":"Stop"
}

sequence = ""
reverse_complement = ""

for record in SeqIO.parse("input.fasta", "fasta"):
    sequence = str(record.seq)
    reverse_complement = str(record.seq.reverse_complement())

proteins = set()

def find_proteins(input_sequence):

    for match in re.finditer(r'ATG', input_sequence):
        protein = ""

        for position in range(match.start(), len(input_sequence) - 2, 3):
            codon = input_sequence[position:position + 3]
            aa = codon_table[codon]

            if aa == "Stop":
                proteins.add(protein)
                break

            protein += aa

find_proteins(sequence)
find_proteins(reverse_complement)

for p in proteins:
    print(p)