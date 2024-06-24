import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Define headers
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

# List of URLs
urls = [
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/intel-corp',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc'
]

# Initialize an empty list to store the data
data = []

for url in urls:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Extract company name
    company = soup.find('h1', class_='mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr').text

    # Extract price
    price = soup.find('div', class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text

    # Extract numeric values (price change)
    change_tag = soup.find('div', class_='flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main')
    change = change_tag.text if change_tag else None
    
    if change is None:
        # Try to find positive change tag if negative is not found
        change_tag = soup.find('div', class_='flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-positive-main')
        change = change_tag.text if change_tag else 'N/A'
    

    # Use regex to extract numbers and percentages
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+%|\d+", change)
    
    # Combine extracted values into a single string
    change_values = ' '.join(numbers)
    
    # Append extracted data to the list
    data.append([company, price, change_values])

# Define column names
column_names = ["Company", "Price", "Change"]

# Create a DataFrame
df = pd.DataFrame(data, columns=column_names)

print(df)

# Save DataFrame to a CSV file
df.to_csv("stock_data.csv", index=False)

