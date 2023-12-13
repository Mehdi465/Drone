import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import time

class RealTimeGraphApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Real-Time Graphs")
        self.master.configure(bg="black")

        # Create the panel for the set of graphs
        self.panel1 = ttk.Frame(self.master)
        self.panel1.grid(row=0, column=0)

        # Create Figures and Axes for the set of graphs
        self.figures = []
        self.axes = []

        for i in range(3):
            fig = Figure(figsize=(5, 4), dpi=100, facecolor='black')
            ax = fig.add_subplot(111, facecolor='black')
            self.figures.append(fig)
            self.axes.append(ax)

        # Generate initial x values
        self.x = np.linspace(0, 2 * np.pi, 100)

        # Embed the set of graphs in the panel
        self.canvas_widgets = []

        for i in range(3):
            canvas = FigureCanvasTkAgg(self.figures[i], master=self.panel1)
            canvas.get_tk_widget().grid(row=0, column=i, padx=10, pady=10)
            self.canvas_widgets.append(canvas)

        # Schedule the real-time update for the set of graphs
        self.update_interval = 5000  # 5000 milliseconds = 5 seconds
        self.update_graphs()

    def plot_function(self, axes, y, label="Function"):
        axes.cla()  # Clear the current plot
        axes.plot(self.x, y, label=label)
        axes.legend()

        # Customize appearance
        axes.set_facecolor('black')
        axes.tick_params(axis='both', colors='white')
        axes.xaxis.label.set_color('white')
        axes.yaxis.label.set_color('white')
        axes.title.set_color('white')

    def update_graphs(self):
        # Simulate different functions for the set of graphs
        y1 = np.sin(self.x)
        y2 = np.cos(self.x)
        y3 = np.tan(self.x)

        # Plot functions on the respective Axes for the set of graphs
        self.plot_function(self.axes[0], y1, label="Sine Wave")
        self.plot_function(self.axes[1], y2, label="Cosine Wave")
        self.plot_function(self.axes[2], y3, label="Tangent Wave")

        # Update the canvas widgets for the set of graphs
        for canvas in self.canvas_widgets:
            canvas.draw()

        # Schedule the next update for the set of graphs
        self.master.after(self.update_interval, self.update_graphs)


class DroneHUDApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drone HUD")
        self.master.geometry("1920x1080")  # Set your desired window size
        self.master.configure(bg="black")

        # Create the panel for the drone HUD
        self.panel2 = ttk.Frame(self.master)
        self.panel2.grid(row=1, column=0)

        # Create a canvas with a black background
        self.canvas = tk.Canvas(self.panel2, bg="black")
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Variables to store drone information
        self.speed_var = tk.StringVar()
        self.position_var = tk.StringVar()
        self.angular_rotation_var = tk.StringVar()
        self.altitude_var = tk.StringVar()

        # Simulate updating drone information (replace this with your actual data update mechanism)
        self.update_drone_info()

    def update_drone_info(self):
        # Replace the following lines with actual data retrieval/update logic

        speed = f"{np.random.randint(0, 111)} km/h"
        position = "(10, 20)"
        angular_rotation = f"{float(np.random.randint(0, 90)) + np.random.random()} degrees"
        altitude = "300 meters"

        # Clear previous drawings on the canvas
        self.canvas.delete("all")

        # Draw HUD elements with a larger text size and modern font
        self.draw_text("Speed: {}".format(speed), 10, 20, "white", size=25, font_family="Arial")
        self.draw_text("Position: {}".format(position), 10, 50, "white", size=25, font_family="Arial")
        self.draw_text("Angular Rotation: {}".format(angular_rotation), 10, 80, "white", size=25, font_family="Arial")
        self.draw_text("Altitude: {}".format(altitude), 10, 110, "white", size=25, font_family="Arial")

        # Schedule the update after 1000 milliseconds (1 second)
        self.master.after(1000, self.update_drone_info)

    def draw_text(self, text, x, y, color, size, font_family):
        self.canvas.create_text(x, y, text=text, anchor=tk.W, fill=color, font=(font_family, size, "bold"))

class CombinedApp(RealTimeGraphApp, DroneHUDApp):
    def __init__(self, master):
        RealTimeGraphApp.__init__(self, master)
        DroneHUDApp.__init__(self, master)

def main():
    root = tk.Tk()
    app = CombinedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
