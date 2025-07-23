import csv
from fpdf import FPDF
import os
from datetime import datetime

# function to read data from a CSV file

def read_student_data(file_name):
    students = []

    try:
        with open(file_name, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["Name"]
                math = int(row["Math"])
                science = int(row["Science"])
                english = int(row["English"])

                total_marks = math + science + english
                average_marks = total_marks / 3

                student_info = {
                    "name": name,
                    "math": math,
                    "science": science,
                    "english": english,
                    "total": total_marks,
                    "average": round(average_marks, 2)
                }

                students.append(student_info)

        return students
    
    except FileNotFoundError:
        print("File not found. Please check the file name.")
        return[]
    
    except Exception as error:
        print("Something went wrong while reading the file:", error)
        return[]
    
# function to create a PDF report from the student data 

def create_pdf_report(student_list, output_file):
    pdf = FPDF()
    pdf.add_page() 
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Student Report Card", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=10)
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    pdf.cell(200, 8, txt=f"Created on: {now}", ln=True, align="R")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    for number, student in enumerate(student_list, start=1):
        pdf.cell(200, 10, txt=f"Student {number}", ln=True)
        pdf.cell(200, 8, txt=f"Name     : {student['name']}", ln=True)
        pdf.cell(200, 8, txt=f"Math     : {student['math']}", ln=True)
        pdf.cell(200, 8, txt=f"Science  : {student['science']}", ln=True)
        pdf.cell(200, 8, txt=f"English  : {student['english']}", ln=True)
        pdf.cell(200, 8, txt=f"Total    : {student['total']}", ln=True)
        pdf.cell(200, 8, txt=f"Average  : {student['average']}%", ln=True)
        pdf.ln(4)
        pdf.cell(200, 5, txt="", ln=True)
        pdf.ln(3)

    pdf.output(output_file)
    print(f"\n PDF report has been saved as: {output_file}")

# main funtion that controls everything

def main():
    print("\n Stundet Marks Report Generator")
    print("")

    file_name = input("Enter the name of the CSV file (example: students.csv): ")

    if not os.path.isfile(file_name):
        print("The file does not exist in this folder.")
        return

    students = read_student_data(file_name)

    if not students:
        print("No student data found in the file.")
        return

    pdf_file_name = input("Enter a name for the PDF file (example: report.pdf): ").strip()

    if not pdf_file_name:
        pdf_file_name = "student_report.pdf"
    elif not pdf_file_name.endswith(".pdf"):
        pdf_file_name += ".pdf"

    create_pdf_report(students, pdf_file_name)

if __name__ == "__main__":
    main()


        


        