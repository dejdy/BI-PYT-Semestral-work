from PIL import ImageTk, Image
import tkinter as tk

def get_window_geometry(window_dim, screen_dim):
	x = (screen_dim[0] - window_dim[0])/2
	y = (screen_dim[1] - window_dim[1])/2
	return '%dx%d+%d+%d' % (window_dim[0], window_dim[1], x, y)


def display(p):
	p.top.title('Image editor')

	window_dimensions = (960, 480)
	screen_dimensions = (p.top.winfo_screenwidth(), p.top.winfo_screenheight())
	p.top.geometry(get_window_geometry(window_dimensions, screen_dimensions))
	

	button1=tk.Button(text="Otevřít", command=p.loadImage)
	button1.grid(row=1, column=1, padx=10, pady=10)

	button1=tk.Button(text="Negativ", command=p.to_negative)
	button1.grid(row=2, column=1, padx=10, pady=10)

	button1=tk.Button(text="Převrátit")
	button1.grid(row=3, column=1, padx=10, pady=10)


	picture = Image.open(p.getPath())
	photoimage = ImageTk.PhotoImage(picture)

	p.canvas = tk.Label(p.wid, image = photoimage)
	p.canvas.image = photoimage
	p.canvas.grid()
	p.wid.grid(row=1, column=2, rowspan=3, padx=10, pady=10)

	p.setCanvas(p.canvas)



	return p.top

