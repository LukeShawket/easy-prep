<div align="center">

# Easy Prep

**A high-productivity desktop suite for rapid data transformation, multi-sheet SQL analytics, and low-code Python automation.**

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![UI Framework](https://img.shields.io/badge/UI-ttkbootstrap-107C41.svg)](https://ttkbootstrap.readthedocs.io/)
[![Data Engine](https://img.shields.io/badge/Data-Pandas%20%7C%20DuckDB-150458.svg)](https://duckdb.org/)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

</div>

---

**Easy Prep** bridges the gap between manual Excel manipulations and full-scale data engineering. Designed for data analysts, business intelligence teams, and operational specialists, Easy Prep turns messy datasets into clean, report-ready tables using high-performance local processing, multi-file SQL joins, and automated GUI generation for custom script pipelines.

---

## ⚡ Key Highlights

### 🔌 Dynamic Python Plugin Engine
*Transform scripts into interactive desktop tools effortlessly.*
- **Zero-Boilerplate GUI Generation:** Write standard Python data functions, and Easy Prep automatically generates corresponding UI controls (inputs, dropdowns, toggles) for end users.
- **Extensible Architecture:** Package custom transformation logic, proprietary formulas, or company-specific cleaning rules into modular plugins.
- **Low-Code Automation:** Allow non-technical team members to leverage custom Python logic without opening a terminal or modifying code.

### 🦆 Embedded DuckDB SQL Engine
*Perform complex multi-sheet relational queries locally.*
- **Cross-Sheet & Multi-File Analytics:** Query across multiple loaded Excel worksheets, CSVs, or DataFrames using standard SQL syntax.
- **High-Performance In-Memory Joins:** Cross-reference tables, execute aggregations, and blend datasets instantly powered by DuckDB.
- **Native SQL Syntax Highlighting:** Built-in SQL editor with tokenization and key-bindings for rapid ad-hoc data exploration.

---

## 📸 Interface Preview

<div align="center">

### Main Workspace
<img width="100%" alt="Easy Prep Main Page" src="https://github.com/user-attachments/assets/8b66f8d1-e4fe-4dc2-a133-a4373821a769" />

<br/><br/>

### Data Profiling & Analytics Dashboard
<img width="100%" alt="Easy Prep Dashboard" src="https://github.com/user-attachments/assets/537a6a7d-1330-47d2-9b19-1dedc96898d2" />

</div>

---

## 🚀 Core Features

- **Automated Data Cleaning:** Standardize date formats, handle missing values, clean whitespace, and deduplicate records with instant UI controls.
- **Modern Responsive UI:** Built with `ttkbootstrap` for a crisp visual interface with native dark/light theme support.
- **Interactive Profiling:** Instant column distributions, data type detection, and summary statistics to catch data anomalies early.
- **Local-First & Secure:** Processes data entirely in-memory on your local machine—ideal for confidential workplace files.

---

## 🛠️ Tech Stack

<div align="center">

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Core Runtime** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Application engine and execution runtime |
| **Interface** | ![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-107C41?style=flat) | Modern desktop GUI component architecture |
| **Data Engine** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | In-memory tabular manipulation and transformation |
| **SQL Engine** | ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat&logo=duckdb&logoColor=black) | Fast multi-file relational querying and cross-referencing |

</div>

---

## 🏁 Getting Started

### Prerequisites
- **Python 3.9+** installed on your system.

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/LukeShawket/easy-prep.git](https://github.com/LukeShawket/easy-prep.git)
   cd easy-prep
