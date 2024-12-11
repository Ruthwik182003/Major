from flask import Flask, render_template, jsonify
from config import LOG_FILE
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    """Render the dashboard page."""
    return render_template("dashboard.html")


@app.route("/logs", methods=["GET"])
def get_logs():
    """Fetch the latest logs."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as log_file:
            logs = log_file.readlines()
        return jsonify({"logs": logs[::-1]})  # Reverse logs for recent first
    return jsonify({"error": "Log file not found"}), 404


@app.route("/alerts", methods=["GET"])
def get_alerts():
    """Fetch system alerts (filtered logs)."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as log_file:
            alerts = [line for line in log_file.readlines() if "WARNING" in line or "ERROR" in line]
        return jsonify({"alerts": alerts[::-1]})
    return jsonify({"error": "Log file not found"}), 404