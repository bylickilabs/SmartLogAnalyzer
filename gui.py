import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
from parser import parse_log
from analyzer import detect_anomalies
from visualizer import plot_events

def start_gui():
    root = tk.Tk()
    root.title("Smart Log Analyzer")

    def open_file():
        file_path = filedialog.askopenfilename(
            title="Logdatei auswählen",
            filetypes=[("Alle Dateien", "*.*"), ("Logdateien", "*.log *.txt *.csv *.json")]
        )
        if not file_path:
            return
        try:
            df = parse_log(file_path)
            anomalies = detect_anomalies(df)
            show_table(df, anomalies)
            plot_events(df, anomalies)
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    label = ttk.Label(frame, text="Bitte wählen Sie eine Logdatei aus:")
    label.pack(pady=8)

    btn_open = ttk.Button(frame, text="Datei auswählen", command=open_file)
    btn_open.pack(pady=8)

    root.mainloop()

def show_table(df, anomalies):
    win = tk.Toplevel()
    win.title("Logdaten – Übersicht")
    tree = ttk.Treeview(win)
    tree.pack(fill="both", expand=True)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    for col in df.columns:
        tree.heading(col, text=col)
    for idx, row in df.iterrows():
        style = ""
        if idx in anomalies:
            style = "anomaly"
        tree.insert("", "end", values=list(row), tags=(style,))
    tree.tag_configure("anomaly", background="#ffcdd2")