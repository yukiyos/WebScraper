import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define headers
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

# List of URLs
urls = [
    'https://www.investing.com/equities/nike',
    'https://www.investing.com/equities/coca-cola-co',
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/3m-co',
    'https://www.investing.com/equities/american-express',
    'https://www.investing.com/equities/amgen-inc',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/boeing-co',
    'https://www.investing.com/equities/cisco-sys-inc',
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/intel-corp',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/mcdonalds',
    'https://www.investing.com/equities/salesforce-com',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc',
    'https://www.investing.com/equities/wal-mart-stores',
    'https://www.investing.com/equities/disney',
]

# Initialize an empty list to store the data
# all_data = []
data = []

for url in urls:
    page = requests.get(url, headers=headers)
    try:
        soup = BeautifulSoup(page.text, 'html.parser')
        
        # Extract company name
        company = soup.find('h1', class_='mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr').text

        # Extract price
        price = soup.find('div', class_= 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text
        
        # Extract price change
        # change = soup.find('div', class_='instrument-price_instrument-price__xfgbB flex items-end flex-wrap font-bold').find_all('span')[2].text
        
        # Extract trading volume
        # volume = soup.find('div', class_='trading-hours_value__5_NnB').text
        
        # Append extracted data to the list
        data.append([company,price])
        # all_data.append([company, price, change, volume])
        
    except AttributeError:
        print(f"Change the Element id for URL: {url}")

# Define column names
column_names = ["Company", "Price"]

# Create a DataFrame
df = pd.DataFrame(column_names,data)

# Save the DataFrame to an Excel file
# df.to_excel('stocks.xlsx', index=False)

# Print the DataFrame to verify the output
print(df)
