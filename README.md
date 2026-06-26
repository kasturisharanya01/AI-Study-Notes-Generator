# 📚 SmartStudy AI

An AI-powered Study Notes Generator built using **Python**, **Streamlit**, and **Google Gemini 2.5 Flash**. The application helps students quickly summarize study materials, generate quiz questions, create flashcards, estimate study time, and download AI-generated notes as a PDF.

---

## 🚀 Features

- 📄 Upload PDF study notes
- ✍️ Paste notes manually
- 🤖 AI-generated detailed summary
- 📌 Key points extraction
- ❓ Important exam questions
- 🎯 Difficulty-based quiz generation (Easy, Medium, Hard)
- 📝 Flashcard generator
- ⏰ Study time estimation
- 📥 Download generated results as PDF
- 🎨 Modern and responsive Streamlit user interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash API
- PyPDF2
- FPDF

---

## 📂 Project Structure

```
SmartStudy-AI/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/ (optional)
```

---

## 📦 Required Libraries

Install the required libraries using:

```bash
pip install streamlit google-generativeai PyPDF2 fpdf
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Setup

1. Visit Google AI Studio.
2. Create a Gemini API key.
3. Open `app.py`.
4. Replace:

```python
genai.configure(api_key="YOUR_API_KEY")
```

with your own API key.

> **Note:** Do not share your API key publicly.

---

## ▶️ Run the Project

Open the terminal inside the project folder and run:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 📖 How to Use

1. Launch the application.
2. Upload a PDF or paste your study notes.
3. Select the quiz difficulty.
4. Choose one of the available options:
   - Generate Notes
   - Generate Flashcards
   - Estimate Study Time
5. View the AI-generated content.
6. Download the results as a PDF if needed.

---

## 🎯 Project Workflow

```
User Input
      │
      ▼
Upload PDF / Paste Notes
      │
      ▼
Google Gemini AI
      │
      ▼
Generate:
 • Summary
 • Key Points
 • Exam Questions
 • Quiz Questions
 • Flashcards
 • Study Time
      │
      ▼
Display Results
      │
      ▼
Download PDF
```

---

## 💡 Applications

- Student learning assistant
- Exam preparation
- Quick revision
- Self-assessment
- AI-powered study companion

---

## 📸 Features Demonstrated

- PDF Upload
- AI Summary Generation
- Key Point Extraction
- Exam Question Generation
- Difficulty-Based Quiz Generation
- Flashcard Generation
- Study Time Estimation
- PDF Export
- Responsive User Interface

---

## 🔮 Future Enhancements

- Voice input
- OCR support for scanned PDFs
- Multi-language support
- User authentication
- History of generated notes
- Dark mode
- MCQ scoring system
- Speech-to-text integration

---

## 👨‍💻 Author

**Kasturi Sharanya**

AI-Powered Study Notes Generator using Google Gemini 2.5 Flash.

---

## 📄 License

This project is developed for educational purposes. Feel free to modify and extend it for learning and academic use.