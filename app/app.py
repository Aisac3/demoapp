#!/usr/bin/env python3

import os
import sys
import time
from datetime import datetime


def log(message, level="INFO"):
    """Simple logger to stdout"""
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] [{level}] {message}", flush=True)


def main():
    log("Python application starting...")

    # Read environment variable to simulate failure
    # FAIL_APP=true will force the app to fail
    fail_flag = os.getenv("FAIL_APP", "false").lower()

    log(f"FAIL_APP flag value: {fail_flag}")

    # Simulate some work
    log("Performing application task...")
    time.sleep(2)

    if fail_flag == "true":
        log("Simulated failure triggered!", level="ERROR")
        log("Application exiting with code 1", level="ERROR")
        sys.exit(1)   #  failure (important for CI/CD)

    log("Application completed successfully")
    log("Application exiting with code 0")
    sys.exit(0)       # success


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"Unhandled exception: {e}", level="ERROR")
        sys.exit(2)
