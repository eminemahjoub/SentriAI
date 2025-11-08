def parse_json_log(json_log):
    """
    Normalizes JSON logs into a unified format.

    Args:
        json_log (dict): The JSON log to normalize.

    Returns:
        dict: A normalized JSON log.
    """
    # Example normalization process
    normalized_log = {
        "timestamp": json_log.get("timestamp"),
        "level": json_log.get("level", "INFO"),
        "message": json_log.get("message", ""),
        "source": json_log.get("source", "unknown"),
        "additional_info": json_log.get("additional_info", {})
    }
    
    return normalized_log