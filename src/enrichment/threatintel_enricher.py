from typing import Dict, Any
import requests

def enrich_with_threatintel(log: Dict[str, Any]) -> Dict[str, Any]:
    """
    Enriches the given log with threat intelligence data.

    Args:
        log (Dict[str, Any]): The log entry to enrich.

    Returns:
        Dict[str, Any]: The enriched log entry with threat intelligence data.
    """
    threat_intel_api_url = "https://api.threatintel.example.com/enrich"
    
    try:
        response = requests.post(threat_intel_api_url, json=log)
        response.raise_for_status()
        threat_data = response.json()
        
        # Merge threat intelligence data into the log
        log.update(threat_data)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching threat intelligence: {e}")
    
    return log