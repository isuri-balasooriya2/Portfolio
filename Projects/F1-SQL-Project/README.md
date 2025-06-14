# 🏁 F1 Insights: Race, Rivalry, and Records (1950–2024)

A Formula 1-themed SQL analysis project exploring driver performance, team strategy, and historical trends across 70+ years of racing history. Built using relational databases, structured query language (SQL), and real-world data — this project simulates the work of a data analyst in motorsport and showcases advanced querying, data modeling, and analytical thinking.

---

## 🚀 Project Goals

- Design and implement a normalized relational schema for F1 data.
- Write complex SQL queries to answer strategic and performance-based questions.
- Visualize trends in race strategy, driver rivalries, and constructor dominance.
- Demonstrate SQL proficiency for data science portfolios and job interviews.

---

## 🗃️ Database Schema

The database contains the following key tables:

- `drivers`: Driver bio data
- `constructors`: Teams
- `circuits`: Race venues
- `races`: Year, round, and location of each race
- `results`: Final classification, points, and status
- `lap_times`: Per-lap timing data
- `qualifying`: Q1–Q3 timings
- `pit_stops`: Strategy-related pit data

Refer to `schema.sql` and `ERD.png` for the complete schema and relationships.

---

## 🔍 Key Analytical Questions

This project explores over 15 strategic questions across four key areas:

### 🧠 Driver Intelligence
- Who are the most consistent finishers in F1 history?
- Which drivers show the most year-on-year improvement?

### 🏢 Constructor Strategy
- Which teams dominate specific circuits (e.g., Monaco, Silverstone)?
- Who has the best podium-to-pole conversion ratio?

### ⏱️ Race Strategy & Performance
- How do grid positions influence finishing results?
- Which teams execute the fastest pit stops on average?

### 🔥 Rivalry & History
- Hamilton vs. Verstappen: Who wins head-to-head?
- Career points evolution of F1 legends

All SQL queries can be found in the `/queries/` folder.

---

## 🧪 Technologies Used

- SQL (PostgreSQL / MySQL compatible)
- Relational Database Design
- ER Diagrams (drawn with dbdiagram.io)
- CSV imports for data population
- Optional: Python (for data visualization phase)

---

## 📁 File Structure


