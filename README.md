# Anti-Ghost-Ping Bot

A Discord bot that detects and alerts users when someone ghost-pings them.
## Features
### 🚨 Ghost Ping Detection
- Detects and alerts users when someone deletes a pinged message.
- Monitors edited messages to identify removed mentions.

### ✅ Whitelist System
- Allows trusted users to bypass ghost ping detection.
- Manage whitelist using /whitelist add/remove @user.

### 📌 Smart Alerts & Automatic Cleanup
- Sends an embed notification when ghost pings are detected.
- Alerts auto-delete after 10 seconds to keep chat clutter-free.

### 🔒 Role-Based Access
- Only the bot developer can pause or restart bot operations.

### 🌍 24/7 Hosting Compatibility
- Works with Railway, Heroku, AWS, Render, and other cloud hosting solutions.

## Installation

### **Step 1: Install Required Packages**
Before running the bot, install the necessary dependencies.

#### **Using pip (Python Package Manager)**
```sh
pip install -r requirements.txt
pip install discord.py
pip install python-dotenv
```
### Step 2: Create a .env File
Create a new file named .env in your project directory and add:
```
DISCORD_TOKEN=your_bot_token_here
```
***⚠️ Do NOT share your bot token publicly!***

### Step 3: Copy the bot.py File
Copy the provided bot.py code into your project directory.

### Step 4: Verify Installation & Check for Errors
Ensure all packages are installed correctly:
```
pip list
```
```
pip check
```

Then, test running the bot:
```
python bot.py
```

If errors appear, check your .env file and dependencies.
### Step 5 (Optional): Choose a Hosting Server
If you want to keep your bot online 24/7, use:
- Heroku
- Amazon WPS
- Railway
- Render
- Google Cloud Run

### Step 6: Start the Bot
✅ Invite the bot to your Discord server with the necessary OAuth2 scopes.
✅ Start the bot by running:
```
python bot.py
```

⚠️ Running the bot locally means your device must stay on 24/7 to keep it running
