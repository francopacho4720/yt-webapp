from flask import Flask, request
import subprocess, os

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return {"error": "falta el parámetro url"}, 400
    result = subprocess.run(
        ["/usr/local/bin/yt-dlp", "-o", "/downloads/%(title)s.%(ext)s", url],
        capture_output=True, text=True
    )
    return {"stdout": result.stdout, "stderr": result.stderr}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)