# Simple PDF Merge App

**A simple desktop application built with Python and Tkinter for merging PDF files.**

## Description

**This application provides a graphical user interface (GUI) for easily merging multiple PDF files into a single document. Users can add files by dragging and dropping them onto a designated area or by using a file selection dialog. The application utilizes the **`<span class="selected">pypdf</span>` library for the PDF merging process and `<span class="selected">tkinterdnd2</span>` for drag-and-drop functionality.

**Note:** This version of the application currently only supports merging PDF files. Features for editing or converting PDFs are not included.

## Features

* **Intuitive graphical user interface (GUI).**
* **Drag and drop functionality for adding PDF files.**
* **File selection dialog to browse and add PDF files.**
* **List display of selected files.**
* **Option to remove selected files from the list.**
* **Merge multiple selected PDF files into one.**
* **"Save As" dialog to specify the output filename and location for the merged PDF.**
* **Basic styling with a dark teal interface and lighter drop box area.**
* **Styled buttons with hover effects.**
* **"About" menu with application information, contact details, and website.**

## Requirements

* **Python 3.6 or higher**
* `<span class="selected">pypdf</span>` library
* `<span class="selected">tkinterdnd2</span>` library

## Installation

1. **Make sure you have Python installed on your system.**
2. **Install the required libraries using pip:**
   ```
   pip install pypdf tkinterdnd2

   ```
3. **Save the provided Python script as a **`<span class="selected">.py</span>` file (e.g., `<span class="selected">pdf_merge_app.py</span>`).

## Usage

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where you saved the script.**
3. **Run the script using the Python interpreter:**
   ```
   python pdf_merge_app.py

   ```
4. **The "Simple PDF Editor" window will open.**
5. **Drag and drop PDF files onto the designated drop area, or click the "Select PDF files" button to choose files using a file explorer.**
6. **The selected files will appear in the list below the drop area.**
7. **You can select files in the list and click "Remove Selected" to remove them.**
8. **Click the "Merge PDFs" button.**
9. **A "Save Merged PDF As" dialog will appear. Choose the desired location and filename for the output merged PDF and click "Save".**
10. **A message box will confirm the success or report any errors during the merging process.**
11. **Access the "About" menu for application information.**

## Styling

**The application uses a dark teal color scheme for the interface, a slightly lighter teal for the drop box, and white text. Buttons are styled with dark purple background and white text, changing to light purple background and black text on hover with a raised relief. The text font is set to Verdana, size 12.**

## About

* **Version:** 1.0
* **Contact:** svanbuggenum@gmail.com
* **Website:** [www.svanbuggenumanalytics.com](https://www.svanbuggenumanalytics.com "null")
