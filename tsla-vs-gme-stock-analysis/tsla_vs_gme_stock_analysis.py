import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# define graphing functions 
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=.3)
    stock_data_specific = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data['Date'] <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific['Date']), y=stock_data_specific['Close'].astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific['Date']), y=revenue_data_specific['Revenue'].astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    fig.show()

# Extract TSLA Stock Data 
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head())

# Use Webscraping to Extract Tesla Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')
tables = soup.find_all("table")
target_table = tables[1]  # Assuming the table is at index 1

# Extract rows from the target table
rows = target_table.find_all("tr")

# Initialize lists to hold the data
dates = []
revenues = []

# Loop through the rows and extract data
for row in rows[1:]:  # Skip the header row
    cols = row.find_all("td")
    if len(cols) == 2:  # Ensure there are two columns
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()
        dates.append(date)
        revenues.append(revenue)

# Create a DataFrame
tesla_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r'[\$,]',"", regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail())

# Extract GME Stock Data 
gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head())

# Use Webscraping to Extract GME Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
soup_two = BeautifulSoup(html_data, 'html.parser')
tables = soup_two.find_all("table")
target_table = tables[1]  # Assuming the table is at index 1

# Extract rows from the target table
rows = target_table.find_all("tr")

# Initialize lists to hold the data
dates = []
revenues = []

# Loop through the rows and extract data
for row in rows[1:]:  # Skip the header row
    cols = row.find_all("td")
    if len(cols) == 2:  # Ensure there are two columns
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()
        dates.append(date)
        revenues.append(revenue)

# Create a DataFrame
gme_revenue = pd.DataFrame({
    "Date": dates,
    "Revenue": revenues
})
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r'[\$,]',"", regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
print(gme_revenue.tail())

# plot tsla stock data 
make_graph(tesla_data, tesla_revenue, 'Tesla')
# plot gme stock data 
make_graph(gme_data, gme_revenue, 'Game Stop')