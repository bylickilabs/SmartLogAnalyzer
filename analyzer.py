def detect_anomalies(df):
    anomalies = []
    if "line" in df.columns:
        for idx, row in df.iterrows():
            if "error" in str(row["line"]).lower():
                anomalies.append(idx)
    return anomalies