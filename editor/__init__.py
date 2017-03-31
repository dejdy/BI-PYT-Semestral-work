#!/usr/bin/env python3

import PIL.Image
from PIL import ImageTk, Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

size=500, 400

class Pict:
	def __init__(self):
		self.name='files/img.jpg'
		img = PIL.Image.open(self.name)
		self.data = np.asarray( img, dtype='uint8' )

		self.top = tk.Tk()
		self.wid = tk.Frame(self.top, borderwidth=2, relief='groove')
		self.canvas = tk.Label(self.wid)
		self.bw = False

	def reloadImage(self, name):
		thumb = PIL.Image.open(name)
		thumb.thumbnail(size, Image.ANTIALIAS)
		photoimage = ImageTk.PhotoImage(thumb)
		self.canvas.configure(image = photoimage)
		self.canvas.image = photoimage

	def revert(self):
		self.loadArray()
		self.bw = False

	def loadArray(self):
		self.reloadImage(self.name)
		img = PIL.Image.open(self.name)
		try:
		    self.data = np.asarray( img, dtype='uint8' )
		except SystemError:
		    self.data = np.asarray( img.getdata(), dtype='uint8' )
		

	def updateImage(self):
		self.writeImage('temp/temp.jpg')
		img = PIL.Image.open('temp/temp.jpg')
		self.reloadImage('temp/temp.jpg')

	def loadImage(self):
		f = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		if f is None:
			return
		self.name=f
		self.loadArray()
		print('Loaded image ' + self.name)

	def writeImage(self, outName):
		if self.bw == False:
			outimg = PIL.Image.fromarray(self.data, "RGB")
		else:
			outimg = PIL.Image.fromarray(self.data).convert('RGB')
		outimg.save(outName)

	def saveImage(self):
		f = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
		print('Saving image')
		if f is None:
			return
		self.writeImage(f)

	def to_negative(self):
		print('Applying negative filter')
		self.data = 255-self.data
		self.updateImage()

	def rotateLeft(self):
		print('Rotating left')
		self.data = np.rot90(self.data, 1)
		self.updateImage()

	def rotateRight(self):
		print('Rotating right')
		self.data = np.rot90(self.data, 3)
		self.updateImage()

	def mirror(self):
		print('Applying mirror filter')
		self.data = np.flip(self.data, 1)
		self.updateImage()

	def brighten(self, perc):
		print('Applying brightening filter - ' + str(perc) + '%')
		newData = self.data.astype(np.int32) * (perc/100)
		np.clip(newData, 0,255, newData)
		self.data = newData.astype('uint8')
		self.updateImage()


	def grey(self):
		if self.bw == True:
			return

		print('Black and white filter')
		R = self.data[:, :, 0]
		G = self.data[:, :, 1]
		B = self.data[:, :, 2]
		self.data = R * 0.299 + G * 0.587 + B * 0.114 / 1000

		self.bw = True
		self.updateImage()


	def edges(self):
		print('Detect edges')





