# This returns the record ID with the highest GC-content and its GC percentage.

records = {}
sequence_parts = []
sequence_id = None
max_gc_content = 0
max_gc_id = None

with open("rosalind.fasta") as fasta_file:
    for line in fasta_file:
        if line.startswith(">"):
            sequence_id = line.strip().lstrip(">")
            sequence_parts = []
        else:
            sequence_parts.append(line.strip())
        records[sequence_id] = "".join(sequence_parts)

for seq_id, seq in records.items():
    gc_content = round((seq.count("G") + seq.count("C")) / len(seq) * 100, 6)
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_id = seq_id

print(max_gc_id)
print(max_gc_content)