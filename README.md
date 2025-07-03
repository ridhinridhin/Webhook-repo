# GitHub Webhook Listener

This project listens for GitHub webhook events (Push and Pull Request) using a Flask app and displays them in a real-time web UI.

## 💡 Features

- Receives push and pull request events via GitHub Webhooks
- Stores all events in MongoDB Atlas
- Displays them in a simple HTML frontend (auto-refreshes every 15 seconds)
- Flask + PyMongo based backend
- ngrok used for local-to-public URL tunneling

## 🚀 How It Works

1. Start the Flask app locally
2. Expose it with ngrok: `ngrok http 5000`
3. Add the ngrok link + `/webhook` as a webhook in your GitHub repo
4. Push or create PRs in `action-repo`
5. Events appear instantly at `http://localhost:5000`

## 📦 Tech Stack

- Python 3.10
- Flask
- PyMongo
- MongoDB Atlas
- HTML/CSS (Jinja Templates)
- ngrok

## ✅ Setup Instructions

```bash
git clone https://github.com/ridhinridhin/Webhook-repo.git
cd Webhook-repo
pip install -r requirements.txt
python app.py
