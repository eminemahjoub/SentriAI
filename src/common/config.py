from pydantic import BaseSettings

class Settings(BaseSettings):
    # General configuration
    app_name: str = "SIEM Platform"
    app_version: str = "1.0.0"
    
    # Logging configuration
    log_level: str = "INFO"
    log_file: str = "logs/app.log"
    
    # Database configuration
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "siem_user"
    db_password: str = "siem_password"
    db_name: str = "siem_db"
    
    # Elasticsearch configuration
    es_host: str = "localhost"
    es_port: int = 9200
    
    # Alerting configuration
    alert_email: str = "alerts@siemplatform.com"
    alert_slack_webhook: str = ""
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()