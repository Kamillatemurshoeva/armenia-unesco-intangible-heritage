# Armenia UNESCO Intangible Cultural Heritage Dataset

Part of the **Open Data Armenia Project**.

This repository collects metadata about Armenian elements listed in the UNESCO Intangible Cultural Heritage (ICH) database.


---

## Data Source

UNESCO Intangible Cultural Heritage – Armenia  
https://ich.unesco.org/en/state/armenia-AM

All original cultural heritage descriptions and media belong to **UNESCO and the respective cultural heritage communities**.

This repository only provides **structured metadata extracted from publicly available pages**.

---

## Dataset Fields

| Field | Description |
|------|-------------|
| element_id | UNESCO unique identifier of the element |
| title | Name of the heritage element |
| year | Year of inscription |
| list_type | UNESCO list (RL – Representative List, USL – Urgent Safeguarding List) |
| url | Link to the original UNESCO page |
| source_page | Page where the data was collected |

---

## Files

main.py — Python scraper script  
armenia_unesco.csv — dataset in CSV format  
armenia_unesco.json — dataset in JSON format  
requirements.txt — Python dependencies  

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Run the scraper

python main.py

The script will generate:

armenia_unesco.csv  
armenia_unesco.json

---

## Project

This repository is part of the **Open Data Armenia**, which aims to collect and structure publicly available Armenian cultural and historical datasets for research and open data initiatives.
