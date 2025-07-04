# 🌩️ SFU StormSage – Weather Alert Twitter Bot

A Python-powered Twitter bot that delivers real-time weather alerts, road and parking conditions, and driving updates for SFU Burnaby campus. Built by **Amraj Koonar** and **Amar Koonar**, this bot scrapes live data and webcam feeds to keep students and staff informed as conditions change.

---

## 🎯 Features

- 🌦️ **Real-Time Weather Alerts**: Posts live updates on weather, road conditions, and parking lot status.
- 📷 **Live Webcam Integration**: Includes webcam screenshots with each update for enhanced situational awareness.
- 🔍 **Web Scraping**: Uses BeautifulSoup to extract structured and unstructured data (text and images) from the [SFU Road Conditions Page](https://www.sfu.ca/security/sfuroadconditions/).
- 🐍 **Python-Based Automation**: Fully scripted in Python with Twitter API integration via Tweepy for automated posting.
- 🏫 **Campus Focused**: Designed specifically to support safety at SFU Burnaby Campus.
- 🔁 **Auto-Updating**: Continuously fetches new data and pushes alerts as conditions evolve.

---

## 🔗 Links

- 📡 **Live Bot**: [@sfulivewebcams on Twitter](https://x.com/sfulivewebcams)
- 🌐 **Data Source**: [SFU Security Road Conditions](https://www.sfu.ca/security/sfuroadconditions/)

---

## 🛠️ Setup & Installation

Follow the steps below to run SFU StormSage locally:

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/sfu-stormsage.git
cd sfu-stormsage
```

### 2. **Create Virtual Environment (optional)**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Configure Environment Variables**

Create a `.env` file in the root folder and add your keys:
```env
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_SECRET=your_token_secret
```

### 5. **Run the Bot**
```bash
python bot.py
```

The bot will begin scraping data and automatically tweet updates.

---

## 🧠 Tech Stack

- **Language**: Python
- **Libraries**: BeautifulSoup, Tweepy, Requests
- **Output Platform**: Twitter/X
- **Deployment**: Run locally or as a scheduled job (e.g., via cron or systemd)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE) and intended for educational and informational use only.



