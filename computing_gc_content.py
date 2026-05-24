# This returns the record ID with the highest GC-content and its GC percentage.

records = {}
seq = []
seq_id = None
max_gc_content = 0
max_gc_id = None

with open("rosalind.fasta") as fasta_file:
    for line in fasta_file:
        if line.startswith(">"):
            seq_id = line.strip().lstrip(">")
            seq = []
        else:
            seq.append(line.strip())
        records[seq_id] = "".join(seq)

for ids, seqs in records.items():
    gc_content = round((seqs.count("G") + seqs.count("C")) / len(seqs) * 100, 6)
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_id = ids

print(max_gc_id)
print(max_gc_content)