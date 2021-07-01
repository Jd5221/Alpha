#!/usr/bin/env python3.9

# Encoder and Decoder created 6/30/2021 by Jacob Huffman(jd5221)
# Version 1.0

import tkinter as tk
from tkinter import *
import base64 
import sys


root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=500)
canvas.grid(columnspan=100, rowspan=100)

#root.configure(bg='grey')

root.title("def")

lbl = Label(root, text="Enter The Text You Want Encoded/Decoded")
lbl.grid(column=0, row=0)

intext_box = tk.Text(root, height=10, width=100, padx=15, pady=15)
intext_box.grid(columnspan=20, row=2)

outtext_box = tk.Text(root, height=10, width=100, padx=15, pady=15,)
outtext_box.grid(columnspan=20, row=4)

def En64():
	txt = intext_box.get("1.0",'end-1c')
	message = txt
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	outtext_box.insert(1.0, base64_message)

def Dc64():
	txt = intext_box.get("1.0",'end-1c')
	base64_message = txt
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	outtext_box.insert(1.0, message)

def En32():
	txt = intext_box.get("1.0",'end-1c')
	message = txt
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b32encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	outtext_box.insert(1.0, base64_message)

def Dc32():
	txt = intext_box.get("1.0",'end-1c')
	base64_message = txt
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b32decode(base64_bytes)
	message = message_bytes.decode('ascii')
	outtext_box.insert(1.0, message)

def delete():
	outtext_box.delete("1.0", "end")
	#intext_box.delete("1.0", "end")

b64_btn = tk.Button(root, text="Encode base64", bg="orange", fg="black", command=En64)
b64_btn.grid(column=1, row=0)

d64_btn = tk.Button(root, text="Decode base64", bg="grey", fg="black", command=Dc64)
d64_btn.grid(column=2, row=0)

b32_btn = tk.Button(root, text="Encode base32", bg="orange", fg="black", command=En32)
b32_btn.grid(column=3, row=0)

d32_btn = tk.Button(root, text="Decode base32", bg="grey", fg="black", command=Dc32)
d32_btn.grid(column=4, row=0)

del_btn = tk.Button(root, text="Clear", command=delete)
del_btn.place(relx=0.5, rely=0.94, anchor=CENTER)

root.mainloop()

