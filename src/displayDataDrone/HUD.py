import tkinter as tk
from tkinter import ttk

class DroneHUDApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drone HUD")
        self.master.geometry("800x600")  # Set your desired window size

        # Create a canvas with a black background
        self.canvas = tk.Canvas(master, bg="black")
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
        speed = "100 km/h"
        position = "(10, 20)"
        angular_rotation = "45 degrees"
        altitude = "300 meters"

        # Clear previous drawings on the canvas
        self.canvas.delete("all")

        # Draw HUD elements
        self.draw_text("Speed: {}".format(speed), 10, 10, "white")
        self.draw_text("Position: {}".format(position), 10, 30, "white")
        self.draw_text("Angular Rotation: {}".format(angular_rotation), 10, 50, "white")
        self.draw_text("Altitude: {}".format(altitude), 10, 70, "white")

        # Schedule the update after 1000 milliseconds (1 second)
        self.master.after(1000, self.update_drone_info)

    def draw_text(self, text, x, y, color):
        self.canvas.create_text(x, y, text=text, anchor=tk.W, fill=color, font=("Arial", 12, "bold"))

def main():
    root = tk.Tk()
    app = DroneHUDApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
