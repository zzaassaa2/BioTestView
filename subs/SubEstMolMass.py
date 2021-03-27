import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import Utils


class EstimateMolMassApp(ttk.Frame):
    dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
    proteinSeq = 'IRTNGTHMQPLLKLMKFQKFLLELFTLQKRKPEKGYNLPIISLNQ'
    residueMasses = {
        "DNA": {"G": 329.21, "C": 289.18, "A": 323.21, "T": 304.19},
        "RNA": {"G": 345.21, "C": 305.18, "A": 329.21, "U": 302.16},
        "protein": {"A": 71.07, "R": 156.18, "N": 114.08, "D": 115.08,
                    "C": 103.10, "Q": 128.13, "E": 129.11, "G": 57.05, "H": 137.14, "I": 113.15, "L": 113.15,
                    "K": 128.17, "M": 131.19, "F": 147.17, "P": 97.11, "S": 87.07, "T": 101.10, "W": 186.20,
                    "Y": 163.17, "V": 99.13}}

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)

        self.typeOf = tk.StringVar()
        self.typeOf.set("protein")
        self.output = tk.StringVar()
        self.output.set("**Output**")

        leftFrame = ttk.Frame(self)
        leftFrame.grid(row=0, column=0, padx=8, pady=5)
        ttk.Radiobutton(leftFrame, text="Protein", variable=self.typeOf, value="protein").grid(row=0, column=0)
        ttk.Radiobutton(leftFrame, text="DNA", variable=self.typeOf, value="DNA").grid(row=1, column=0)
        ttk.Radiobutton(leftFrame, text="RNA", variable=self.typeOf, value="RNA").grid(row=2, column=0)
        self.src = scrolledtext.ScrolledText(self, width=50, height=5)
        self.src.grid(row=0, column=1)

        ttk.Button(self, text="Submit", command=lambda: self.output.set(self.estimateMolMass(self.src.get(1.0, "end-1c"), self.typeOf.get()))).grid(row=1, column=1)
        ttk.Label(self, textvariable=self.output).grid(row=2, column=1)

        rightFrame = ttk.Labelframe(self, text="Warning: this will clear the\ncontents on the input box")
        rightFrame.grid(row=0, column=2, pady=3)
        ttk.Button(rightFrame, text="Sample DNA Sequence",
                   command=lambda: self.setSrcData(EstimateMolMassApp.dnaSeq)).grid(row=0, column=0)
        ttk.Button(rightFrame, text="Sample RNA Sequence",
                   command=lambda: self.setSrcData(EstimateMolMassApp.dnaSeq.replace('T', 'U'))).grid(row=1, column=0)
        ttk.Button(rightFrame, text="Sample Protein Sequence",
                   command=lambda: self.setSrcData(EstimateMolMassApp.proteinSeq)).grid(row=2, column=0)

    def estimateMolMass(self, seq: str, molType='protein'):
        if seq == "":
            return "**Output**"

        if molType == "protein":
            if not Utils.validate_protein(seq):
                return "Invalid Protein sequence"
        elif molType == "DNA":
            if not Utils.validate_dna(seq):
                return "Invalid DNA sequence"
        elif molType == "RNA":
            if not Utils.validate_rna(seq):
                return "Invalid RNA sequence"

        massDict = EstimateMolMassApp.residueMasses[molType]
        # Begin with mass of extra end atoms H + OH
        molMass = 18.02
        for letter in seq:
            molMass += massDict.get(letter, 0.0)

        return molMass

    def setSrcData(self, insert: str):
        self.src.delete("1.0", tk.END)
        self.src.insert("1.0", insert)



