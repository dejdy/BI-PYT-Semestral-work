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
	
	leftFrame = tk.Frame(p.top,  height=10000, borderwidth=2, relief='groove')

	open_btn=tk.Button(master=leftFrame, text="Otevřít", command=p.loadImage, width=10)
	open_btn.grid(row=1, column=1, padx=10, pady=5)
	save_btn=tk.Button(master=leftFrame, text="Uložit", command=p.saveImage, width=10)
	save_btn.grid(row=1, column=2, padx=10, pady=5)

	rotL_btn=tk.Button(master=leftFrame, text="Otočit doleva", command=p.rotateLeft, width=10)
	rotL_btn.grid(row=2, column=1, padx=10, pady=5)
	rotR_btn=tk.Button(master=leftFrame, text="Otočit doprava", command=p.rotateRight, width=10)
	rotR_btn.grid(row=2, column=2, padx=10, pady=5)

	neg_btn=tk.Button(master=leftFrame, text="Negativ", command=p.to_negative, width=10)
	neg_btn.grid(row=3, column=1, padx=10, pady=5)

	mirr_btn=tk.Button(master=leftFrame, text="Převrátit", command=p.mirror, width=10)
	mirr_btn.grid(row=3, column=2, padx=10, pady=5)


	sc = tk.Scale(master=leftFrame, from_=0, to=200, orient='horizontal', label="Jas (%)", length=200)
	sc.set(100)
	sc.grid(row=4, column=1, columnspan=2)
	apply_btn=tk.Button(master=leftFrame, text="Použít", command=lambda: p.brighten(sc.get()), width=10)
	apply_btn.grid(row=5, column=1, padx=10, pady=10, columnspan=2)


	close_btn=tk.Button(master=leftFrame, text="Vrátit změny", command=p.revert, width=10)
	close_btn.grid(row=6, column=1, padx=10, pady=10)

	close_btn=tk.Button(master=leftFrame, text="Konec", command=p.top.destroy, width=10)
	close_btn.grid(row=6, column=2, padx=10, pady=10)

	leftFrame.grid(row=1, column=1, rowspan=1000)

	picture = Image.open(p.getPath())
	photoimage = ImageTk.PhotoImage(picture)

	p.canvas = tk.Label(p.wid, image = photoimage)
	p.canvas.image = photoimage
	p.canvas.grid()
	p.wid.grid(row=1, column=2, rowspan=6000, padx=50, pady=10)

	return p.top

