import matplotlib.pyplot as plt

def plot_events(df, anomalies=None):
    if "line" in df.columns:
        error_count = sum("error" in str(l).lower() for l in df["line"])
        normal_count = len(df) - error_count
        labels = ["Normal", "Fehler"]
        values = [normal_count, error_count]
        plt.figure(figsize=(5,3))
        plt.bar(labels, values)
        plt.title("Fehler-Ereignisse im Log")
        plt.show()