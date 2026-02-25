from flask import Flask, render_template, request
import zipfile
import os
import re
import smtplib
from email.message import EmailMessage

from mashup_engine import reset_folder, download_audio, trim_audio, merge_audio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    singer = request.form["singer"]
    videos = int(request.form["videos"])
    duration = int(request.form["duration"])
    email = request.form["email"]

    if videos <= 10 or duration <= 20:
        return "Videos must be >10 and Duration must be >20 seconds"

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid Email Address"

    work = "web_temp"
    reset_folder(work)

    download_audio(singer, videos, work)
    clips = trim_audio(work, duration)

    output_file = "mashup.mp3"
    merge_audio(clips, output_file)

    zip_name = "mashup.zip"
    with zipfile.ZipFile(zip_name, "w") as zipf:
        zipf.write(output_file)

    send_mail(email, zip_name)

    return "Mashup sent successfully to your email!"

def send_mail(receiver, file):
    sender = "aasthac2605@gmail.com"
    password = "YOUR_APP_PASSWORD"

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Attached is your mashup zip file.")

    with open(file, "rb") as f:
        msg.add_attachment(f.read(), maintype="application",
                           subtype="zip", filename=file)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)