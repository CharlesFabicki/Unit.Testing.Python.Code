import psutil
import tkinter as tk

# Create the GUI window
root = tk.Tk()
root.title("System Monitor")

# Set the font size and weight
font_size = 20
font_weight = "bold"

# Create the CPU usage label
cpu_label = tk.Label(root, text="CPU usage: ", font=(None, font_size, font_weight))
cpu_label.pack()

# Create the RAM usage label
ram_label = tk.Label(root, text="RAM usage: ", font=(None, font_size, font_weight))
ram_label.pack()


# Function to update the labels with the current system usage
def update_labels():
    # Get CPU usage
    cpu_percent = psutil.cpu_percent()
    cpu_label.config(text=f"CPU usage: {cpu_percent}%", font=(None, font_size, font_weight))

    # Get RAM usage
    ram_percent = psutil.virtual_memory().percent
    ram_label.config(text=f"RAM usage: {ram_percent}%", font=(None, font_size, font_weight))

    # Schedule the function to run again after 1 second
    root.after(1000, update_labels)


# Schedule the function to run initially
update_labels()

# Adjust the window size to fit the labels
root.update()
width = root.winfo_width()
height = root.winfo_height()
root.geometry(f"{width}x{height}")

# Start the GUI event loop
root.mainloop()
