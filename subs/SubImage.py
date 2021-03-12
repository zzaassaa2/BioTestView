import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np


class ImageApp(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)

        self.loadedImage = None
        self.render = None
        self.path = tk.StringVar()
        self.text = ttk.Entry(self, textvariable=self.path)
        self.text.grid(row=0, column=0)
        ttk.Button(self, text="Load Image", command=self.loadImage).grid(row=0, column=1)

        self.imageFrame = ttk.Frame(self)
        self.imageFrame.grid(row=1, column=0)
        self.image = ttk.Label(self.imageFrame, text='**Load Image**').grid(row=0, column=0)
        ttk.Button(self.imageFrame, text="Reset", command=self.loadImage).grid(row=0, column=1)
        ttk.Button(self.imageFrame, text="GreyScale", command=self.greyscaleToggle).grid(row=0, column=2)

        self.transform_red = tk.DoubleVar()
        self.transform_red.set(1.0)
        self.transform_green = tk.DoubleVar()
        self.transform_green.set(1.0)
        self.transform_blue = tk.DoubleVar()
        self.transform_blue.set(1.0)

        self.transformFrame = ttk.Frame(self.imageFrame)
        self.transformFrame.grid(row=1, column=1)
        ttk.Label(self.transformFrame, text="Red Scale Value").grid(row=0, column=0, sticky=tk.W)
        ttk.Scale(self.transformFrame, from_=0, to=1, value=1,
                  command=lambda value: self.setTransform(value, "Red")).grid(row=1, column=0, sticky=tk.W)
        ttk.Label(self.transformFrame, text="Green Scale Value").grid(row=2, column=0, sticky=tk.W)
        ttk.Scale(self.transformFrame, from_=0, to=1, value=1,
                  command=lambda value: self.setTransform(value, "Green")).grid(row=3, column=0, sticky=tk.W)
        ttk.Label(self.transformFrame, text="Blue Scale Value").grid(row=4, column=0, sticky=tk.W)
        ttk.Scale(self.transformFrame, from_=0, to=1, value=1,
                  command=lambda value: self.setTransform(value, "Blue")).grid(row=5, column=0, sticky=tk.W)

    def greyscaleToggle(self):
        if self.loadedImage is not None:
            newImage = self.loadedImage.convert('L')
            self.render = ImageTk.PhotoImage(newImage)
            self.image.create_image((0, 0), image=self.render, anchor='nw')

    def setTransform(self, value, mode: str):
        if mode == "Red":
            self.transform_red.set(value)
        elif mode == "Green":
            self.transform_green.set(value)
        elif mode == "Blue":
            self.transform_blue.set(value)

        if self.loadedImage is not None:
            pixmap = self.imageToPixmapRGB(self.loadedImage)
            transform = np.array([[self.transform_red.get(), 0.0, 0.0],
                                  [0.0, self.transform_green.get(), 0.0],
                                  [0.0, 0.0, self.transform_blue.get()]])
            pixmap2 = np.dot(pixmap, transform)
            newImage = self.pixmapToImage(pixmap2)
            newImage = newImage.resize((200, 200))
            self.render = ImageTk.PhotoImage(newImage)
            self.image.create_image((0, 0), image=self.render, anchor='nw')

    def pixmapToImage(self, pixmap: np.array, mode="RGB"):
        if pixmap.max() > 255:
            pixmap *= 255.0 / pixmap.max()

        pixmap = np.array(pixmap, np.uint8)
        img = Image.fromarray(pixmap, mode)
        return img

    def imageToPixmapRGB(self, img):
        img2 = img.convert("RGB")
        w, h = img2.size
        data = img2.getdata()
        pixmap = np.array(data, np.uint8)
        pixmap = pixmap.reshape((h, w, 3))
        return pixmap

    def loadImage(self):
        if self.image is not None:
            self.image.destroy()
            self.image = None

        self.image = tk.Canvas(self.imageFrame, width=200, height=200)
        self.image.grid(row=0, column=0)

        self.loadedImage = Image.open(self.path.get())
        self.loadedImage = self.loadedImage.resize((200, 200))

        self.render = ImageTk.PhotoImage(self.loadedImage)
        self.image.create_image((0,0), image=self.render, anchor='nw')
