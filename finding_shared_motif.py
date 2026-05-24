# This returns a longest common substring among sequences in a FASTA file.

from Bio import SeqIO

sequences = [str(record.seq) for record in SeqIO.parse("shared_motif.fasta", "fasta")]

longest_substring = ""

shortest_sequence = min(sequences, key=len)

seqs = [seq for seq in sequences if seq != shortest_sequence]

for i in range(len(shortest_sequence)):
    for j in range(i+1, len(shortest_sequence) + 1):
        substring = shortest_sequence[i:j]
        if len(substring) > len(longest_substring) and all(substring in seq for seq in seqs):
            longest_substring = substring

print(longest_substring)