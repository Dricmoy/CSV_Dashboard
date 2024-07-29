import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualization App")

        # Create a button to load CSV
        self.load_button = tk.Button(root, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

        # Create a button to plot data
        self.plot_button = tk.Button(root, text="Plot Data", command=self.plot_data)
        self.plot_button.pack(pady=10)

        # Initialize a placeholder for the DataFrame
        self.df = None

        # Create a matplotlib figure and canvas
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                messagebox.showinfo("Data Loaded", "CSV file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def plot_data(self):
        if self.df is not None:
            numeric_cols = self.df.select_dtypes(include='number').columns
            if numeric_cols.size > 0:
                self.ax.clear()
                self.df[numeric_cols[0]].hist(ax=self.ax)
                self.ax.set_title(f'Histogram of {numeric_cols[0]}')
                self.ax.set_xlabel(numeric_cols[0])
                self.ax.set_ylabel('Frequency')
                self.canvas.draw()
            else:
                messagebox.showwarning("No Numeric Data", "No numeric columns found for plotting.")
        else:
            messagebox.showwarning("No Data", "Please load a CSV file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizationApp(root)
    root.mainloop()
