#!/usr/bin/env python
import gfx
import cv2
import sys
import os
def pdf2bitmap():
	print("Converting into bitmap...")
	doc = gfx.open("pdf", sys.argv[1])
	img = gfx.ImageList()
	img.setparameter("antialise", "1")
	page1 = doc.getPage(1)
	img.startpage(page1.width,page1.height)
	page1.render(img)
	img.endpage()
	img.save("temporal.png")
	print("Done!")
def encontrarpix(plop):
	print("Serching for a non white pixel (This may take a while)")
	dot = []
	im = cv2.imread("temporal.png")
	for x in range(plop[1],584):
		for y in range(plop[0]+1,841):
			px = im[y,x]
			if px[0] != 255 or px[1] != 255 or px[2] != 255:
				break
		if px[0] != 255 or px[1] != 255 or px[2] != 255:
			break
	dot.append(y)
	dot.append(x)
	if x != 583 and y != 840:
		print("Done!")
		print ("Line starts at :")
		print dot
		chainpix(dot)
	else:
		print("No more lines left... Bye :D")
def chainpix(dot):
	im = cv2.imread("temporal.png")
	px = im[dot[0],dot[1]]
	if px[0] !=255 or px[1] != 255 or px[2] != 255:
		d = chainpix([dot[0]+1,dot[1]+1])
		if d == 0:
			d = chainpix([dot[0]+1,dot[1]])
			if d ==0:
				d = chainpix([dot[0],dot[1]+1])
				if d ==0:
					d= chainpix([dot[0]-1,dot[0]+1])
					if d==0:
						print("Done!")
						print("Line ends at :") 
						print dot
						encontrarpix(dot)
	else:
		return 0
def clean():
	print("Cleaning Up")
	os.remove("temporal.png")
	print("Done!")
pdf2bitmap()
encontrarpix([0,0])
clean()

	
	
