#!/bin/bash

# Remote server details
REMOTE_USER=""
REMOTE_HOST=""
REMOTE_FILE="log.csv"

LOCAL_DIR=""

scp "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_FILE}" "${LOCAL_DIR}/"

