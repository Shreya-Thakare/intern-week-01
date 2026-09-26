import subprocess
import sys
import time
from pathlib import Path


def test_main_starts_uvicorn_server():
    project_dir = Path(__file__).resolve().parent
    process = subprocess.Popen(
        [sys.executable, "main.py"],
        cwd=project_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    try:
        deadline = time.time() + 10
        output = ""

        while time.time() < deadline:
            if process.poll() is not None:
                break
            time.sleep(0.25)
            if process.stdout is not None:
                chunk = process.stdout.readline()
                if chunk:
                    output += chunk
                    if "Uvicorn running on" in output:
                        break

        assert "Uvicorn running on" in output, (
            "Expected FastAPI startup logs from uvicorn, but the backend never started."
        )
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
