<div align="center">

# 🕵️‍♀️ LabelQuest
### **Scan. Learn. Choose Smart.**

*An AI-powered, gamified food-label awareness platform that decodes complex nutrition tables, exposes hidden sugars/salts, and teaches healthier choices through an interactive 100-level educational game.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![EasyOCR](https://img.shields.io/badge/EasyOCR-AI-red?style=for-the-badge)](https://github.com/JaidedAI/EasyOCR)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.10-green?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-yellow?style=for-the-badge&logo=javascript)](https://developer.mozilla.org/)

</div>

---

## 📖 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [The Problem & Market Research](#-the-problem--market-research)
3. [Our Unique Solution](#-our-unique-solution)
4. [Key Features](#-key-features)
5. [System Architecture & Workflow](#-system-architecture--workflow)
6. [Evidence](#-evidence)
7. [Tech Stack](#-tech-stack)
8. [Project Directory Structure](#-project-directory-structure)
9. [How to Run Locally](#-how-to-run-locally)
10. [Future Scope & Roadmap](#-future-scope--roadmap)
11. [Medical Disclaimer](#-medical-disclaimer)
12. [Conclusion](#-conclusion)

---

## 🌟 Executive Summary

In India, packaged foods are ubiquitous. While the FSSAI mandates strict labeling rules for serving sizes, nutrition, and ingredients, **research proves that the average consumer—especially children—cannot understand or use this information.** 

Existing apps mostly scan barcodes and output a single score. **LabelQuest goes several steps further.** We use OCR (Optical Character Recognition) to read the back of the packet, perform a **"Serving-Size Reality Check"** (e.g., highlighting that a pack with 3 servings means 3x the sugar), and wrap this health data in a **100-Level Gamified Dashboard** to teach children and adults how to read labels for life.

---

## 🚨 The Problem & Market Research

The core issue isn't a lack of information on food packets; it is a **lack of comprehension**. 

### What the Research Proves:
| Research / Source | What it proves for LabelQuest |
| :--- | :--- |
| **Food labelling review in India** | FSSAI has mandatory labelling rules, but Indian consumers have limited awareness, understanding, and use of label information. |
| **Kochi urban consumer study** | Mean food-label literacy was low; **60.4%** of participants scored 4 or below, showing many cannot properly use label details. |
| **Packaged-food purchase study** | Only about **one-fourth** of participants read food labels; rural consumers have even lower usage. |
| **Food Safety Works survey** | Only **23%** of participants *always* checked nutrition facts; 48% checked only sometimes. |
| **Low-literacy front-of-pack label study** | Nutrition literacy is low, especially among people with lower education. Users explicitly requested simpler, clearer labels. |
| **FSSAI labelling regulations** | Nutrition panels must include serving size, number of servings, and quantity in grams—this is exactly what our app explains. |
| **FoodLabel OCR research** | Proves that OCR/LLM methods can successfully extract nutrition values from phone photos. |

### The "Serving Size" Trap
A packet of biscuits might proudly display *"Per serving: 12g sugar"*. But the packet contains **3 servings**. If a user eats the whole packet, they consume **36g of sugar** (nearly 9 teaspoons). Without a translator, the average consumer is blind to this risk.

---

## 💡 Our Unique Solution

**LabelQuest is not just a scanner; it is an educational platform.** 

1. **The Scanner:** Users take a photo of the nutrition table. Our AI extracts the text, identifies Calories, Sugar, Sodium, Fat, and Allergens, and grades the product as **Green (Safe), Yellow (Moderate), or Red (High Concern)**.
2. **The Reality Check:** The app explicitly calculates total sugar/salt if the whole pack is eaten.
3. **The Game Center:** We solved the engagement problem. Kids don't want to read tables. But they *do* want to beat the "SnackBot" in a trivia battle to unlock "World 2: Salt Guardian." The game teaches nutrition concepts indirectly.

---

## 🎮 Key Features

### 1. Real-Time AI Label Scanner
- Upload an image of any nutrition label.
- OpenCV pre-processes the image (upscaling and sharpening) to ensure readability.
- EasyOCR extracts the raw text, and a custom Python Regex Parser extracts the exact grams/mg of Sugar, Salt, and Fat.

### 2. Dynamic Health Warnings & Profiles
- **Child vs. Adult View:** Toggle between profiles. Kids get advice like *"Eating this much fat affects growth,"* while adults get *"High sodium raises blood pressure."*
- **Smart Swaps:** If a product is high in sugar/salt, the app dynamically suggests 5 specific alternatives (e.g., swapping Cola for Coconut Water).

### 3. Gamified 100-Level Dashboard
- **5 Worlds:** Sugar Detective, Salt Guardian, Fat Inspector, Ingredient Decoder, Allergen Hero.
- **100 Unique Levels:** Users must win battles to unlock the next level.
- **Bot Battles:** Player vs. Bot (SnackBot) where answering nutrition questions correctly deals damage to the bot.
- **XP, Coins, and Stars:** A complete progression system to keep users engaged.

### 4. Live Global Leaderboard
- A simulated multiplayer environment with **100+ active bots**.
- Bots earn XP and level up in real-time. A live activity feed shows what other users are doing (e.g., *"HealthNinja defeated Level 12!"*), creating a sense of a massive, active community.

### 5. 365 Daily Nutrition Quotes
- A built-in database of 365 health and nutrition quotes. The app calculates the day of the year and displays a new quote every single day on the dashboard.

---

## 🛠️ System Architecture & Workflow

1. **User Uploads Image** ➔ Frontend sends `multipart/form-data` to the Flask API.
2. **Image Processing** ➔ OpenCV upscales the image 2.5x and applies a sharpening matrix to make the text pop.
3. **OCR Extraction** ➔ EasyOCR scans the image and returns a block of raw text.
4. **Smart Parsing** ➔ `parser.py` reads the text line-by-line, ignoring bilingual words (e.g., "Sucres") and finding the nearest number to "Sugar", "Sodium", etc.
5. **Scoring Engine** ➔ `health_rules.py` applies strict WHO thresholds (e.g., Sodium > 300mg = Red) and returns the final score.
6. **Frontend Rendering** ➔ The result is displayed in a modern, dark-mode UI with animations and specific health swaps.

---
## 💻 EVIDENCE
<img width="1920" height="1020" alt="Screenshot 2026-10-23 194251" src="https://github.com/user-attachments/assets/9217796a-3cbf-45df-8a1b-518f4b0619ed" />
<img width="1920" height="1020" alt="Screenshot 2026-10-23 194211" src="https://github.com/user-attachments/assets/8b6ad743-1b6e-430d-bb29-97f06f2c6c85" />
<img width="1920" height="1020" alt="Screenshot 2026-10-23 194310" src="https://github.com/user-attachments/assets/e9f8ddd3-ba8e-49e7-a67c-210167c92361" />
<img width="1920" height="1020" alt="Screenshot 2026-10-23 194220" src="https://github.com/user-attachments/assets/3cb52583-3d62-4eda-b5a4-71e40864802b" />
<img width="1920" height="1020" alt="Screenshot 2026-10-23 194224" src="https://github.com/user-attachments/assets/d66455e1-ccfb-4dd6-9221-d340a3abc000" />
<img width="1920" height="1020" alt="Screenshot 2026-10-23 194228" src="https://github.com/user-attachments/assets/c8e2db5b-e3e4-4ec8-9017-1c1d13b9186a" />

## 💻 Tech Stack

<table>
  <tr>
    <td align="center"><b>Frontend</b></td>
    <td>HTML5, CSS3, Vanilla JavaScript (Single Page Application, LocalStorage for Game State)</td>
  </tr>
  <tr>
    <td align="center"><b>Backend</b></td>
    <td>Python 3, Flask</td>
  </tr>
  <tr>
    <td align="center"><b>AI / ML</b></td>
    <td>EasyOCR, PyTorch, OpenCV (Image Processing)</td>
  </tr>
  <tr>
    <td align="center"><b>Design</b></td>
    <td>Custom Dark Mode UI, Glassmorphism, CSS Animations, Confetti.js</td>
  </tr>
</table>

---

## 📁 Project Directory Structure

```text
labelquest/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Flask server & API routes
│   ├── ocr.py               # EasyOCR & Image extraction
│   ├── parser.py            # Regex extraction of nutrition
│   ├── health_rules.py      # Threshold scoring (Red/Yellow/Green)
│   └── static/
│       └── index.html       # Full frontend (Scanner + 100 Level Game)
│
├── data/
│   └── uploads/             # Temporary folder for uploaded images
│
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignores venv and temp files
└── README.md                # This file

## 🌑 How to Run Locally

Follow these steps to run **LabelQuest** on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/purohitsangeetha112-droid/labelquest-ai.git
cd labelquest-ai
```

### 2. Create and Activate a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** On the first launch, EasyOCR may download approximately 100 MB of AI models. This is expected behavior and may take a few minutes, depending on your internet connection.

### 4. Start the Flask Application

```bash
python -m app.main
```

### 5. Open LabelQuest

Open your browser and visit:

**http://127.0.0.1:5000**

You're ready to explore LabelQuest! 🚀

---

## 🔮 Future Scope & Roadmap

* [ ] **Multilingual Support** — Introduce Hindi, Tamil, and Telugu translations to improve accessibility for users across India.
* [ ] **Barcode Scanning** — Integrate the Open Food Facts API to enable quick product lookups.
* [ ] **School & Teacher Mode** — Develop a dedicated dashboard for teachers to create quizzes and track student progress, supporting the goals of the FSSAI Eat Right School initiative.
* [ ] **Cloud Database** — Migrate browser-based LocalStorage data to a secure PostgreSQL database for persistent, cross-device leaderboard synchronization.
* [ ] **Advanced Machine Learning** — Explore models for identifying and explaining specific food additives, such as INS 621 (monosodium glutamate), from ingredient lists.

---

## ⚠️ Medical Disclaimer

LabelQuest is an educational and nutritional awareness tool designed to help users better understand packaged food labels. It provides general information intended for educational purposes and is not a substitute for professional medical advice, diagnosis, or treatment.

Nutritional information and interpretations may vary depending on the product, serving size, and applicable labeling standards. Always consult a qualified healthcare professional for personalized dietary or health-related decisions.

---

## 🏁 Conclusion

**LabelQuest is more than a food-label scanner — it is an interactive platform designed to make nutritional literacy accessible, engaging, and practical.**

The project addresses a real-world challenge: understanding the nutritional information printed on packaged foods. Serving sizes, added sugars, sodium levels, and unfamiliar ingredients can make informed food choices difficult, particularly for younger consumers.

LabelQuest bridges this gap through three core capabilities:

* **🤖 AI-Powered Label Analysis:** Uses OpenCV and EasyOCR to extract nutritional information from food-label images and present it through an easy-to-understand Green, Yellow, and Red classification system.
* **🔍 The Reality Check:** Helps users understand the difference between a stated serving size and the entire package, making total nutritional intake easier to interpret.
* **🎮 Gamified Nutrition Education:** Makes learning interactive through a 100-level, bot-battling game experience that encourages users to explore topics such as sodium and hidden sugars.

Built with a Python and Flask backend alongside a responsive Vanilla JavaScript frontend, LabelQuest combines image processing, nutritional awareness, and interactive learning in one application.

With features such as child-versus-adult guidance, healthier food alternatives, and daily nutrition quotes, the platform aims to encourage users to think more critically about their food choices.

**Our vision is simple: turn complicated food labels into clearer information, and turn nutritional awareness into a daily habit.**

---

<div align="center">

### ❤️ Built with a vision for a healthier, smarter generation.

**LabelQuest — Scan. Understand. Learn. Choose Better.**

</div>

Why LabelQuest Wins:

It is technically advanced, but more importantly, it is socially impactful. It aligns directly with FSSAI's "Eat Right" initiative and the UN's Sustainable Development Goal 3 (Good Health and Well-Being).
We do not just tell users what is inside the packet—we teach them how to understand it.

"LabelQuest: Scan. Learn. Choose Smart. Building a healthier, smarter, and more informed generation, one label at a time."
