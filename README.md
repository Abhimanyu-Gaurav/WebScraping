# WebScraping
A simple web scraping project using Python's `requests` and `BeautifulSoup` to extract information from a website like **Times of India**.

---

## Technologies Used
- **Python**: Core programming language for backend logic.
- **Requests**: For making HTTP requests and fetching the HTML code.
- **BeautifulSoup**: For parsing and navigating through HTML data.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Key Features](#key-features)
3. [Installation](#installation)
4. [How to Use](#how-to-use)
5. [License](#license)

---

## Project Description
This project demonstrates how to scrape web pages using the `requests` module to fetch HTML and `BeautifulSoup` to parse and extract meaningful data. The code extracts various HTML elements like:
- Paragraphs (`<p>`)
- Headings (`<h1>`, `<h2>`)
- Links (`<a>`)
- Images (`<img>`)

It also shows how to extract specific content based on CSS class names or HTML IDs.

---

## Key Features
- Fetch HTML code from a website.
- Parse and pretty-print the HTML structure.
- Extract elements like title, paragraphs, links, and images.
- Find specific content by class names and IDs.
- Extract all links and image URLs on the page.

---

## Installation
To install the required dependencies, follow these steps:

1. Clone the repository:
   ```bash
   https://github.com/Abhimanyu-Gaurav/WebScraping

2. Navigate to the project directory:
   ```bash
   cd WebScraping
   
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt

---

## How to Use
1. Modify the `url` variable in the script to the website you want to scrape.
2. Run the script:

    ```bash
    python main.py

3. The script will print extracted information such as:
   - Page title
   - Paragraph text
   - All links and images

---    

## License

- This project is licensed under the MIT License - see the [License](License) file for details.

---    