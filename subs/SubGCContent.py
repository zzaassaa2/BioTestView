import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import scrolledtext


class GCContentPlotApp(ttk.Frame):
    dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)

        self.src = scrolledtext.ScrolledText(self, width=50, height=5)
        self.src.grid(row=0, column=0, padx=5, pady=0)
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(buttonFrame, text="Plot",
                   command=lambda: self.plot(self.src.get(1.0, "end-1c"))).grid(row=0, column=0, padx=5)
        ttk.Button(buttonFrame, text="Default Data",
                   command=lambda: self.setSrcData(GCContentPlotApp.dnaSeq)).grid(row=0, column=1, padx=5)

    def plot(self, toGraph: str):
        fig = Figure(figsize=(5, 5), dpi=100)
        gcResults = self.calcGcContent(toGraph)
        plot1 = fig.add_subplot(111)
        plot1.plot(gcResults)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        # toolbar = NavigationToolbar2Tk(canvas, self)
        # toolbar.update()
        canvas.get_tk_widget().grid(row=2, column=0, padx=5, pady=5)

    def calcGcContent(self, seq, winSize=10):
        gcValues = []

        for i in range(len(seq) - winSize):
            subSeq = seq[i:i + winSize]
            numGc = subSeq.count('G') + subSeq.count('C')
            value = numGc / float(winSize)
            gcValues.append(value)

        return gcValues

    def setSrcData(self, insert: str):
        self.src.delete("1.0", tk.END)
        self.src.insert("1.0", insert)

