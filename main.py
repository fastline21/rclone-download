import sys
import os
import json
import subprocess
from pathlib import Path

# --- LOAD NATIVE JSON CONFIG ---
CONFIG_FILE = Path("config.json")
RCLONE_PASS = ""
RCLONE_REMOTE = "gdrive:/MyTermuxBackups/"

if CONFIG_FILE.exists():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)
        RCLONE_PASS = config_data.get("RCLONE_CONFIG_PASS", "")
        RCLONE_REMOTE = config_data.get("RCLONE_REMOTE", RCLONE_REMOTE)
# -------------------------------

def download_from_drive(local_destination):
    # Use .expanduser() so ~/storage works!
    dest = Path(local_destination).expanduser().resolve()
    
    # Create the folder if it doesn't exist
    dest.mkdir(parents=True, exist_ok=True)

    print(f"Downloading from: {RCLONE_REMOTE}")
    print(f"To local path: {dest}")

    env = os.environ.copy()
    if RCLONE_PASS:
        env["RCLONE_CONFIG_PASS"] = RCLONE_PASS 
    
    # Note the order: Remote comes FIRST for download
    download_cmd = [
        "rclone", "copy", 
        RCLONE_REMOTE, 
        str(dest), 
        "-P",
        "--retries", "5"
    ]
    
    try:
        subprocess.run(download_cmd, env=env, check=True)
        print("-" * 40)
        print("Download successfully completed!")
    except subprocess.CalledProcessError:
        print("-" * 40)
        print("Error: Download failed. Check your connection or config.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download.py ~/storage/shared/Download/RestoreFolder")
        sys.exit(1)
        
    download_from_drive(sys.argv[1])

