# 🧠 Smart Log Analyzer

**Smart Log Analyzer** is a local Python-based tool for analyzing, visualizing, and detecting anomalies in system, server, and application log files. Designed for IT departments, DevOps teams, and cybersecurity professionals, it enables secure, on-premises log processing without cloud dependency — fully GDPR-compliant.

---

## 🚀 Features

- 📁 **Log File Support:** CSV, JSON, TXT, LOG (custom formats via plugin)
- 🔍 **Anomaly Detection:** Identifies potential errors or suspicious events
- 📊 **Interactive Visualization:** Real-time statistics and visual feedback
- 🧠 **Extensible Architecture:** Ready for integration with ML models or custom rules
- 🔒 **Privacy First:** All processing is done locally — no telemetry, no cloud
- 🧰 **User-Friendly GUI:** Built with Tkinter for simple local interaction

---

## 🖥️ Screenshot

![Smart Log Analyzer Interface](./assets/screenshot.png)

---

## 📦 Installation

Make sure Python 3.10+ is installed.

```bash
git clone https://github.com/yourname/smart-log-analyzer.git
cd smart-log-analyzer
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application with:

```bash
python main.py
```

You can then:
- Select a log file
- View it in a table
- See automatic anomaly highlights
- Visualize event statistics (errors vs normal logs)

---

## 🔧 Project Structure

```
smart_log_analyzer/
├── main.py           # Entry point
├── gui.py            # GUI logic (Tkinter)
├── parser.py         # Multi-format log parser
├── analyzer.py       # Error/anomaly detection logic
├── visualizer.py     # Data visualization (Matplotlib)
├── requirements.txt  # Dependencies
└── README.md         # This file
```

---

## 📈 Planned Features

- Regex-based log parsing
- Timeline & heatmap visualizations
- Advanced anomaly scoring (ML-based)
- Multi-format export (PDF, CSV)
- Multi-user support (optional login & roles)

---

## ⚖️ License

MIT License – feel free to use, modify, and distribute.  
Attribution appreciated but not required.

---

## 🤝 Contributing

Pull requests, issue reports, and suggestions are welcome.  
Let’s make log analysis more efficient and secure – together.

---

## 🔐 Security & Compliance

All operations are executed **locally**.  
No external data transmission or tracking.  
Built with **privacy and GDPR** compliance in mind.
