# 🐞 BUG-BOT: WhatsApp Automation & Anti-Scam Bot

A powerful WhatsApp bot built to automate tasks, manage chats, and protect users from scammers. Easily deployable via Render or Termux, BUG-BOT offers real-time message handling, customizable commands, and secure pairing with your WhatsApp account.

---

## 🚀 Features
- Anti-scam detection and auto-response
- Custom command support
- Real-time message monitoring
- Easy deployment via Render or Termux
- QR code pairing for WhatsApp

---

## 🛠️ Installation

### 🔧 Deploy on Render
1. Fork this repo to your GitHub account.
2. Add a `render.yaml` file to the root directory:
   ```yaml
   services:
     - type: web
       name: bug-bot
       env: node
       repo: https://github.com/alex96656/BUG-BOT
       branch: main
       buildCommand: npm install
       startCommand: node index.js
       autoDeploy: true
