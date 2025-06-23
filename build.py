import os
import subprocess

os.makedirs("build", exist_ok=True)

# Build with emcc
subprocess.run(
    'emcc main.cpp -s USE_WEBGL2=1 -s FULL_ES3=1 -s EXPORTED_RUNTIME_METHODS=\'["requestFullscreen"]\' -o build/index.html',
    shell=True,
    check=True
)

# Start emrun dev server
subprocess.run(
    'emrun --no_browser --port 8080 build',
    shell=True,
    check=True
)
