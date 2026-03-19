# Rclone Download Script

A simple Python wrapper script to download files or folders from a configured `rclone` remote to a local directory. This script handles password-protected rclone configurations and is well-suited for retrieving backups (e.g., in environments like Termux).

## Prerequisites

- Python 3
- `rclone` installed and configured on your system.

## Configuration

The script optionally reads from a `config.json` file in the same directory to securely load your rclone password and remote path.

Create a `config.json` file with the following structure:

```json
{
  "RCLONE_CONFIG_PASS": "your_rclone_config_password",
  "RCLONE_REMOTE": "gdrive:/MyTermuxBackups/"
}
```

_Note: If `config.json` is not provided, the script defaults to `gdrive:/MyTermuxBackups/` as the remote and assumes no rclone configuration password is required._

## Usage

Run the script by passing the target local destination path as an argument. The script automatically expands user paths (such as `~/`).

```bash
python main.py ~/storage/shared/Download/RestoreFolder
```
