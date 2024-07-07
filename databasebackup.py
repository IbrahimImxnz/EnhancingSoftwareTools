import os
import subprocess
import datetime

# Configuration
DB_NAME = 'your_database_name'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'
BACKUP_DIR = '/path/to/backup/directory'

def backup_database():
    # Create a backup directory if it doesn't exist
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # Generate a timestamped filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"{DB_NAME}_backup_{timestamp}.sql"

    # Command to backup the database
    backup_command = f"mysqldump -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {os.path.join(BACKUP_DIR, backup_filename)}"

    try:
        # Execute the backup command
        subprocess.run(backup_command, shell=True, check=True)
        print(f"Backup successful: {backup_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    backup_database()
