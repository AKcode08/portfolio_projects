# Count Nucleotide Freq

def countNucFrequency(seq):
    tmpFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict 

DNAstring = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
result = countNucFrequency(DNAstring)

print(' '.join([str(val) for key, val in result.items()]))