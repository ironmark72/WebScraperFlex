# Web Scraping

This Python web_scraping allows you to scrape product data from a list of URLs provided in a CSV file. The web_scraping is designed to be flexible, allowing you to specify the HTML tags and class names for extracting the product name, product price, and product description from web pages.

## Prerequisites

Before using this web_scraping, you should have the following prerequisites installed:

- Python 3.9
- `requests` library (for making HTTP requests)
- `beautifulsoup4` library (for parsing HTML)
- A CSV file (`links.csv`) containing a list of product URLs to scrape.

## Usage

1. Clone this repository to your local machine.

2. Install the required Python libraries if you haven't already:

   ```bash
   pip install requests beautifulsoup4
   ```

3. Create a CSV file named `links.csv` in the same directory. Add a list of product URLs that you want to scrape in a single column.

4. Run the web_scraping using the following command:

   ```bash
   python web_scraping.py
   ```

5. The web_scraping will prompt you to enter the HTML tags and class names for the product name, product price, and product description. Provide the required information as requested.

6. The web_scraping will start scraping data from the provided URLs and save the results to an `output.csv` file.

7. Once the web_scraping finishes, you can find the scraped data in the `output.csv` file in the same directory.

## Customization

You can customize the web_scraping by specifying the HTML tags and class names for the product information fields (name, price, description) directly in the web_scraping. Alternatively, you can follow the prompts during web_scraping execution to customize on the fly.

## Example CSV File (links.csv)

```
https://example.com/product1
https://example.com/product2
https://example.com/product3
```

## Acknowledgments

- This web_scraping was created for educational purposes and can be adapted for various web scraping tasks.
- Make sure to respect the website's terms of service and robots.txt file when scraping data from websites.

Happy scraping!
