from tkinter import *
import tkinter as tk
from constants import COLOR, FONT, LABELS


class LABEL:
    def __init__(self):
        self.create_label()

    def create_label(self):
        for text in LABELS:
            label = Label(text=text, bg=COLOR, font=FONT)
            label.grid(column=0, row=LABELS.index(text) + 1)


class BUTTON(tk.Button):
    def __init__(self, text, column, row, span, comm, width):
        super().__init__()
        self.column = column
        self.row = row
        self.text = text
        self.span = span
        self.config(padx=10)
        self.comm = comm
        self.width = width
        self.create_button()

    def create_button(self):
        add_button = Button(text=self.text, bg=COLOR, command=self.comm, width=self.width)
        add_button.grid(column=self.column, row=self.row, columnspan=self.span)

