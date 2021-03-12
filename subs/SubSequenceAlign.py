import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


class SequenceAlignApp(ttk.Frame):
    DNA_1 = {'G': {'G': 1, 'C': 0, 'A': 0, 'T': 0}, 'C': {'G': 0, 'C': 1, 'A': 0, 'T': 0},
             'A': {'G': 0, 'C': 0, 'A': 1, 'T': 0}, 'T': {'G': 0, 'C': 0, 'A': 0, 'T': 1}}
    DNA_2 = {'G': {'G': 1, 'C': -3, 'A': -3, 'T': -3, 'N': 0}, 'C': {'G': -3, 'C': 1, 'A': -3, 'T': -3, 'N': 0},
             'A': {'G': -3, 'C': -3, 'A': 1, 'T': -3, 'N': 0}, 'T': {'G': -3, 'C': -3, 'A': -3, 'T': 1, 'N': 0},
             'N': {'G': 0, 'C': 0, 'A': 0, 'T': 0, 'N': 0}}
    BLOSUM62 = {'A': {'A': 4, 'R': -1, 'N': -2, 'D': -2, 'C': 0, 'Q': -1, 'E': -1, 'G': 0, 'H': -2, 'I': -1,
                      'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1, 'T': 0, 'W': -3, 'Y': -2, 'V': 0, 'X': 0},
                'R': {'A': -1, 'R': 5, 'N': 0, 'D': -2, 'C': -3, 'Q': 1, 'E': 0, 'G': -2, 'H': 0, 'I': -3,
                      'L': -2, 'K': 2, 'M': -1, 'F': -3, 'P': -2, 'S': -1, 'T': -1, 'W': -3, 'Y': -2, 'V': -3, 'X': 0},
                'N': {'A': -2, 'R': 0, 'N': 6, 'D': 1, 'C': -3, 'Q': 0, 'E': 0, 'G': 0, 'H': 1, 'I': -3,
                      'L': -3, 'K': 0, 'M': -2, 'F': -3, 'P': -2, 'S': 1, 'T': 0, 'W': -4, 'Y': -2, 'V': -3, 'X': 0},
                'D': {'A': -2, 'R': -2, 'N': 1, 'D': 6, 'C': -3, 'Q': 0, 'E': 2, 'G': -1, 'H': -1, 'I': -3,
                      'L': -4, 'K': -1, 'M': -3, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -4, 'Y': -3, 'V': -3, 'X': 0},
                'C': {'A': 0, 'R': -3, 'N': -3, 'D': -3, 'C': 9, 'Q': -3, 'E': -4, 'G': -3, 'H': -3, 'I': -1,
                      'L': -1, 'K': -3, 'M': -1, 'F': -2, 'P': -3, 'S': -1, 'T': -1, 'W': -2, 'Y': -2, 'V': -1, 'X': 0},
                'Q': {'A': -1, 'R': 1, 'N': 0, 'D': 0, 'C': -3, 'Q': 5, 'E': 2, 'G': -2, 'H': 0, 'I': -3,
                      'L': -2, 'K': 1, 'M': 0, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -2, 'Y': -1, 'V': -2, 'X': 0},
                'E': {'A': -1, 'R': 0, 'N': 0, 'D': 2, 'C': -4, 'Q': 2, 'E': 5, 'G': -2, 'H': 0, 'I': -3,
                      'L': -3, 'K': 1, 'M': -2, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -3, 'Y': -2, 'V': -2, 'X': 0},
                'G': {'A': 0, 'R': -2, 'N': 0, 'D': -1, 'C': -3, 'Q': -2, 'E': -2, 'G': 6, 'H': -2, 'I': -4,
                      'L': -4, 'K': -2, 'M': -3, 'F': -3, 'P': -2, 'S': 0, 'T': -2, 'W': -2, 'Y': -3, 'V': -3, 'X': 0},
                'H': {'A': -2, 'R': 0, 'N': 1, 'D': -1, 'C': -3, 'Q': 0, 'E': 0, 'G': -2, 'H': 8, 'I': -3,
                      'L': -3, 'K': -1, 'M': -2, 'F': -1, 'P': -2, 'S': -1, 'T': -2, 'W': -2, 'Y': 2, 'V': -3, 'X': 0},
                'I': {'A': -1, 'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -3, 'E': -3, 'G': -4, 'H': -3, 'I': 4,
                      'L': 2, 'K': -3, 'M': 1, 'F': 0, 'P': -3, 'S': -2, 'T': -1, 'W': -3, 'Y': -1, 'V': 3, 'X': 0},
                'L': {'A': -1, 'R': -2, 'N': -3, 'D': -4, 'C': -1, 'Q': -2, 'E': -3, 'G': -4, 'H': -3, 'I': 2,
                      'L': 4, 'K': -2, 'M': 2, 'F': 0, 'P': -3, 'S': -2, 'T': -1, 'W': -2, 'Y': -1, 'V': 1, 'X': 0},
                'K': {'A': -1, 'R': 2, 'N': 0, 'D': -1, 'C': -3, 'Q': 1, 'E': 1, 'G': -2, 'H': -1, 'I': -3,
                      'L': -2, 'K': 5, 'M': -1, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -3, 'Y': -2, 'V': -2, 'X': 0},
                'M': {'A': -1, 'R': -1, 'N': -2, 'D': -3, 'C': -1, 'Q': 0, 'E': -2, 'G': -3, 'H': -2, 'I': 1,
                      'L': 2, 'K': -1, 'M': 5, 'F': 0, 'P': -2, 'S': -1, 'T': -1, 'W': -1, 'Y': -1, 'V': 1, 'X': 0},
                'F': {'A': -2, 'R': -3, 'N': -3, 'D': -3, 'C': -2, 'Q': -3, 'E': -3, 'G': -3, 'H': -1, 'I': 0,
                      'L': 0, 'K': -3, 'M': 0, 'F': 6, 'P': -4, 'S': -2, 'T': -2, 'W': 1, 'Y': 3, 'V': -1, 'X': 0},
                'P': {'A': -1, 'R': -2, 'N': -2, 'D': -1, 'C': -3, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -3,
                      'L': -3, 'K': -1, 'M': -2, 'F': -4, 'P': 7, 'S': -1, 'T': -1, 'W': -4, 'Y': -3, 'V': -2, 'X': 0},
                'S': {'A': 1, 'R': -1, 'N': 1, 'D': 0, 'C': -1, 'Q': 0, 'E': 0, 'G': 0, 'H': -1, 'I': -2,
                      'L': -2, 'K': 0, 'M': -1, 'F': -2, 'P': -1, 'S': 4, 'T': 1, 'W': -3, 'Y': -2, 'V': -2, 'X': 0},
                'T': {'A': 0, 'R': -1, 'N': 0, 'D': -1, 'C': -1, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -1,
                      'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1, 'T': 5, 'W': -2, 'Y': -2, 'V': 0, 'X': 0},
                'W': {'A': -3, 'R': -3, 'N': -4, 'D': -4, 'C': -2, 'Q': -2, 'E': -3, 'G': -2, 'H': -2, 'I': -3,
                      'L': -2, 'K': -3, 'M': -1, 'F': 1, 'P': -4, 'S': -3, 'T': -2, 'W': 11, 'Y': 2, 'V': -3, 'X': 0},
                'Y': {'A': -2, 'R': -2, 'N': -2, 'D': -3, 'C': -2, 'Q': -1, 'E': -2, 'G': -3, 'H': 2, 'I': -1,
                      'L': -1, 'K': -2, 'M': -1, 'F': 3, 'P': -3, 'S': -2, 'T': -2, 'W': 2, 'Y': 7, 'V': -1, 'X': 0},
                'V': {'A': 0, 'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -2, 'E': -2, 'G': -3, 'H': -3, 'I': 3,
                      'L': 1, 'K': -2, 'M': 1, 'F': -1, 'P': -2, 'S': -2, 'T': 0, 'W': -3, 'Y': -1, 'V': 4, 'X': 0},
                'X': {'A': 0, 'R': 0, 'N': 0, 'D': 0, 'C': 0, 'Q': 0, 'E': 0, 'G': 0, 'H': 0, 'I': 0,
                      'L': 0, 'K': 0, 'M': 0, 'F': 0, 'P': 0, 'S': 0, 'T': 0, 'W': 0, 'Y': 0, 'V': 0, 'X': 0}}

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)

        self.entry1 = scrolledtext.ScrolledText(self, width=30, height=5)
        self.entry1.grid(row=0, column=0)
        self.entry2 = scrolledtext.ScrolledText(self, width=30, height=5)
        self.entry2.grid(row=0, column=1)

        self.readVar = tk.IntVar()
        ttk.Radiobutton(self, text="Protein", variable=self.readVar, value=1).grid(row=1, column=0)
        ttk.Radiobutton(self, text="DNA", variable=self.readVar, value=0).grid(row=1, column=1)
        self.label = ttk.Label(self)
        self.label.grid(row=2, column=0)

        ttk.Button(self, text="Calc Sequence Similarity",
                   command=self.calcSequenceSimilarity).grid(row=3, column=0)
        ttk.Button(self, text="Calc Sequence Alignment",
                   command=self.calcSequenceAlignment).grid(row=3, column=1)

    def calcSeqIdentity(self, seqA: str, seqB: str):
        numPlaces = min(len(seqA), len(seqB))
        score = 0.0

        for i in range(numPlaces):
            if seqA[i] == seqB[i]:
                score += 1.0

        return 100.0 * score / numPlaces

    # This cannot handle gap sequence, represented with '-'
    def calcSeqSimilarity(self, seqA: str, seqB: str, simMatrix: dict):
        numPlaces = min(len(seqA), len(seqB))
        totalScore = 0.0

        for i in range(numPlaces):
            residueA = seqA[i]
            residueB = seqB[i]
            totalScore += simMatrix[residueA][residueB]

        return totalScore

    def pairAlignScore(self, alignA: str, alignB: str, simMatrix: dict, insert=8, extend=4):
        totalScore = 0.0
        n = min(len(alignA), len(alignB))

        for i in range(n):
            residueA = alignA[i]
            residueB = alignB[i]

            if '-' not in (residueA, residueB):
                simScore = simMatrix[residueA][residueB]
            elif (i > 0) and ('-' in (alignA[i - 1], alignB[i - 1])):
                simScore = -extend
            else:
                simScore = -insert

            totalScore += simScore

        return totalScore

    def calcSequenceSimilarity(self):
        if self.readVar.get() == 0:
            self.label['text'] = self.calcSeqSimilarity(self.entry1.get("1.0", tk.END).replace('\n', ""),
                                                        self.entry2.get("1.0", tk.END).replace('\n', ""),
                                                        SequenceAlignApp.DNA_2)
        else:
            self.label['text'] = self.calcSeqSimilarity(self.entry1.get("1.0", tk.END).replace('\n', ""),
                                                        self.entry2.get("1.0", tk.END).replace('\n', ""),
                                                        SequenceAlignApp.BLOSUM62)

    def calcSequenceAlignment(self):
        if self.readVar.get() == 0:
            self.label['text'] = self.pairAlignScore(self.entry1.get("1.0", tk.END).replace('\n', ""),
                                                     self.entry2.get("1.0", tk.END).replace('\n', ""),
                                                     SequenceAlignApp.DNA_2)
        else:
            self.label['text'] = self.pairAlignScore(self.entry1.get("1.0", tk.END).replace('\n', ""),
                                                     self.entry2.get("1.0", tk.END).replace('\n', ""),
                                                     SequenceAlignApp.BLOSUM62)
