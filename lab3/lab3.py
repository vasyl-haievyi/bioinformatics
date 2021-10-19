from Bio import Entrez
Entrez.email = "vasyl.haievyi@student.uj.edu.pl"

handle = Entrez.esearch(db="gene",term="BRCA1", retmax=10)
result = Entrez.read(handle)

id_list = result['IdList']

handle = Entrez.esummary(db="gene", id=",".join(id_list))
result = Entrez.read(handle)

for record in result['DocumentSummarySet']['DocumentSummary']:
    keys = ["Name", "Chromosome", "MapLocation", "Description"]
    str = ", ".join([f"{key} : {record[key]}" for key in keys])
    print(str)


record = next(iter(result))