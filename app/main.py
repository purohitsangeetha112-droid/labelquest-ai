import os, uuid
import cv2
import requests
from flask import Flask, request, jsonify, send_from_directory
from app.parser import parse_label
from app.health_rules import product_score

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "data", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="")

@app.get("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")

@app.post("/upload")
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    f = request.files["image"]
    
    ext = os.path.splitext(f.filename)[1].lower() or ".jpg"
    path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4().hex}{ext}")
    f.save(path)

    try:
        # Zoom in for better OCR
        img = cv2.imread(path)
        if img is not None:
            img = cv2.resize(img, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(path, img)
        
        # CLOUD OCR with isTable=True
        url = "https://api.ocr.space/parse/image"
        with open(path, "rb") as image_file:
            payload = {
                "apikey": "helloworld",
                "language": "eng",
                "isTable": True,
                "scale": True
            }
            files = {"file": image_file}
            response = requests.post(url, data=payload, files=files, timeout=15)
            result = response.json()
            raw = result.get("ParsedResults", [{}])[0].get("ParsedText", "")

        print("\n===== CLOUD OCR TEXT =====")
        print(raw)
        print("==========================\n")

        if len(raw.strip()) < 15:
            return jsonify({"error": "Could not read text. Please take a closer photo."}), 400

        product = parse_label(raw, product_name=f.filename.rsplit(".", 1)[0].upper())
        
        # Trust Check
        n = product["perServing"]
        if n["calories"] == 0 and n["sugar"] == 0 and n["sodium"] == 0 and n["fat"] == 0:
            return jsonify({"error": "Could not find a Nutrition Table. Please upload the BACK of the packet."}), 400

        product["score"] = product_score(product["perServing"])
        return jsonify(product)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        try: os.remove(path)
        except OSError: pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)