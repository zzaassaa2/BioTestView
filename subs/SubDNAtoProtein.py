import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


class DNAtoProteinApp(ttk.Frame):
    dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
    STANDARD_GENETIC_CODE = {
        'UUU': 'Phe', 'UUC': 'Phe', 'UCU': 'Ser', 'UCC': 'Ser', 'UAU': 'Tyr', 'UAC': 'Tyr', 'UGU': 'Cys', 'UGC': 'Cys',
        'UUA': 'Leu', 'UCA': 'Ser', 'UAA': None, 'UGA': None, 'UUG': 'Leu', 'UCG': 'Ser', 'UAG': None, 'UGG': 'Trp',
        'CUU': 'Leu', 'CUC': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro', 'CAU': 'His', 'CAC': 'His', 'CGU': 'Arg', 'CGC': 'Arg',
        'CUA': 'Leu', 'CUG': 'Leu', 'CCA': 'Pro', 'CCG': 'Pro', 'CAA': 'Gln', 'CAG': 'Gln', 'CGA': 'Arg', 'CGG': 'Arg',
        'AUU': 'Ile', 'AUC': 'Ile', 'ACU': 'Thr', 'ACC': 'Thr', 'AAU': 'Asn', 'AAC': 'Asn', 'AGU': 'Ser', 'AGC': 'Ser',
        'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', 'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
        'GUU': 'Val', 'GUC': 'Val', 'GCU': 'Ala', 'GCC': 'Ala', 'GAU': 'Asp', 'GAC': 'Asp', 'GGU': 'Gly', 'GGC': 'Gly',
        'GUA': 'Val', 'GUG': 'Val', 'GCA': 'Ala', 'GCG': 'Ala', 'GAA': 'Glu', 'GAG': 'Glu', 'GGA': 'Gly', 'GGG': 'Gly'}

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)

        self.output = tk.StringVar()
        self.output.set("Enter Value Within Text Field")

        self.text = scrolledtext.ScrolledText(self, width=30, height=5)
        self.text.grid(row=0, column=0)

        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(buttonFrame, text="submit",
                   command=lambda: self.output.set(self.proteinTranslation(self.text.get(1.0, 'end-1c')))).grid(row=0,
                                                                                                                column=0)
        ttk.Button(buttonFrame, text="default", command=lambda: self.setSrcData(DNAtoProteinApp.dnaSeq)).grid(row=0, column=1)
        ttk.Label(self, textvariable=self.output).grid(row=2, column=0)

    def proteinTranslation(self, seq: str, geneticCode=STANDARD_GENETIC_CODE):
        # Convert to RNA sequence
        seq = seq.replace('T', 'U')
        proteinSeq = []

        i = 0
        while i + 2 < len(seq):
            codon = seq[i:i + 3]
            aminoAcid = geneticCode[codon]
            if aminoAcid is None:
                break

            proteinSeq.append(aminoAcid)
            i += 3

        return ''.join(proteinSeq)

    def setSrcData(self, insert: str):
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", insert)
