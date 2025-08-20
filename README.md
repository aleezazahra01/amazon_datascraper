🛒 Amazon Scraper with GUI


<img width="300" height="200" alt="amazonscraper" src="https://github.com/user-attachments/assets/1c60f402-6617-4e37-896a-87a58a2af44b" />

This project is a Tkinter-based desktop application that allows users to scrape product data from Amazon search result pages using Selenium and BeautifulSoup. The data is saved into a CSV or Excel file, which the user can name and download directly from the GUI.

🚀 Features

GUI built with Tkinter for easy interaction.

Scrapes product details such as:

✅ Title

✅ Price

✅ Number of items sold

✅ Ratings

✅ Product link

✅ Image link

Supports saving data in CSV and XLSX formats.

Displays real-time scraping progress and status updates inside the GUI.


📂 How It Works

Run the script:

python amazon_scraper.py


In the GUI:

Enter the Amazon page URL (search results or product listing).

Enter a file name for your output.

Click "Scrape from this page" to start scraping.

Once completed, click "Save As" to export the data in .csv or .xlsx.

🖼️ GUI Preview

The interface provides:

Input fields for URL & file name.

Buttons for Scraping and Saving.

A status frame showing instructions and scraping progress.

📑 Example Output

Sample CSV file contains:

title	price	item sold	ratings	link to the item	image link
Example Product 1	$29.99	500+	4.5 ★	amazon.com/...	img-url...
Example Product 2	$15.49	N/A	4.0 ★	amazon.com/...	img-url...
