import requests

def extract_text(image_path: str) -> str:
    # We use the free OCR.space API (Engine 2 is best for tables)
    url = "https://api.ocr.space/parse/image"
    
    with open(image_path, "rb") as image_file:
        payload = {
            "apikey": "helloworld", # Free public test key
            "language": "eng",
            "isOverlayRequired": False,
            "scale": True,
            "OCREngine": 2 
        }
        files = {"file": image_file}
        
        try:
            # Send image to the cloud
            response = requests.post(url, data=payload, files=files, timeout=15)
            result = response.json()
            
            # If it failed, return nothing
            if result.get("IsErroredOnProcessing"):
                return ""
                
            # Return the text!
            return result.get("ParsedResults", [{}])[0].get("ParsedText", "")
            
        except Exception as e:
            print("Cloud OCR Error:", e)
            return ""