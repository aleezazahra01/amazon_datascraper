from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service   
from tkinter import *
from bs4 import BeautifulSoup
import csv
import tkinter as tk
import datetime
import time
import pandas as pd
from tkinter import filedialog


format_list = ['.csv', '.xlsx']


class AmazonScraper:
    def __init__(self):
        self.url = ''
        self.file_name = ''
        self.driver=''
        self.GUI()


    def GUI(self):
        self.COLOUR_ONE = "#222831"
        self.text_color = "#EB8007"
        self.frame_color = "#B5B3AF"

        self.root = tk.Tk()
        self.root.geometry('600x600')
        self.root.config(bg=self.COLOUR_ONE)
        self.root.title("AirBnb scraper ")

        self.title = Label(self.root, text='Amazon Scraper', font=('Helvetica', 20, 'bold'), fg=self.text_color, bg=self.COLOUR_ONE)
        self.title.pack(pady=10)
        self.entry_title = Label(self.root, text='Enter the url of the page:', fg=self.text_color, bg=self.COLOUR_ONE)
        self.entry_title.pack(pady=10)
        self.entry_url = Entry(self.root)
        self.entry_url.pack(pady=5)
     

        # file name 
        self.file_label = Label(self.root, text='Enter the file name: ', fg=self.text_color,bg=self.COLOUR_ONE)
        self.file_label.pack(pady=10)
        # self.file_entry = Entry(self.root)
        # self.file_entry.pack(pady=5)
        # self.file_name = self.file_entry.get_text()
        self.file_var = tk.StringVar()
        Entry(self.root, textvariable=self.file_var).pack(pady=5)

        # create a scrape button 
        self.scrape_button = Button(self.root, text="Scrape from this page", command=self.scrape_func).pack(pady=10)

        # creating a path to save the file 
        self.save_button = Button(self.root, text='Save As', command=self.save_as).pack(pady=10)

        # creating another frame inside the root to display the current status
        self.status_frame = tk.Frame(
            self.root,
            width=400,
            height=400,
            bg=self.frame_color,
            relief="ridge",
            borderwidth=3
        )
        #printing instructions on the frane
        self.status_frame.pack(pady=10, padx=10, fill='both', expand=True)
        self.instructions=Label(self.status_frame, text='Instructions: \n1. Enter the URL of the Amazon page you want to scrape.\n2. Enter a name for your output file.\n3. Choose the format (CSV or XLSX).\n4. Click "Scrape from this page" to start scraping.', fg=self.COLOUR_ONE,bg=self.frame_color).pack(pady=5)


        self.root.mainloop()

    # creating a function to scrape data from the url given by the user 
    def scrape_func(self):
        self.url = self.entry_url.get()
        self.file_name = self.file_var.get()
        #initalizing a driver
        self.driver = webdriver.Chrome()

        self.driver.get(self.url)
    
        # Wait until all products get loaded

        WebDriverWait(self.driver, 20).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-component-type='s-search-result']"))

        )


        # Scroll to the bottom so all the contents get loaded
        self.scroll_to = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2)")
        #save the html in a file then scrape using beautfulsoup
        with open('page.html', 'w', encoding='utf-8') as f:
            f.write(self.driver.page_source)
        f.close()

        # Open the CSV file to write the data into
        with open(f'{self.file_name}.csv', mode='w', encoding='utf-8') as f:
            self.writer = csv.writer(f)
            self.writer.writerow(['title', 'price', 'item sold', 'link to the item', 'image link', 'ratings'])
            f.close()
        
        # Parse the page
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.products = soup.find_all('div', {'data-component-type': 's-search-result'})
        self.product_found = len(self.products)

        # Show number of products found in status frame
        self.display_found = tk.Label(
            self.status_frame,
            text=f"Found {self.product_found} products",
            bg=self.text_color
        )
        self.display_found.pack(pady=5)

        try:
            for product in self.products:
                # Title
                titles = product.select_one('h2 > span')
                title_names = titles.get_text(strip=True) if titles else 'N/A'

                # Price
                price_tag = product.find('span', class_='a-price-whole')
                price = price_tag.get_text(strip=True) if price_tag else 'N/A'

                price_symbol_tag = product.find('span', class_='a-price-symbol')
                price_symbol = price_symbol_tag.get_text(strip=True) if price_symbol_tag else 'N/A'

                final_price = price_symbol + price

                # Item sold
                item_sold_tag = product.find('span', class_='a-size-base s-underline-text')
                item_sold = item_sold_tag.get_text(strip=True) if item_sold_tag else 'N/A'

                # Ratings
                stars_tag = product.find('span', class_='a-icon-alt')
                stars = stars_tag.get_text(strip=True) if stars_tag else 'N/A'

                # Product link
                prod_link_tag = product.find('a', class_='a-link-normal s-line-clamp-4 s-link-style a-text-normal')
                prod_link = prod_link_tag['href'] if prod_link_tag else 'N/A'

                # Image link
                img_link_tag = product.find('img', class_='s-image')
                img_link = img_link_tag['src'] if img_link_tag else 'N/A'

                # Append to CSV
                with open(f'{self.file_name}.csv', mode='a', encoding='utf-8') as f:
                    self.writer = csv.writer(f)
                    self.writer.writerow([title_names, final_price, item_sold, stars, prod_link, img_link])
                self.label_success=Label(self.status_frame, text='Scraping completed successfully',fg=self.text_color).pack(pady=5)


        except Exception as e:
            self.exception_label=Label(self.status_frame, text=f"An error occurred: {e}", bg=self.text_color).pack(pady=5)
    def save_as(self):
        # pass
        self.file_path = filedialog.asksaveasfilename(
            defaultextension='.csv,.xlsx',
            filetypes=[('CSV files', '*.csv'), ('XLSX files', '*xlsx')],
            title="Save your file as "
        )

        if self.file_path.endswith('.csv'):
            df = pd.read_csv(f"{self.file_name}.csv")
            self.display_save = tk.Label(self.root, text=f"Sved in {self.file_path} as {self.file_name}.csv").pack(pady=4)
        elif self.file_path.endswith('.xlsx'):
            df.to_excel(self.file_path, index=False)

            self.display_save = tk.Label(self.root, text=f"Sved in {self.file_path} as {self.file_name}.xlsx").pack(pady=4)
        else:
            self.display_not_saved = Label(self.root, text='Not saved ', fg=self.text_color, bg=self.COLOUR_ONE).pack(pady=4)


if __name__ == "__main__":
    AmazonScraper()
