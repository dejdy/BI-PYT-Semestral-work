#!/usr/bin/env python3

import PIL.Image
from PIL import ImageTk, Image
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

size=500, 400

class Pict:
	def __init__(self):
		self.name='files/img.jpg'
		self.ext = 'jpg'
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
		self.writeImage('temp/temp.' + self.ext)
		img = PIL.Image.open('temp/temp.' + self.ext)
		self.reloadImage('temp/temp.' + self.ext)

	def loadImage(self):
		f = filedialog.askopenfilename(title = "Vyberte soubor",filetypes = (("Soubory jpg","*.jpg *.jpeg *.JPG *.JPEG"),("Soubory png","*.png"),("Soubory gif","*.gif")))
		if f is None:
			return
		self.ext = os.path.splitext(f)[1].replace(".","")
		self.bw = False
		self.name=f
		self.loadArray()
		print('Loaded image ' + self.name)

	def writeImage(self, outName):
		outimg = PIL.Image.fromarray(self.data).convert('RGB')
		outimg.save(outName)

	def saveImage(self):
		f = filedialog.asksaveasfile(mode='wb',  filetypes = (("Soubory jpg","*.jpg"),("Soubory png","*.png"),("Soubory gif","*.gif")))
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
		self.data = (R * 0.299 + G * 0.587 + B * 0.114).astype('uint8')

		self.bw = True
		self.updateImage()


	def newVal(self, f, i, j):
		if i==0 or i >= (self.data.shape[0]-1) or j == 0 or j >= (self.data.shape[1]-1):
			return self.data[i][j]
		
		val = 0;
		for x in range(-1, 2):
			for y in range(-1, 2):
				val = val + self.data[i+x][j+y]*f[x+1][y+1]
		return val

	def applyFilter(self, f):
		newData = np.empty((self.data.shape[0], self.data.shape[1]))
		for i in range(self.data.shape[0]):
			for j in range(self.data.shape[1]):
				newData[i][j] = self.newVal(f, i, j)

		np.clip(newData, 0,255, newData)
		self.data = newData.astype('uint8')


	def edges(self):
		self.grey()
		f = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
		self.applyFilter(f)
		self.updateImage()
		print('Detect edges')



