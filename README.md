# BWF Badminton Rules Assistant
A domain-specific AI chatbot that answers questions about official Badminton World Federation (BWF) rules, court dimensions, scoring, serving, and match regulations.

## Team
| Name | GitHub Username | Role |
|------|-----------------|------|
| KHATIB SARBINI BIN SAID | Cuttip | Project Leader |
| AHMAD IZAHAN BIN AZMAN | izahanahmad | Frontend Developer |
| WAN AQMAL ARIFF QHAUSAR BIN WAN SHAIPULNIZAM | soulessx | Backend Developer |
| MUHAMMAD IBRAHIM SHAH BIN ABDUL RAZAK | Kawaiions | Domain Specialist |

## Domain and Dataset
* **Domain:** Sports Rules — Badminton Rules Assistant
* **Dataset Size:** 38 Question-Answer pairs stored in `data/dataset.csv`
* **Dataset Sources & References:** Summarized in our own words from official BWF sources (accessed November 2026):
  1. Badminton World Federation (BWF). *BWF Statutes, Section 4.1: Laws of Badminton*.
  2. Badminton World Federation (BWF). (2023, May 12). *BWF Council Approves Interim Ban on 'Spin Serve' (Amendment to Law 9.1.5)*.
  3. Badminton World Federation (BWF). (2026, April 26). *Key Changes Under the 3x15 Scoring System*.

## Architecture
1. **User Interface (`app/main.py`):** Built with Streamlit to capture user questions and display conversation history.
2. **Retrieval Engine (`src/chatbot.py`):** Searches `data/dataset.csv` using keyword-overlap matching to retrieve the top 3 relevant BWF rule pairs.
3. **LLM Generation (`src/chatbot.py`):** Injects the retrieved context into a structured prompt sent to the **Google Gemini API (`gemini-2.5-flash`)**.

## Model
* **Model / API:** Google Gemini API (`gemini-2.5-flash`)
* **Why we chose it:** Fast response speed, accurate context-grounded answers, and accessible free tier without GPU hardware.
* **Parameters:** `temperature = 0.3` (kept low to prevent hallucinating badminton rules outside our verified dataset).

## How to Run
1. Open the repository in GitHub Codespaces.
2. Install required libraries:
   `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and insert your Gemini API key:
   `cp .env.example .env`
4. Launch the chatbot:
   `streamlit run app/main.py`

## Demo
* **Video Demo:** [Link will be added on Day 6]
* **Screenshots:** Available in `docs/`

## Limitations
* Keyword-overlap retrieval relies on matching English words from `data/dataset.csv`, so queries asked purely in Malay or using unusual phrasing without matching keywords trigger a polite refusal.
* Knowledge is restricted to BWF Laws of Badminton covered in our dataset; unrelated topics are politely declined.

## GenAI Use
* **Tools Used:** Google Gemini
* **Purpose:** Used for code debugging, boilerplate structuring, and summarizing BWF rules under FSKM GenAI Tahap 3 (Kolaborasi Hibrid, 30%). All files were verified and committed by group members.
