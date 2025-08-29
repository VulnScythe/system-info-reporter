```
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗      ██╗███╗   ██╗███████╗ ██████╗       ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║      ██║████╗  ██║██╔════╝██╔═══██╗      ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║█████╗██║██╔██╗ ██║█████╗  ██║   ██║█████╗██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║╚════╝██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║      ██║██║ ╚████║██║     ╚██████╔╝      ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝       ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                          
```
# 🛰️ System Info & IP Reporter

A lightweight Python tool that collects **system information, local IPs, public IP, and approximate geolocation** and sends the report to a **Discord channel via webhook**.

---

## ✨ Features

- 📡 **System details**: OS, version, architecture, processor, hostname, and username  
- 🌐 **Local IPs**: Captures `ipconfig` (Windows) or `ifconfig` (Linux/macOS) output  
- 🔓 **Public IP**: Fetches external IP from [ipify](https://www.ipify.org)  
- 🌍 **Geolocation**: Uses [ipinfo.io](https://ipinfo.io) to resolve city, region, country, ISP, and coordinates  
- 📤 **Discord integration**: Sends everything to a channel using a webhook  
- ⚡ **Cross-platform**: Works on Windows, Linux, and macOS  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/system-info-reporter.git
cd system-info-reporter
```

### 2. Create a virtual environment (optional)
python -m venv venv

source venv/bin/activate   # macOS/Linux

venv\Scripts\activate  # Windows

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a .env file in the project root with the following code and your discord webhook:

DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_here

### 5. Run the script - python file
> reporter.py

---

### 📸 Example Discord Output
Machine Info:

System: Windows 11 (10.0.22621)
Machine: AMD64
Processor: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
Hostname: MY-PC
Username: johndoe

Local IPs:
Ethernet adapter Ethernet:
   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 192.168.1.42

Public IP:
123.45.67.89

Approx. Location:
City: Berlin

Region: Berlin
Country: DE
Coordinates: 52.5200,13.4050
ISP: AS12345 ExampleISP

---

### ⚠️ Disclaimer

This project is intended for educational and administrative use only.
Do not use it for malicious purposes. Always ensure you have permission before collecting or sharing system/network information.

### 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.
