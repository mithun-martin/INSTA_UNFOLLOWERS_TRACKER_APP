from flask import Flask, request, redirect, render_template
import os
import re

# Flask: lets you build a web app
# render_template: to show HTML pages (like index.html, result.html)
# request: to read data from the form (file uploads here)
# redirect: used if you ever want to send user to another route
# re: for regex (to extract usernames from URLs)
# os: to save & delete files from the system

app = Flask(__name__)

def extract_username(file_path):
    # (file_path) → This is the input parameter: a path to the file like "followers.html" or "following.html"
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        pattern = r'www\.instagram\.com/([a-zA-Z0-9_.]+)'
        usernames = re.findall(pattern, content)
        return usernames

# with → A Python keyword used for safe file handling. It automatically closes the file after reading — cleaner than open() + close() manually.
# "r" → Open the file in read mode
# encoding="utf-8" → Tells Python how to read special characters properly (especially important for web files)
# 🧠 file.read() → Reads the entire contents of the file (as a string)
# 🧠 content = ... → Save that string into a variable called content
# Now content holds all the HTML from the file.
# In programming, "" (empty string) and r"" (raw string) are used to represent strings, but they differ in how they handle backslashes 
# (`\`). An empty string contains no characters, while a raw string treats backslashes literally,
#   without interpreting them as escape sequences.

# 🧠 ([a-zA-Z0-9_.]+) → This is a regex pattern inside parentheses — it captures the username part
# a-zA-Z → Matches lowercase and uppercase letters
# 0-9 → Matches numbers
# _ and . → Matches underscores and dots
# + → Means “one or more of the above characters”

# now we apply regex to content to find all matches and get the usernames
# usernames = {'elonmusk', 'therock', 'nasa'}

@app.route('/')
def instructions():
    return render_template('instructions.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        followers_file = request.files.get('followers')
        following_file = request.files.get('following')
        # fetching files from the form

        followers_path = os.path.join("temp_followers.html")
        following_path = os.path.join("temp_following.html")
        # creating temporary file paths to save the uploaded files temporarily..now they r empty

        followers_file.save(followers_path)
        following_file.save(following_path)
        # 🧠 Actually saves the uploaded files to those paths

        followers = extract_username(followers_path)
        following = extract_username(following_path)
        # Now we can extract usernames from the saved files using the old function created

        os.remove(followers_path)
        os.remove(following_path)
        # 🧠 Deletes the temporary files used after reading the files saved in the path now no more needed those paths
        # get file -> create temporary path -> save file to that path -> extract usernames from path -> delete temp path

        # not_following_back = following - followers wrong bcz python does not support subtraction of lists
        # So we convert them to sets and then subtract
        not_following_back = set(following) - set(followers)
        print("Request method:", request.method)


        return render_template("result.html", not_following_back=not_following_back)
    
    
    return render_template('index.html')

# Read the uploaded files from the form
# The names "followers" and "following" must match the <input name="..."> in HTML
# So now:
# followers_file = file object for followers.html
# following_file = file object for following.html

# 🧠 Prepares file paths to temporarily save those uploads
# os.path.join(...) → builds a path string (good for cross-platform)
# We just call them temp_followers.html and temp_following.html


if __name__ == "__main__":
    app.run(debug=True)