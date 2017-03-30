#!/usr/bin/env python3

import PIL.Image
from PIL import ImageTk, Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

class Pict:
	def __init__(self):
		self.name='files/img.jpg'
		img = PIL.Image.open(self.name)
		self.data=  np.asarray( img, dtype='uint8' )

		self.top = tk.Tk()
		self.wid = tk.Frame(self.top)
		self.canvas = tk.Label(self.wid)

	def updateImage(self, img):
		photoimage = ImageTk.PhotoImage(img)
		self.canvas.configure(image = photoimage)
		self.canvas.image = photoimage

	def loadImage(self):
		self.name = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		img = PIL.Image.open(self.name)
		self.updateImage(img)
		try:
		    self.data = np.asarray( img, dtype='uint8' )
		except SystemError:
		    self.data = np.asarray( img.getdata(), dtype='uint8' )


	def writeImage(self, outName):
		outimg = PIL.Image.fromarray(self.data, "RGB")
		outimg.save(outName)

	def to_negative(self):
		self.data = 255-self.data
		self.writeImage('temp/temp.jpg')
		img = PIL.Image.open('temp/temp.jpg')
		self.updateImage(img)
		print('negativ')

	def rotate(self, num):
		self.data = np.rot90(self.data, num)

	def mirror(self):
		self.data = np.flip(self.data, 1)

	def getPath(self):
		return self.name

	def setCanvas(self, can):
		self.canvas = can
