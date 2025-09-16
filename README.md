# Text-Extraction-and-Automation
This project provides an **API for extracting structured entities from raw text**.  
It uses **FastAPI** as the backend framework and **Gemini API** for information extraction.  

---

## 🚀 Features
- Extracts structured entities such as:
  - `persons`
  - `dates`
  - `organizations`
  - `locations`
  - `events`
  - `emails`
  - `phone_numbers`
  - `urls`
  - `titles`
  - `addresses`
  - `others`
- Ensures minimum output always contains `"persons"` and `"dates"` (even if empty).
- Returns only **valid JSON**.

---

## 1️⃣ Setup Instructions

### Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```
### Install dependencies
pip install -r requirements.txt

### Add environment variables

- Create a .env file in the root folder:
GEMINI_API_KEY=your_api_key_here

## 2️⃣ Running the API

Run the FastAPI app with uvicorn:
uvicorn main:app --reload --host 0.0.0.0 --port 8000

- If you’re running locally but need an external/public URL (for automation tools like n8n), use localtunnel:
-- npx localtunnel --port 8000

- This will give you a public URL like:
https://your-app.loca.lt/extract

## 3️⃣ API Usage
- Endpoint
- POST /extract

- Request Body
{
  "text": "Barack Obama was born on August 4, 1961 in Honolulu. He served as the President of the United States."
}

- Example Response
{
  "persons": ["Barack Obama"],
  "dates": ["August 4, 1961"],
  "organizations": ["United States"],
  "locations": ["Honolulu"],
  "events": [],
  "emails": [],
  "phone_numbers": [],
  "urls": [],
  "titles": ["President"],
  "addresses": [],
  "others": []
}

## 4️⃣ n8n Integration

- You can automate text extraction and save results to Google Sheets using n8n

- Steps:
- Open your n8n dashboard.
- Create a new workflow with these nodes:
- File > Raw → add text inputs.
- HTTP Request → configure it to call your /extract endpoint (use the public LocalTunnel URL).
- Google Sheets → save the extracted entities.
- Add the public URL credentials from LocalTunnel in the HTTP request node.
- Run the workflow — your text gets processed, and structured data lands in Google Sheets 🎉.
