def enrich_with_geoip(log_entry):
    """
    Enrichit une entrée de log avec des informations géographiques basées sur l'adresse IP.

    Args:
        log_entry (dict): L'entrée de log à enrichir, contenant une clé 'ip_address'.

    Returns:
        dict: L'entrée de log enrichie avec des informations géographiques.
    """
    import geoip2.database

    # Chemin vers la base de données GeoIP
    geoip_database_path = '/path/to/GeoLite2-City.mmdb'
    
    # Initialiser le lecteur de base de données GeoIP
    reader = geoip2.database.Reader(geoip_database_path)

    ip_address = log_entry.get('ip_address')
    if ip_address:
        try:
            response = reader.city(ip_address)
            log_entry['geoip'] = {
                'country': response.country.name,
                'region': response.subdivisions.most_specific.name,
                'city': response.city.name,
                'latitude': response.location.latitude,
                'longitude': response.location.longitude
            }
        except Exception as e:
            log_entry['geoip'] = {'error': str(e)}
    
    return log_entry