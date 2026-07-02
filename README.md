<div align="center">

<img src="Assets/logo.png" alt="ReviewGPT Logo" width="120"/>

# 🛍️ ReviewGPT

**AI-Powered Product Review Analyzer for Smarter Purchasing Decisions**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-green.svg)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Overview](#-overview) • [Features](#-features) • [Architecture](#️-architecture) • [Installation](#️-installation) • [Usage](#️-usage) • [Roadmap](#-roadmap)

</div>

---

## 📖 Overview

**ReviewGPT** helps online shoppers cut through review overload. Paste a product URL, and ReviewGPT scrapes customer reviews and ratings, then uses an LLM pipeline (LangChain + Hugging Face) to distill everything into a concise report — key strengths, common complaints, and a clear buying recommendation — all through a clean Streamlit interface.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🔗 URL-based analysis | Analyze any supported product directly from its URL |
| 🌐 Web scraping | Extracts reviews and product data using BeautifulSoup |
| 📦 Product metadata | Pulls product image, title, and details |
| ⭐ Rating aggregation | Collects and summarizes customer ratings |
| 📝 Review extraction | Gathers raw customer review text at scale |
| 🤖 AI summarization | LangChain + Hugging Face LLM pipeline for review synthesis |
| 👍 Strength detection | Surfaces the most praised product attributes |
| 👎 Complaint detection | Highlights recurring customer pain points |
| 💡 Buying recommendation | Generates an overall verdict backed by review evidence |
| 🎨 Interactive UI | Clean, responsive Streamlit front end |

---

## 🏗️ Architecture

```text
                    Product URL
                         │
                         ▼
             Web Scraper (BeautifulSoup)
                         │
                         ▼
              Extract Product & Reviews
                         │
                         ▼
            Clean & Preprocess Review Data
                         │
                         ▼
          LangChain Pipeline + Hugging Face LLM
                         │
                         ▼
             AI-Generated Product Report
                         │
                         ▼
              Streamlit Results Dashboard
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Scraping | BeautifulSoup4, Requests |
| Data Processing | Pandas |
| LLM Orchestration | LangChain |
| Inference | Hugging Face Inference API |
| Config | python-dotenv |

---

## 📁 Project Structure

```text
ReviewGPT/
│
├── Assets/
│   └── logo.png              # Project logo
│
├── app.py                    # Streamlit entry point
├── scraper.py                # Review & product scraping logic
├── llm_analysis.py           # LangChain + HF summarization pipeline
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ReviewGPT.git
```

### 2. Navigate to the project directory
```bash
cd ReviewGPT
```

### 3. Create a virtual environment
```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Linux/macOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 5. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
HUGGINGFACE_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file. It's already excluded via `.gitignore`.

---

## ▶️ Usage

Launch the app:
```bash
streamlit run app.py
```

Then, in the browser window that opens:
1. Paste a product URL into the input field
2. Click **Analyze**
3. Review the AI-generated summary — strengths, complaints, ratings snapshot, and final recommendation

---

## 📸 Demo

> Add screenshots or a GIF of the application here.

---

## 🔮 Roadmap

- [ ] Aspect-based sentiment analysis
- [ ] Multi-product comparison view
- [ ] Interactive visualizations (rating distribution, sentiment trends)
- [ ] Export reports as PDF
- [ ] RAG-powered Q&A over review data
- [ ] Support for multiple e-commerce platforms

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/yourusername/ReviewGPT/issues) or open a pull request.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Darsh Chouhan**
B.Tech – Data Science & AI, IIIT Dharwad
[GitHub](https://github.com/yourusername) • [LinkedIn](https://linkedin.com/in/yourusername)

---

<div align="center">

⭐ **If you found this project helpful, consider giving it a star!**

</div>
