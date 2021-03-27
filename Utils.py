def validate_dna(dna_seq: str):
    seq = dna_seq.upper()
    valid = seq.count('A') + seq.count('C') + seq.count('G') + seq.count('T')

    return valid == len(seq)


def validate_rna(rna_seq: str):
    seq = rna_seq.upper()
    valid = seq.count('A') + seq.count('C') + seq.count('G') + seq.count('U')

    return valid == len(seq)


def validate_protein(protein_seq: str):
    seq = protein_seq.upper()
    valid = seq.count('A') + seq.count('R') + seq.count('N') + seq.count('D') + seq.count('C') + seq.count('Q') \
        + seq.count('E') + seq.count('G') + seq.count('H') + seq.count('I') + seq.count('L') + seq.count('K') \
        + seq.count('M') + seq.count('F') + seq.count('P') + seq.count('S') + seq.count('T') + seq.count('W') \
        + seq.count('Y') + seq.count('V')

    return valid == len(seq)


def transcription(dna_seq: str):
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    return dna_seq.upper().replace('T', 'U')


def dna_reverse_complement(dna_seq: str):
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    comp = list(dna_seq.upper())
    for index, c in enumerate(comp):
        if c == 'A':
            comp[index] = 'T'
        elif c == 'T':
            comp[index] = 'A'
        elif c == 'G':
            comp[index] = 'C'
        elif c == 'C':
            comp[index] = 'G'

    return "".join(comp[::-1])
