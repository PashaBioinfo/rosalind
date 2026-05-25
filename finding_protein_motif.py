# This returns each protein ID along with the positions of the N-glycosylation motif in its sequence.

import re
import requests

url = "https://rest.uniprot.org/uniprotkb/"
motif = "(?=N[^P][ST][^P])"
sequences = {}

with open("protein_motif.txt", "r") as file:
    access_ids = [line.strip() for line in file]

for access_id in access_ids:
    fetch_id = access_id.split("_")[0]
    response = requests.get(f'{url}{fetch_id}.fasta')
    if response.status_code == 200:
        sequences[access_id] = "".join(response.text.split("\n")[1:])

for access_id, seq in sequences.items():
    positions = [m.start() + 1 for m in re.finditer(motif, seq)]
    if positions:
        print(access_id)
        print(" ".join(str(pos) for pos in positions))