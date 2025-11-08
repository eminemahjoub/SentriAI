#!/bin/bash

# Script to backup log archives

# Define backup directory
BACKUP_DIR="/path/to/backup/directory"
# Define log directory
LOG_DIR="/path/to/log/directory"
# Define date format for backup
DATE=$(date +"%Y%m%d_%H%M%S")

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create a tarball of the log directory
tar -czf "$BACKUP_DIR/log_backup_$DATE.tar.gz" -C "$LOG_DIR" .

# Print completion message
echo "Backup of logs completed successfully at $BACKUP_DIR/log_backup_$DATE.tar.gz"