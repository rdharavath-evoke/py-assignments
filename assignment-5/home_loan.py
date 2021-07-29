from _typeshed import Self
import logging
import tkinter
from tkinter import *

logging.info("Home loan calculator")
class LoanCalculator:
    window=Tk()   #create a window
    window.title("Loan Calculator")
    logging.info("create the input boxes")
    Label(window, text="Loan Amount").grid(row=1,column=1,sticky=W)
    Label(window, text="Rate of Interest").grid(row=2,column=1,sticky=W)
    Label(window, text="Number of Years").grid(row=3,column=1,sticky=W)

    Label(window, text="Total Interest").grid(row=4,column=1,sticky=W)
    Label(window, text="Total Amount").grid(row=5,column=1,sticky=W)

    logging.info("for taking inputs")
    Self.annual
