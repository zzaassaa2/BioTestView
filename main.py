import tkinter as tk
from tkinter import ttk
import subs.SubEstMolMass as Mod1
import subs.SubGCContent as Mod2
import subs.SubDNAtoProtein as Mod3
import subs.SubImage as Mod4
import subs.SubSequenceAlign as Mod5
import subs.SubSignal as Mod6


class OpeningApplication(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent

        ttk.Label(self, text="Note: The program only excepts standard DNA/RNA/Protein codes, no ambiguous."
                             "\n\n"
                             "Module Info:"
                             "\n"
                             "Molecular Mass Estimator: This module takes a DNA, RNA, or amino acid Sequence,\n"
                             "and estimate the mass.\n"
                             "\n"
                             "GC Content: This module takes a sequence, such as DNA, and generates a plot of\n"
                             "the GC density within a region.\n"
                             "\n"
                             "DNA to Protein: This module takes a DNA sequence, and generates the amino acid\n"
                             "sequence generate from it.\n"
                             "\n"
                             "Image: This module takes in a path to an image, and then allows grey-scaling,\n"
                             "or alternating of the RGB values.\n"
                             "\n"
                             "Sequence Alignment: This module takes in two different sequences, of either DNA\n"
                             "or amino acid, and then calculates the similarity.\n"
                             "\n"
                             "Signal: This module takes in various parameters within the input,\n"
                             "and then generates a signal graph, and/or the fourier transform.").grid(row=0, column=0)


class Application(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent

        self.moduleFrame = OpeningApplication(self)
        self.moduleFrame.grid(row=0, column=1)

        self.selectedModule = tk.StringVar()
        self.modulePickFrame = ttk.Frame(self)
        self.modulePickFrame.grid(row=0, column=0, padx=8, pady=8)
        ttk.Label(self.modulePickFrame, text="Choose module").grid(row=0, column=0)
        module_choose = ttk.Combobox(self.modulePickFrame, width=20, textvariable=self.selectedModule, state="readonly")
        module_choose['values'] = ("Molecular Mass Estimator", "GC Content Plot",
                                   "DNA Seq to Protein", "Image", "Sequence Alignment",
                                   "Signal")
        module_choose.grid(row=1, column=0)
        module_button = ttk.Button(self.modulePickFrame, text="Change Module", command=self.changeModule)
        module_button.grid(row=2, column=0)

    def changeModule(self):
        self.moduleFrame.destroy()

        if self.selectedModule.get() == "Molecular Mass Estimator":
            self.moduleFrame = Mod1.EstimateMolMassApp(self)
        elif self.selectedModule.get() == "GC Content Plot":
            self.moduleFrame = Mod2.GCContentPlotApp(self)
        elif self.selectedModule.get() == "DNA Seq to Protein":
            self.moduleFrame = Mod3.DNAtoProteinApp(self)
        elif self.selectedModule.get() == "Image":
            self.moduleFrame = Mod4.ImageApp(self)
        elif self.selectedModule.get() == "Sequence Alignment":
            self.moduleFrame = Mod5.SequenceAlignApp(self)
        elif self.selectedModule.get() == "Signal":
            self.moduleFrame = Mod6.SignalApp(self)

        self.moduleFrame.grid(row=0, column=1)


root = tk.Tk()
root.title("BioTestView")
Application(root).pack(side="top", fill="both", expand=True)
root.mainloop()
