dna_string= 'AAAACCCGGT'
def reverse_trans(dna_string):
    reverse_trans_string=''
    for i in dna_string:
        if i=='A': 
           reverse_trans_string=dna_string.replace('A','U')
       
        elif i=='G' and i=='C':
            reverse_trans_string= reverse_trans_string.replace("G", "_").replace("C", "G").replace("_", "C")
        else:
           reverse_trans_string=reverse_trans_string.replace('T','A')    
           return reverse_trans_string[::-1]
print(reverse_trans(dna_string))