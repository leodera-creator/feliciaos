import schedule
import time
import subprocess
import os

BRAIN = os.path.expanduser("~/feliciaos/felicia_brain.py")
PYTHON = os.path.expanduser("~/feliciaos/felicia_env/bin/python3")

def run_layer(layer):
    print(f"\n⏰ Auto-running: {layer}")
    subprocess.run([PYTHON, BRAIN, "--layer", layer])

# Every 4 hours — market scan
schedule.every(4).hours.do(run_layer, "market_scan")

# Every 6 hours — confession
schedule.every(6).hours.do(run_layer, "confession")

# Every 12 hours — community audit
schedule.every(12).hours.do(run_layer, "community_audit")

# Daily at 9AM — narrative thread
schedule.every().day.at("09:00").do(run_layer, "narrative")

# Daily at 7PM — DeFi education
schedule.every().day.at("19:00").do(run_layer, "defi_education")

print("⚡ FeliciaOS Scheduler Active — Running 24/7")
print("Press Ctrl+C to stop\n")

while True:
    schedule.run_pending()
    time.sleep(60)
