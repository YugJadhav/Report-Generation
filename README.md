# Task 2 – Automated Report Generation

**Internship**: Python Developer  
**Organization**: ELiteTEch  
**Duration**: 16th May – 5th August 2025

## Task Overview
This script reads student marks from a CSV file and generates a structured PDF report card using the `fpdf` library.

## Technologies Used
- Python
- `fpdf`
- CSV file handling

## Files Included
- `main.py`: Python script to read student data and create a PDF
- `students.csv`: Input CSV file containing student marks
- `report.pdf`: Sample output report
- `README.md`

## How to Run
1. Make sure you have the required library:
   ```bash
   pip install fpdf
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Enter the name of the CSV file (`students.csv`) and desired output PDF file name (e.g., `report.pdf`).

## Sample Output
A PDF is generated showing each student’s:
- Name
- Marks in Math, Science, and English
- Total Marks
- Average Percentage

> Example:
> Name     : Isha  
> Math     : 90  
> Science  : 93  
> English  : 98  
> Total    : 281  
> Average  : 93.67%

## Learnings
- Working with file I/O in Python
- Using FPDF to generate structured documents
- Automating report generation from data
