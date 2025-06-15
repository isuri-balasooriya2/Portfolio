# 🏁 F1 Insights: Race, Rivalry, and Records (1950–2024)

A Formula 1-themed SQL analysis project exploring driver performance, team strategy, and historical trends across 70+ years of racing history. Built using relational databases, structured query language (SQL), and real-world data - this project simulates the work of a data analyst in motorsport and showcases advanced querying, data modeling, and analytical thinking.

---

## 🚀 Project Goals

- Design and implement a normalized relational schema for F1 data.
- Write complex SQL queries to answer strategic and performance-based questions.
- Visualize trends in race strategy, driver rivalries, and constructor dominance.

---

## 🗃️ Database Schema

The database contains the following key tables:

- `drivers`: Driver bio data
- `constructors`: Teams
- `circuits`: Race venues
- `races`: Year, round, and location of each race
- `results`: Final classification, points, and status
- `qualifying`: Q1–Q3 timings
- `pit_stops`: Strategy-related pit data

Refer to `schema.sql` and `schema diagram.png` for the complete schema and relationships.

---

## 🔍 Key Analytical Questions

This project explores over 10 strategic questions across four key areas:

### 🧠 Driver Performance
- Who are the most consistent finishers in F1 history?
- Which drivers convert entries into points the most efficiently?
- Which drivers converts pole position to a win on race day?
- Who are the fastest one-lap drivers in Q3?
- Who overtakes the most positions on average?

### 🏢 Constructor Strategy
- Which teams dominate specific circuits (e.g., Monaco, Silverstone)?
- Which constructors have the highest pole to podium ratio?

### ⏱️ Race Strategy & Performance
- Which teams execute the fastest pit stops on average?

### 🔥 Rivalry & History
- Hamilton vs. Verstappen: Who wins head-to-head?
- Senns vs. Prost

All SQL queries can be found in the `/queries/` folder.

---

## 🧪 Technologies Used

- SQL
- Relational Database Design
- MySQL Workbench for executing querries
- Relational schema diagram (drawn with drawsql.app)
- CSV imports for data population

---



