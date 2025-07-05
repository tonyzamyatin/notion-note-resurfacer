# 📓 Notion Note Resurfacer

**Rediscover old insights, spark new ideas.**
This simple script picks random notes from your Notion database to bring back serendipity into your knowledge system.

Inspired by the concept of **slow hunches** in *Where Good Ideas Come From* by Steven Johnson, this tool helps you revisit forgotten thoughts and make unexpected connections.

## 🧠 Motivation

Notion makes it easy to save lots of ideas. But over time, older notes get buried, and filters can limit your view.
This script helps by randomly bringing back notes you already wrote. This way, you can see them with fresh eyes and find new inspiration.

Inspired by the book *Where Good Ideas Come From* by Steven Johnson, it helps you revisit old thoughts and make new connections.

## 🧪 Example Use Case
You maintain a Notion database of 1,000 ideas. Every morning, this script picks 3 at random and flags them. You open the filtered Feed view of you notion database and review them over coffee. Marking them as read when you're done to save space on your Notion page.

## 🚀 Features

* Works with any Notion database
* No-code solution with minimal setup
* Can be automated via [Pipedream](https://pipedream.com) or similar schedulers

## ⚙️ Setup Instructions

### 1. Configure your Notion database

* Add a checkbox property called `"Today's idea"` (or choose your own).
* This property will be toggled by the script.

### 2. Create a Notion integration

* Follow the official guide: [Create a Notion integration](https://developers.notion.com/docs/create-a-notion-integration)
* Share your database with the integration so it has access.

### 3. Automate with Pipedream (or run manually)

* Follow the official Pipedream docs to [create a scheduled workflow](https://pipedream.com/docs/workflows/steps/triggers/#schedule-trigger).
* Set it to run at your preferred time (e.g. daily at 5 AM).

### 4. Set up the script

* Open `script.py` and fill in the **four variables** at the top:

  * `INTEGRATION_TOKEN`
  * `NOTION_DATABASE_ID`
  * `NUM_RANDOM_PAGES`
  * `PROP_NAME`
* That's it! You don't need to modify anything else.

### 5. View resurfaced notes

* In Notion, create a view with `Filter → "Today's idea" is checked`
* Or use the new **"Feed" view** (available in the latest Notion versions) to scroll through resurfaced notes like a social media feed.
* Tip: If you display the checkbox, you can uncheck notes after reading them to save space on your page.

## 📄 License

MIT License. Use and modify freely.
