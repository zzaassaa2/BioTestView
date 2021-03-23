import tkinter as tk
from tkinter import ttk
import matplotlib as mp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from numpy.random import standard_normal as normal
from widgets.NumberEntry import *
from numpy.fft import fft

mp.use("TkAgg")


class SignalApp(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)

        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=0, column=0)
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(row=1, column=0)
        self.ft_frame = ttk.Frame(self)
        self.ft_frame.grid(row=0, column=1)

        self.parem = []
        self.int_number = 0
        self.nPoints = tk.IntVar(value=50)
        ttk.Button(self.input_frame, text="Generate Graph", command=self.createPlot).grid(row=0, column=0)
        ttk.Button(self.input_frame, text="New Parameter Entry", command=self.addParameterRow).grid(row=0, column=1)
        NumberEntry(self.input_frame, False, textvariable=self.nPoints).grid(row=0, column=2)
        ttk.Label(self.input_frame, text="Amplitude").grid(row=1, column=0)
        ttk.Label(self.input_frame, text="Frequency").grid(row=1, column=1)
        ttk.Label(self.input_frame, text="Decay").grid(row=1, column=2)
        self.addParameterRow()

        ttk.Button(self.ft_frame, text="Fourier Transform (Real)", command=lambda: self.createFFTGraphs("Real"))\
            .grid(row=2, column=0)
        ttk.Button(self.ft_frame, text="Fourier Transform (Imaginary)", command=lambda: self.createFFTGraphs("Imag"))\
            .grid(row=3, column=0)
        ttk.Button(self.ft_frame, text="Fourier Transform (Magnitude)", command=lambda: self.createFFTGraphs("Mag"))\
            .grid(row=4, column=0)

        self.createPlot(False)
        self.createFFTGraphs()

    def addParameterRow(self):
        self.parem.append([tk.DoubleVar(value=1), tk.DoubleVar(value=1), tk.DoubleVar(value=1)])
        NumberEntry(self.input_frame, True, textvariable=self.parem[self.int_number][0]).grid(row=self.int_number + 2,
                                                                                              column=0)
        NumberEntry(self.input_frame, True, textvariable=self.parem[self.int_number][1]).grid(row=self.int_number + 2,
                                                                                              column=1)
        NumberEntry(self.input_frame, True, textvariable=self.parem[self.int_number][2]).grid(row=self.int_number + 2,
                                                                                              column=2)
        self.int_number += 1

    def createFFTGraphs(self, what_to_show: str = ""):
        self.ft_figure = Figure(figsize=(5, 4), dpi=100)
        self.ft_plot = self.ft_figure.add_subplot()
        title = "Fourier Transform"

        if what_to_show != "":
            t, sig = self.genPlotData()
            freq = fft(sig)
            if what_to_show == "Real":
                freqReal = [f.real for f in freq]
                self.ft_plot.plot(t, freqReal)
                title += " (Real)"
            elif what_to_show == "Imag":
                freqImag = [f.imag for f in freq]
                self.ft_plot.plot(t, freqImag)
                title += " (Imaginary)"
            elif what_to_show == "Mag":
                freqMag = [abs(f)**2 for f in freq]
                self.ft_plot.plot(t, freqMag)
                title += " (Magnitude)"

        self.ft_plot.set(xlabel="Frequency", ylabel="Intensity", title=title)
        self.ft_plot.grid()
        # to this everytime to update canvas
        self.ft_canvas = FigureCanvasTkAgg(self.ft_figure, self.ft_frame)
        self.ft_canvas.get_tk_widget().grid(row=0, column=0)
        # pack_toolbar=False will make it easier to use a layout manager later on.
        self.ft_navbar = NavigationToolbar2Tk(self.ft_canvas, self.ft_frame, pack_toolbar=False)
        self.ft_navbar.grid(row=1, column=0)
        self.ft_navbar.update()

    def createPlot(self, showData: bool = True):
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot()

        if showData:
            t, sig = self.genPlotData()
            self.plot.plot(t, sig.real)

        self.plot.set(xlabel="time", ylabel="Intensity", title="Signal Graph")
        self.plot.grid()

        # to this everytime to update canvas
        self.canvas = FigureCanvasTkAgg(self.figure, self.main_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0)

        # pack_toolbar=False will make it easier to use a layout manager later on.
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.main_frame, pack_toolbar=False)
        self.toolbar.grid(row=1, column=0)
        self.toolbar.update()

    def genPlotData(self):
        sig = np.zeros(self.nPoints.get(), dtype=complex)
        t = 0.1 * np.arange(self.nPoints.get(), dtype=float)
        I = 1j
        for amplitude, frequency, decay in self.parem:
            sig += amplitude.get() * np.exp(2 * np.pi * I * frequency.get() * t) * np.exp(-decay.get() * t)
        noise = 0.0
        noise *= np.sqrt(0.5)
        sig += noise * (normal(self.nPoints.get()) + I * normal(self.nPoints.get()))
        return t, sig

