from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

# Simple daily deal grabber for Tech/Video Games
# BeautifulSoup for parsing the html text, and requests for grabbing web pages
# Run this script again to get an update on the data we're pulling obviously

# Crawls for latest CNET deals
url = 'https://www.cnet.com/deals/'

# Connect to the link specified by url and grab the page html data
urlPage = uReq(url)
urlPageHTML = urlPage.read()
urlPage.close()

# To parse the html we grabbed from the urlPage we utilize Beautiful Soup
soupPage = BeautifulSoup(urlPageHTML, "html.parser")

# based on the sites html design, we want to find all deal components and store into pageDeals
# The info on each deal will be held in our pageDeals separately
pageDeals = soupPage.findAll("div", {"class": "row deal-listing-item"})

# Handle CSV output
newFile = "deals.csv"
n = open(newFile, "w")
headers = "Product Name, Price, Merchant\n"
n.write(headers)

# Loop through each deal of pageDeals and print the price as well as item on sale
for deals in pageDeals:

    # Handle title of each item
    title_temp = str(deals.h4)
    title_temp2 = title_temp[4:]
    title = title_temp2[0:len(title_temp2)-5]
    print(title)

    # Handle price of each item, and if price is not available, indicate so
    price_temp = deals.findAll("span", {"price"})
    price_temp2 = str(price_temp)
    price = price_temp2[22:len(price_temp2)-9]
    if price == "":
        price = "Unavailable"
    print("Price: $", price)

    # Handle merchant
    merchant_temp = deals.findAll("span", {"merchant"})
    merchant_temp2 = str(merchant_temp)
    merchant = merchant_temp2[24:len(merchant_temp2) - 8]
    print("From: ", merchant)

    # Separate info
    print('\n')

    # Write to our file and handle delimination by converting reserved comma usage to periods for csv files
    n.write(title.replace(",", ".") + "," + price.replace(",", ".") + "," + merchant.replace(",", ".")+ "\n")

# close the file once the for loop has looped through each deal
n.close()









