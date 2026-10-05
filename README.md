# 🤖 AI Before-You-Buy Decision Engine

An AI-assisted product decision system that helps users choose products based on their **budget, priorities, and preferences**.

Instead of simply recommending a product, the system uses **weighted multi-criteria decision scoring** to rank available products and explains the recommendation using a **local AI model**.

---

## 🎯 Problem Statement

Choosing the right product can be difficult because users have different budgets and priorities.

For example, one user may prefer:

* ⚡ High performance
* 🔋 Better battery
* 🎒 Portability
* 🎮 Gaming performance

A simple product recommendation system may not consider these individual preferences.

This project solves the problem by combining **personalized scoring, product comparison, What-If analysis, and AI-generated explanations**.

---

## 💡 Proposed Solution

The **AI Before-You-Buy Decision Engine** allows users to:

1. Select a product category.
2. Set their maximum budget.
3. Assign importance weights to different features.
4. Filter products according to the budget.
5. Calculate a personalized decision score.
6. Rank the available products.
7. Identify the best match.
8. Generate an AI explanation for the recommendation.
9. Compare products.
10. Change priorities using What-If analysis.
11. Store previous decisions using SQLite.

---

## ✨ Key Features

### 💰 Budget Filtering

Shows products that fall within the user's selected budget.

### 🛍️ Multiple Product Categories

Currently supports:

* Laptops
* Smartphones

The system can be extended to other categories.

### 🎯 Personalized Ranking

Users assign importance weights to:

* Performance
* Battery
* Portability
* Gaming

The system calculates a weighted decision score.

### 🏆 Best Match

The product with the highest personalized score is displayed as the user's best match.

### 🤖 AI Explanation

The project uses **Ollama with Llama 3.2** to generate a short explanation of why the selected product was recommended.

### 📊 Score Visualization

Interactive charts display product rankings and feature contributions.

### 🆚 Product Comparison

Users can compare two products feature-by-feature.

### 🔄 What-If Analysis

Users can change their priorities and immediately see how the recommendation changes.

### 💾 Decision History

Previous recommendations are stored in a local **SQLite database**.

---

## 🧠 Decision Scoring

The system uses a weighted scoring approach.

```text
Decision Score =
(
Performance × Performance Weight
+
Battery × Battery Weight
+
Portability × Portability Weight
+
Gaming × Gaming Weight
)
/
Total Priority Weight
```

The product with the highest score becomes the **Best Match**.

---

## 🏗️ System Architecture

```text
              ┌─────────────────────┐
              │       User          │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Streamlit UI       │
              │ Budget & Priorities │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Product Filtering   │
              │ Category + Budget   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Decision Engine     │
              │ Weighted Scoring    │
              └──────────┬──────────┘
                         │
                  ┌──────┴──────┐
                  ▼             ▼
        ┌────────────────┐  ┌────────────────┐
        │ Best Product   │  │ Comparison &   │
        │ Ranking        │  │ What-If        │
        └───────┬────────┘  └────────────────┘
                │
                ▼
        ┌────────────────────┐
        │ Ollama + Llama 3.2 │
        │ AI Explanation     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ SQLite Database    │
        │ Decision History   │
        └────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core programming           |
| Streamlit  | Web application interface  |
| Pandas     | Product data processing    |
| Plotly     | Interactive visualizations |
| SQLite     | Decision history storage   |
| Ollama     | Local AI integration       |
| Llama 3.2  | AI explanation generation  |
| VS Code    | Development environment    |
| Git/GitHub | Version control            |

---

## 📂 Project Structure

```text
AI-Before-you-buy/
│
├── app.py
├── ai_engine.py
├── database.py
├── product.csv
├── decisions.db
├── README.md
└── venv/
```

### File Description

**app.py**
Main Streamlit application containing the user interface, filtering, scoring, comparison and What-If analysis.

**ai_engine.py**
Connects the application to Ollama and generates AI explanations.

**database.py**
Creates and manages the SQLite database and stores decision history.

**product.csv**
Contains the product information used by the decision engine.

**decisions.db**
Stores previous user recommendations.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the project

```bash
cd AI-Before-you-buy
```

### 3. Create and activate the virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install streamlit pandas plotly ollama
```

### 5. Install Ollama

Install Ollama and download the required model:

```bash
ollama pull llama3.2
```

Make sure Ollama is running before using the AI explanation feature.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔄 Application Workflow

```text
Select Category
       ↓
Set Budget
       ↓
Set Feature Priorities
       ↓
Filter Products
       ↓
Calculate Weighted Scores
       ↓
Rank Products
       ↓
Select Best Match
       ↓
Generate AI Explanation
       ↓
Compare Products
       ↓
Perform What-If Analysis
       ↓
Save Decision History
```

---

## 📱 Supported Products

The current prototype contains:

### 💻 Laptops

* Laptop A
* Laptop B
* Laptop C
* Laptop D
* Laptop E

### 📱 Smartphones

* Phone A
* Phone B
* Phone C
* Phone D
* Phone E

The product dataset can be expanded by adding new records to `product.csv`.

---

## 🔮 Future Scope

The project can be further improved by adding:

* More product categories
* Real-time product prices
* Online product APIs
* Product reviews and ratings
* User accounts
* Cloud database
* Recommendation history analytics
* Advanced machine learning models
* Price-performance prediction
* Personalized user profiles
* Voice-based product search
* More advanced explainable AI

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* Data processing using Pandas
* Streamlit application development
* Weighted decision algorithms
* AI/LLM integration
* Ollama and local AI models
* SQLite database management
* Data visualization
* User-centered application design
* Git and GitHub project management

---

## 👩‍💻 Developer

**Akshitha**

B.Tech Student | Software Development & AI Enthusiast

Interested in:

* Artificial Intelligence
* Machine Learning
* Software Development
* Data Science
* Prompt Engineering
* Problem Solving

---

## ⭐ Project Highlight

> **An AI-assisted multi-criteria decision engine that personalizes product selection based on user-defined priorities, analyzes trade-offs, and provides explainable recommendations using a local LLM.**
