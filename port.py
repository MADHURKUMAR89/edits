from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# ── Portfolio data ────────────────────────────────────────────────────────────
PORTFOLIO = {
    "name": "Masher",
    "tagline": "Crafting stories, frame by frame.",
    "description": (
        "I transform raw footage into cinematic stories that connect with people "
        "emotionally. Through precise editing, sound design, and color grading, I "
        "bring life, rhythm, and feeling to every vlog and reel. My goal is simple "
        "— to create visuals that people don't just watch, but truly experience."
    ),
    "location": "India",
    "email": "madhurkumar8989@gmail.com",
    "instagram": "https://www.instagram.com/madhur_saini__432?igsh=MXAzZGI5bXdwaDFmYg==",
    "specialties": [
        {"icon": "ti-device-tv",     "label": "YouTube & Vlogs"},
        {"icon": "ti-device-mobile", "label": "Social Media Reels"},
        {"icon": "ti-heart",         "label": "Weddings & Events"},
        {"icon": "ti-color-swatch",  "label": "Color Grading"},
        {"icon": "ti-music",         "label": "Sound Design"},
        {"icon": "ti-cut",           "label": "Motion Editing"},
    ],
    "works": [
        {
            "title": "YouTube Travel Vlog",
            "meta": "YOUTUBE · VLOG",
            "thumb_class": "thumb-youtube",
            "icon": "ti-brand-youtube",
            "badge": "YouTube",
            "url": "https://youtu.be/5bNp0VifFq4?si=IA6nVr3rOyP4SdM5",
        },
        {
            "title": "Brand Instagram Reel",
            "meta": "SOCIAL MEDIA · 30 SEC",
            "thumb_class": "thumb-reel",
            "icon": "ti-brand-instagram",
            "badge": "Reel",
            "url": "https://www.instagram.com/reel/DXvOVCGJ8US/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==",
        },
        {
            "title": "Wedding Highlight Film",
            "meta": "WEDDING · 4 MIN",
            "thumb_class": "thumb-wedding",
            "icon": "ti-heart",
            "badge": None,
            "url": None,
        },
        {
            "title": "Birthday Event Film",
            "meta": "EVENT · 6 MIN",
            "thumb_class": "thumb-event",
            "icon": "ti-confetti",
            "badge": None,
            "url": None,
        },
    ],
    "showreel": {
        "title": "Masher — 2024 Showreel",
        "subtitle": "A highlight of my best work across weddings, YouTube & reels.",
        "url": "https://www.instagram.com/reel/DWeEv7cjKpf/?igsh=eHFpdTRwdmpreDNt",
    },
    "tools": [
        "Adobe Premiere Pro",
        "DaVinci Resolve",
        "After Effects",
        "Adobe Audition",
        "Lightroom",
    ],
    # EmailJS config (client-side sending)
    "emailjs": {
        "public_key":  "0HXEuiV0pbDGfqYux",
        "service_id":  "service_avvuf52",
        "template_id": "template_p3cc1sb",
    },
}


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", p=PORTFOLIO)


@app.route("/contact", methods=["POST"])
def contact():
    """
    Optional server-side fallback endpoint.
    The front-end uses EmailJS directly; this route is here if you ever
    want to handle submissions server-side instead.
    """
    data = request.get_json(silent=True) or {}
    name    = data.get("from_name", "").strip()
    email   = data.get("from_email", "").strip()
    message = data.get("message", "").strip()

    if not (name and email and message):
        return jsonify({"ok": False, "error": "All fields are required."}), 400

    # You can swap this for an SMTP call with real credentials:
    # send_email(name, email, message)
    print(f"[contact] From: {name} <{email}>\n{message}\n")
    return jsonify({"ok": True})


def send_email(name, email, body):
    """Server-side SMTP helper (optional). Set env vars to activate."""
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")
    to_addr   = PORTFOLIO["email"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"[Masher] New message from {name}"
    msg["From"]    = smtp_user
    msg["To"]      = to_addr
    msg["Reply-To"] = email

    html = f"""
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Message:</strong><br>{body}</p>
    """
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(smtp_host, smtp_port) as s:
        s.starttls()
        s.login(smtp_user, smtp_pass)
        s.sendmail(smtp_user, to_addr, msg.as_string())


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)
