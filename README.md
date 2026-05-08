<h1 align="center">🧠 Python Quiz App</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Type-CLI%20Quiz-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/mhmdrzanouriyani/Quiz-python?style=for-the-badge" />
</p>

<p align="center">
  An interactive Python quiz app that tests your programming knowledge.<br>
  Answer multiple choice questions and get your score at the end.
</p>

---

## ✨ Features

- ✅ Multiple choice questions (A, B, C, D)
- ✅ Case-insensitive input (a or A both work)
- ✅ Live correct/wrong feedback after each question
- ✅ Final score display
- ✅ Easy to add new questions
- ✅ No external dependencies — pure Python

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/mhmdrzanouriyani/Quiz-python.git
cd Quiz-python
```

### 2. Run it
```bash
python quiz.py
```

### 3. Answer the questions
```
What does 'print()' do in Python?
A. It adds two numbers
B. It saves data to a file
C. It displays text or values on the screen
D. It makes a new variable
Enter your answer (A, B, C, or D): C
Correct!

You got 5 out of 5 questions correct.
```

---

## ➕ How to Add New Questions

Open `quiz.py` and add to the `questions` list:

```python
{
    "prompt": "Your question here?",
    "options": [
        "A. Option one",
        "B. Option two",
        "C. Option three",
        "D. Option four"
    ],
    "answer": "A"  # correct option letter (uppercase)
}
```

---

## 📁 Project Structure

```
Quiz-python/
├── quiz.py             # Main quiz script
├── requirements.txt    # No dependencies needed
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

---

## 📌 Roadmap

- [ ] Add more question categories (networking, Linux, AI)
- [ ] Add a timer per question
- [ ] Save high scores to a file
- [ ] Build a web version with Flask

---

## 👨‍💻 Author

**Mohammadreza Nouriyani**

[![YouTube](https://img.shields.io/badge/YouTube-Mohix_Code-red?style=flat&logo=youtube)](https://www.youtube.com/@Mohixcode)
[![Instagram](https://img.shields.io/badge/Instagram-mohix_code-purple?style=flat&logo=instagram)](https://www.instagram.com/mohix_code)
[![GitHub](https://img.shields.io/badge/GitHub-mhmdrzanouriyani-black?style=flat&logo=github)](https://github.com/mhmdrzanouriyani)

---

⭐ If this helped you, please give it a star!
