import csv
import requests
from bs4 import BeautifulSoup

def scrape_product_data(url, name_tag, name_class, price_tag, price_class, description_tag, description_class):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract product name
    product_name_tag = soup.find(name_tag, class_=name_class)
    product_name = product_name_tag.text.strip() if product_name_tag else "N/A"

    # Extract product price
    product_price_tag = soup.find(price_tag, class_=price_class)
    product_price = product_price_tag.text.strip() if product_price_tag else "N/A"

    # Extract product description
    product_description_tag = soup.find(description_tag, class_=description_class)
    product_description = product_description_tag.text.strip() if product_description_tag else "N/A"

    return {
        'Product Name': product_name,
        'Product Price': product_price,
        'Product Description': product_description
    }

def main():
    # Get user input for tag names and class names
    name_tag = input("Enter the tag name for the product name (e.g., h1): ")
    name_class = input("Enter the class name for the product name: ")
    price_tag = input("Enter the tag name for the product price (e.g., span): ")
    price_class = input("Enter the class name for the product price: ")
    description_tag = input("Enter the tag name for the product description (e.g., div): ")
    description_class = input("Enter the class name for the product description: ")

    # Read the CSV file containing the list of links
    with open('links.csv', 'r') as file:
        reader = csv.reader(file)
        links = [row[0] for row in reader]
    
    # Scrape data for each link and save to a new CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Product Name', 'Product Price', 'Product Description'])
        writer.writeheader()
        
        for link in links:
            product_data = scrape_product_data(link, name_tag, name_class, price_tag, price_class, description_tag, description_class)
            writer.writerow(product_data)
            print(f"Scraped data for {product_data['Product Name']}")

if __name__ == '__main__':
    main()
