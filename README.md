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
* **Dataset Size:** 35 Question-Answer pairs stored in `data/dataset.csv`
* **Dataset Sources & References:** Summarized in our own words from official BWF sources (accessed November 2026):
  1. Badminton World Federation (BWF). *BWF Statutes, Section 4.1: Laws of Badminton*.
  2. Badminton World Federation (BWF). (2023, May 12). *BWF Council Approves Interim Ban on 'Spin Serve' (Amendment to Law 9.1.5)*.
  3. Badminton World Federation (BWF). (2026, April 26). *Key Changes Under the 3x15 Scoring System*.
Press Ctrl + S (Windows) or Cmd + S (Mac) and check that the white dot next to README.md disappears.
Click inside the black Terminal box at the bottom and run:
git add .
git commit -m "Add project overview, team table, and dataset references to README"

## Architecture
1. **User Interface (`app/main.py`):** Built with Streamlit to capture user questions and display conversation history.
2. **Retrieval Engine (`src/chatbot.py`):** Searches `data/dataset.csv` using keyword-overlap matching to retrieve the top 3 relevant BWF rule pairs.
3. **LLM Generation (`src/chatbot.py`):** Injects the retrieved context into a structured prompt sent to the **Google Gemini API (`gemini-2.5-flash`)**.

## Model
* **Model / API:** Google Gemini API (`gemini-2.5-flash`)
* **Why we chose it:** Fast response speed, accurate context-grounded answers, and accessible free tier without GPU hardware.
* **Parameters:** `temperature = 0.3` (kept low to prevent hallucinating badminton rules outside our verified dataset).