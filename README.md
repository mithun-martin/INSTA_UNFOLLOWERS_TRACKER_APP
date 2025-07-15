# 📸 Insta Unfollowers Tracker 🔍

A simple Flask web app to check which Instagram accounts are not following you back — built with Python, Flask, Gunicorn, and deployed on Heroku.

---

## 🚀 Features

- Upload your **followers.html** and **following.html** files.
- Instantly see a list of accounts not following you back.
- Clean, mobile-friendly UI.
- Deployed live on Heroku.

---

## 📦 How It Works

1. **Download your Instagram data**:
   - Go to Instagram → More → Your Activity → Download your Information.
   - Choose *Followers & Following* → Download to device.

2. Once the files arrive:
   - Unzip the folder.
   - Copy **followers.html** and **following.html** into your computer.

3. **Open the app** and upload both files.

4. See the list of unfollowers instantly.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Production Server**: Gunicorn
- **Deployment**: Heroku
- **Frontend**: HTML, CSS (Tailwind CSS)

---

## 📡 Live Demo

👉 [Check it live on Heroku](https://insta-unfollowers-mithun-9455d165cd09.herokuapp.com/)

---

## 📝 How to Run Locally

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/insta-unfollowers-tracker.git
cd insta-unfollowers-tracker

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
flask run
