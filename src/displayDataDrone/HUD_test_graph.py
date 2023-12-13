import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import HUD 

class RealTimeGraphApp:
    def __init__(self, master):
        self.master = master
        #self.master.title("Real-Time Graphs")

        # Create Figures and Axes for the graphs
        self.figures = []
        self.axes = []

        for i in range(3):
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            self.figures.append(fig)
            self.axes.append(ax)

        # Generate initial x values
        self.x = np.linspace(0, 2 * np.pi, 100)

        # Embed the graphs in the Tkinter window
        self.canvas_widgets = []

        for i in range(3):
            canvas = FigureCanvasTkAgg(self.figures[i], master=self.master)
            canvas.get_tk_widget().grid(row=0, column=i, padx=10, pady=10)
            self.canvas_widgets.append(canvas)

        # Schedule the real-time update
        self.update_interval = 5000  # 5000 milliseconds = 5 seconds
        self.update_graphs()

    def plot_function(self, index, y, label="Function"):
        self.axes[index].cla()  # Clear the current plot
        self.axes[index].plot(self.x, y, label=label)
        self.axes[index].legend()

        # Customize appearance
        self.axes[index].set_facecolor('white')
        self.axes[index].tick_params(axis='both', colors='white')
        self.axes[index].xaxis.label.set_color('white')
        self.axes[index].yaxis.label.set_color('white')

    def update_graphs(self):
        # Simulate different functions for each graph
        y1 = np.sin(self.x)
        y2 = np.cos(self.x)
        y3 = np.tan(self.x)

        # Plot functions on the respective Axes
        self.plot_function(0, y1, label="Sine Wave")
        self.plot_function(1, y2, label="Cosine Wave")
        self.plot_function(2, y3, label="Tangent Wave")

        # Update the canvas widgets
        for canvas in self.canvas_widgets:
            canvas.draw()

        # Schedule the next update
        self.master.after(self.update_interval, self.update_graphs)

def main():
    root = tk.Tk()
    app1 = RealTimeGraphApp(root)
    app2 = HUD.DroneHUDApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
