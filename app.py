import os
import json
from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()

class TextInput(BaseModel):
    text: str
    
@app.post("/extract")
async def extract_entities(input: TextInput):
    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = f"""
    You are an information extraction system.  
    Analyze the following text and extract structured details.  

    Extract as many categories as possible, such as:  
    - persons (individual names)  
    - dates (any format)  
    - organizations  
    - locations  
    - events  
    - emails  
    - phone_numbers  
    - URLs  
    - titles/roles  
    - addresses  
    - other entities that may be relevant  

    ⚠️ Minimum requirement: always include "persons" and "dates" even if empty.  

    Return ONLY valid JSON (no explanations, no markdown).  
    If a field has no values, return an empty list.  

    Format it like this:
    {
    "persons": [],
    "dates": [],
    "organizations": [],
    "locations": [],
    "events": [],
    "emails": [],
    "phone_numbers": [],
    "urls": [],
    "titles": [],
    "addresses": [],
    "others": []
    }

    Text:
    {input.text}
    """
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    )

    structureop = response.text.strip()

    # Cleanup: remove triple backticks if they exist
    if structureop.startswith("```json"):
        structureop = structureop.replace("```json", "").strip()
    if structureop.endswith("```"):
        structureop = structureop[:-3].strip()

    print("Gemini raw output:\n", structureop)

    try:
        final_op = json.loads(structureop)
        return final_op
    except Exception as e:
        print("Failed to parse tags from Gemini:", e)
        return {}