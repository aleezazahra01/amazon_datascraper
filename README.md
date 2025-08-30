## Amazon Scraper with GUI

<img width="606" height="638" alt="amazonscraper" src="https://github.com/user-attachments/assets/50a1a75f-2f05-444b-bc87-3345d573f896" />


(wtf did i write airbnb scraper)

This project is a Tkinter-based desktop application that allows users to scrape product data from Amazon search result pages using Selenium and BeautifulSoup.
The data is saved into a CSV or Excel file, which the user can name and download directly from the GUI.

## Features

GUI built with Tkinter for easy interaction.Using tkinter could be slow but it's the only GUI I'm familiar with.Supports saving data in CSV and XLSX formats ,Displays real-time scraping progress and status updates inside the GUI.
In the GUI:

Just Enter the Amazon page URL (search results or product listing) nd Enter a file name for your output.
Simply Click "Scrape from this page" to start scraping.
Once completed, click "Save As" to export the data in .csv or .xlsx.

## Example Output
(Sample output)
title	price	item sold	ratings	link to the item	image link
Example Product 1	$29.99	500+	4.5 ★	amazon.com/...	img-url...
Example Product 2	$15.49	N/A	4.0 ★	amazon.com/...	img-url...
