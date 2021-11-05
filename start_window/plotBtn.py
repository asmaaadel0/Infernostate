import sys
sys.path.append('plot_window')
import tkinter as tk
from plot_window import run


class plotBtn:
    def __init__(self, frame, font,dataFrame):
        self.dataFrame = dataFrame
        button = tk.Button(frame, text='Plot', command=self.plotData, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10)

    def plotData(self):
        run(self.dataFrame)