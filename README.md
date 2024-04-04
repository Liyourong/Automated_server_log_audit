# Automated Log Audit Service

This repository contains a set of scripts designed to automate the process of fetching log files from a remote server, performing an audit on these logs, and generating a report based on the audit findings. The service primarily targets operations that may be non-compliant or suspicious. This is an automated service I developed in CMPay

## Overview
- `fetch_log.sh`: A bash script to securely copy a log file from a remote server to a local directory.
- `pre_fetch_setup.sh`: A bash script to ensure another script is executable, typically used before `fetch_log.sh`.
- `audit.py`: A Python script that performs the actual audit on the fetched log, identifying non-compliant or suspicious activities.

## How to Use

### Setup

1. Ensure you have `bash` and `Python` (with `pandas` library) installed on your system.
2. Clone this repository to your local machine.

### Making Scripts Executable

Run the `pre_fetch_setup.sh` script to make `fetch_log.sh` executable:

```bash
./pre_fetch_setup.sh
```

### Fetch the log from remote

Run the `fetch_log.sh` script

```bash
./fetch_log.sh
```

### Performing Audit
Before running the audit, ensure you have the necessary CSV files (sudo_apply.csv, iwc_apply.csv) in the same directory as audit.py, or adjust the paths in the script accordingly.

Run the audit with:
```bash
python audit.py
```

## What it Does
- `fetch_log.sh`: Fetches log.csv from a specified remote server using SSH and saves it to a local directory.
- `pre_fetch_setup.sh`: Sets execute permission on fetch_log.sh or any specified script.
- `audit.py`: Analyzes log.csv for compliance with sudo application windows, identifies suspicious SQL and SSH operations, and checks for compliance with IWC application windows. The results are output to CSV files for further review.


## Requirements
- `Bash`
- `Python 3`
- `Pandas library for Python`

## NDA
Due to the non-disclosure reasons, the original service source code is desensitied, replacing the key-words with non-relevant names. However, the source code in this repo remain fully functional
