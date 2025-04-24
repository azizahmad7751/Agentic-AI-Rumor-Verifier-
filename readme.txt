# 🕵️‍♂️ Agentic AI Rumor Verifier

A powerful LLM-based Agent that verifies social media rumors in real-time using trusted sources like Wikipedia, DuckDuckGo, and Snopes.

> ✅ Built with **LangChain**, **Groq's LLaMA 3.3-70B**, and **Gradio**

## 🚀 Live Demo

Try it here: [Agentic AI Rumor Verifier](https://2d0c4343b44eeaa1fe.gradio.live/)

## 📸 Preview

![demo-screenshot](demo.gif) <!-- Replace with your own image or GIF preview -->

---

## 🛠️ Features

- 🔍 Verifies claims using live web search
- ✅ Verdicts: **TRUE**, **FALSE**, or **UNVERIFIED**
- 🧠 Explains the decision with references
- ⚡ Powered by Groq's ultra-fast LLaMA 3.3 70B model
- 🌐 Clean, simple Gradio web interface

---

## 🧱 Tech Stack

| Tool       | Purpose                             |
|------------|-------------------------------------|
| LangChain  | Agent orchestration & tool loading  |
| Groq       | LLaMA 3.3-70B LLM API               |
| Gradio     | Frontend interface                  |
| Python     | Core application logic              |

---

## 🧪 Sample Rumors to Test

Paste these into the app:

- `"NASA just announced they found signs of life on Mars in 2025 mission!"`
- `"Drinking cold water after meals causes cancer."`
- `"Wearing red on Fridays makes you invisible to AI cameras."`

---

## ⚙️ Installation

1. Clone the repo:

```bash
https://github.com/azizahmad7751/Agentic-AI-Rumor-Verifier-.git

2. Install dependencies:

```bash
pip install -r requirements.txt

Run the app:

```bash
python app.py
⚠️ Make sure you have a valid Groq API key and update it inside the code.

🔐 Environment Variables
You can set your API key in a .env file: env

GROQ_API_KEY=your_groq_key_here
Or hardcode it inside the Python file (not recommended for production).

🤝 Contributions
Pull requests are welcome! Feel free to fork, experiment, and suggest new tools (e.g., NewsAPI, Twitter, etc.).

