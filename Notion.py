import os
import json
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Your Notion API Token
NOTION_API_TOKEN = "secret_2sJc3jBgpm1Wps9aDx8mvKon5QtdVjOhaC9wIkQozzk"

# Your Notion Database ID
NOTION_DATABASE_ID = "f184a448f3984a2f9dd7aa89b54eaf6b"

# Notion API Endpoint
NOTION_API_ENDPOINT = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"

@app.route("/")
def index():
    # Fetch data from the Notion database
    headers = {
        "Authorization": f"Bearer {NOTION_API_TOKEN}",
        "Notion-Version": "2021-08-16",  # Check for the latest version
    }
    response = requests.post(NOTION_API_ENDPOINT, headers=headers)
    data = response.json().get("results", [])

    return render_template("index.html", data=data)

@app.route("/add_entry", methods=["POST"])
def add_entry():
    # Get data from the form
    title = request.form["title"]
    content = request.form["content"]

    # Create a new entry in the Notion database
    headers = {
        "Authorization": f"Bearer {NOTION_DATABASE_ID}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16",
    }
    data = {
        "parent": {
            "database_id": "f184a448f3984a2f9dd7aa89b54eaf6b"
        },
        "properties": {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "Content": {
                "rich_text": [
                    {
                        "text": {
                            "content": content
                        }
                    }
                ]
            }
        }
    }
    response = requests.post(NOTION_API_ENDPOINT, headers=headers, json=data)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
