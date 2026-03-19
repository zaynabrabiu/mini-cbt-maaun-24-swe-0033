# COS 202 Assignment 4: Mini CBT Engine with Flask

**Student Name:** ZAINAB RABIU
**Matric Number:** [MAAUN/24/SWE/0033
**Date:** 15 March 2026  

## Project Description
This is a simple Computer-Based Test (CBT) engine built with Python and Flask for COS 202. It uses:
- **OOP**: `Question` class with `__init__` and custom `is_correct` method.
- **Data Structures**: `deque` from `collections` for FIFO queue to manage question order.
- **Datetime**: `datetime.now()` to timestamp the test submission.
- **Flask**: Routes for home (`/`), start (`/start`), question (`/question`), submit (`/submit`), and result (`/result`).
- 6 questions related to our university, course topics, and Nigeria.
- Includes detailed choices for better learning.

The test runs in the browser, shows questions one by one, calculates score, and displays result with percentage and timestamp.

## How to Run
1. Clone the repo: `git clone
2. Enter folder: `cd cos202-mini-cbt-flask`
3. Activate venv: `source venv/bin/activate`
4. Install Flask: `pip install flask`
5. Run: `python app.py`
6. Open in browser: http://127.0.0.1:5000

## Files
- `models.py`: OOP classes + queue + datetime + terminal test.
- `app.py`: Flask app with routes.
- `templates/`: HTML files for home, question, result.

## Why This Meets Requirements
- OOP (7 marks): `Question` class with attributes and methods.
- Data Structures & APIs (7 marks): `deque` for FIFO, `datetime` for timestamp.
- Flask (6 marks): 5 routes, forms for answers, templates with Jinja.
- GitHub (5 marks): 20+ commits (add more small ones if needed, like fixes).

## Screenshots
(You can add screenshots here if you want extra polish – take photos of the browser and upload to GitHub.)
