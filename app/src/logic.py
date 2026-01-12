import requests
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def trigger_n8n_webhook(payload: dict) -> dict:
    """
    Triggers an n8n webhook with the provided payload.
    
    TODO: Modify this function to fit your specific automation needs.
    You can change the endpoint, headers, or any other logic here.
    """
    webhook_url = os.getenv("N8N_WEBHOOK_URL")
    api_key = os.getenv("N8N_API_KEY")
    
    if not webhook_url:
        logger.error("N8N_WEBHOOK_URL not found in environment variables.")
        return {"error": "Configuration error: Webhook URL missing."}
    
    headers = {
        "Content-Type": "application/json"
    }
    
    # Adding a simple security header if API key is provided
    if api_key:
        headers["X-N8N-API-KEY"] = api_key
        
    try:
        # TODO: Adjust timeout or adding more logic before/after the request
        response = requests.post(webhook_url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        logger.info(f"Successfully triggered n8n webhook. Status: {response.status_code}")
        return response.json() if response.content else {"status": "success"}
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return {"error": f"Automation server returned an error: {response.status_code}"}
    except Exception as err:
        logger.error(f"Other error occurred: {err}")
        return {"error": "The automation server is temporarily unreachable. Please try again later."}

# TODO: Add more automation functions here (e.g., fetch_data, process_logs, etc.)
