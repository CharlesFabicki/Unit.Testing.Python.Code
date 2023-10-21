import unittest
import psutil
import tkinter as tk


class TestSystemMonitor(unittest.TestCase):
    def test_cpu_label(self):
        root = tk.Tk()
        cpu_label = tk.Label(root, text="CPU usage: ", font=(None, 20, "bold"))
        cpu_label.pack()
        cpu_percent = psutil.cpu_percent()
        self.assertGreaterEqual(cpu_percent, 1)  # Check if CPU usage is over 1%
        root.destroy()

    def test_ram_label(self):
        root = tk.Tk()
        ram_label = tk.Label(root, text="RAM usage: ", font=(None, 20, "bold"))
        ram_label.pack()
        ram_percent = psutil.virtual_memory().percent
        self.assertGreaterEqual(ram_percent, 10)  # Check if RAM usage is over 10%
        root.destroy()


if __name__ == '__main__':
    unittest.main()
