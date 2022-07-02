DNA=input("DNA: ")
#DNA='CGTACATACACGCGGACAAGCGTACCTGCATCTACAAA'
RNA=''
for i in range(len(DNA)):
  if DNA[i]=='A':
    RNA=RNA+'U'
  elif DNA[i]=='C':
    RNA=RNA+'G'
  elif DNA[i]=='G':
    RNA=RNA+'C'
  elif DNA[i]=='T':
    RNA=RNA+'A'
if "AUG" in RNA:
  RNA=RNA.replace("AUG","[AUG]",1)
RNAsplit=[a for a in RNA]
#print(RNAsplit)
len_RNAsplit=len(RNAsplit)
a=1
b=5
for i in range(len_RNAsplit+99999999):
  if RNAsplit[i]==']':
    if (RNAsplit[i+1]=='U' and RNAsplit[i+2]=='A' and RNAsplit[i+3]=='G') or (RNAsplit[i+1]=='U' and RNAsplit[i+2]=='A' and RNAsplit[i+3]=='A') or (RNAsplit[i+1]=='U' and RNAsplit[i+2]=='G' and RNAsplit[i+3]=='A'):
      break
    else:
      RNAsplit.insert(i+1,'[')
      RNAsplit.insert(i+5,']')
      len_RNAsplit+=2

#print(RNA)
RNAb=''
for i in range(len(RNAsplit)):
  #print(RNAsplit[i],end="")
  RNAb=RNAb+RNAsplit[i]
#print(RNAb)
if "UAA" in RNA:
  RNAb=RNAb.replace("[UAA]","UAA")
if "UGA" in RNA:
  RNAb=RNAb.replace("[UGA]","UGA")
if "UAG" in RNA:
  RNAb=RNAb.replace("[UAG]","UAG")
#print(RNAb)
c=']'
count=[i.count(c) for i in RNAb]
count
sum=0
for i in range(len(count)):
  sum+=count[i]
print(f"{sum} Amino acid(s)")