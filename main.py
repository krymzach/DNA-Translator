def dna_to_rna(dna):
  dna = dna.toUpper()
  rna = ""
  for i in range(len(dna)):
    if(dna[i] == "A":
       rna += "U"
    elif(dna[i] == "T"):
       rna += "A"
    elif(dna[i] == "C"):
       rna += "G"
    elif(dna[i] == "G"):
       rna += "C"
  return rna
       
def rna_to_dna(rna):
  rna = rna.toUpper()
  dna = ""
  for i in range(len(rna)):
    if(rna[i] == "A":
       dna += "T"
    elif(rna[i] == "U"):
       dna += "A"
    elif(rna[i] == "C"):
       dna += "G"
    elif(rna[i] == "G"):
       dna += "C"
  return dna
       
def rna_to_aa(rna):
  j = 0
  while j < len(rna):
    

inp = input("What are you converting from ('DNA', 'RNA', or 'AA' for Amino Acids): ")
oup = input("What would you like to convert this too (use possible inputs from previous line): ")

if(inp != "DNA" and inp != "RNA" and inp != "AA"):
  print("Error: Invalid Input")
  quit()

if(oup != "DNA" and oup != "RNA" and oup != "AA"):
  print("Error: Invalid Output")
  quit()
  
if(inp == oup):
  print("Error: Input is equal to Output")
  quit()
  
if(inp == "DNA" and oup == "RNA"):
  print(dna_to_rna(inp))
elif(inp == "RNA" and oup == "DNA"):
  print(rna_to_dna(inp))
