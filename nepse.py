from bs4 import BeautifulSoup
import requests,csv

url = "https://www.sharesansar.com/today-share-price"

page = requests.get(url)
soup = BeautifulSoup(page.content,"lxml")

stocks = (soup.find_all("tr"))

with open("nepse.csv","w", newline = "") as file:
        writedata = csv.writer(file)
        header = ["SN","symbol","stock confidence","open price","High price","Low price","close price","VWAP","Volume","previous day close price","Total turnover","Transaction","price difference","Range","Difference%","Range%","vwap%","120 days","180 days","52 weeks high","52 weeks low"]
        writedata.writerow(header)
        for stock in stocks:
            rows = stock.find_all("td")
            i=0
            while(i<len(rows)):
                sn=  rows[i].text
                i = i+1
                sym = rows[i].a.text
                i = i+1
                stock_confidence = rows[i].text
                i = i+1
                open_price = rows[i].text
                i = i+1
                high_price = rows[i].text
                i = i+1
                low_price = rows[i].text
                i = i+1
                close_price = rows[i].text
                i = i+1
                vwap = rows[i].text
                i = i+1
                volume = rows[i].text
                i = i+1
                previous_day_close_price = rows[i].text
                i = i+1
                total_turnover = rows[i].text
                i = i+1
                transaction = rows[i].text
                i = i+1
                price_difference = rows[i].text
                i = i+1
                range = rows[i].text
                i = i+1
                difference_percent = rows[i].text
                i = i+1
                range_percent = rows[i].text
                i = i+1
                vwap_percent = rows[i].text
                i = i+1
                days_120 = rows[i].text
                i = i+1
                days_180 = rows[i].text
                i = i+1
                weeks_high_52 = rows[i].text
                i = i+1
                weeks_low_52 = rows[i].text
                i = i+1
                stock_info = [sn,sym,stock_confidence,open_price,high_price,low_price,close_price,vwap,volume,previous_day_close_price,total_turnover,transaction,price_difference,range,difference_percent,range_percent,vwap_percent,days_120,days_180,weeks_high_52,weeks_low_52]
                writedata.writerow(stock_info)