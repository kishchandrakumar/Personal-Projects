'''
A script to notify when an item on amazon is available, 
or if available, track its price and store historic prices.
'''
import requests
import csv
from bs4 import BeautifulSoup
from datetime import date
import smtplib

# URLs we want to track go in this list:
urls = ["https://www.amazon.co.uk/Adidas-Gymnastics-Black-Footwear-White/dp/B079L56FNM/ref=sxin_18_ac_d_rm?ac_md=3-3-YWRpZGFzIHNob2Vz-ac_d_rm_rm_rm&cv_ct_cx=shoes&dchild=1&keywords=shoes&pd_rd_i=B079L56FNM&pd_rd_r=d014aeac-758e-4b5a-a184-609e5d291bd8&pd_rd_w=Lb5KS&pd_rd_wg=df4N1&pf_rd_p=73573abc-9548-43f0-87cb-a185286cee4c&pf_rd_r=AVF547YARHQKJ743J16A&psc=1&qid=1632321242&sr=1-4-fe323411-17bb-433b-b2f8-c44f2e1370d4",
       "https://www.amazon.co.uk/Anker-Ultra-Compact-High-Speed-VoltageBoost-Technology/dp/B07QXV6N1B?ref=deals_deals_deals-grid_dcell_img_28_476c969c_dt_slot-15_582b"]

def email_notif(title, current_price, rrp, url):
    _t = str(title)
    _c = str(current_price)
    _r = str(rrp)
    _u = str(url)
    from_address = "kish.conding.projects@gmail.com"
    to_address   = "kishanck@hotmail.co.uk"
    subject = f'New Price Drop for {_t}'
    message = f'Your watched item {_t} is now {_c}, down from the RRP price of {_r}.\
                Click here to buy: {_u}'

    smtp_object = smtplib.SMTP('smtp.gmail.com', 587) # Simple Mail Transfer Protocol
    smtp_object.ehlo() # Client identifies itself to SMTP server
    smtp_object.starttls()
    smtp_object.login(from_address, "dgbyqcrxnydadadx") #App password used for security

    #Sending an email

    msg = "Subject: "+ subject +"\n\n" + message
    msg = msg.encode('utf-8')
    smtp_object.sendmail(from_address,to_address,msg)


# User-Agent key contains information about the browser
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'} #Identifies the type of browser and version


for url in urls:
    r = requests.get(url, headers = headers)
    # Response will be HTML so needs parsing using beautiful soup
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')

    #Find unique elements in the soup using HTML tag as 'id', and assign to individual variables
    title  = soup.find(id='productTitle').get_text(strip=True)
    rrp    = soup.find("span", {'class':"priceBlockStrikePriceString"}).get_text(strip=True)
    try:
        current_price  = soup.find(id='priceblock_ourprice').get_text(strip=True)
    except:
        current_price  = soup.find("span",{"id":'priceblock_dealprice'}).get_text(strip=True)

    # Remove '£' sign and convert to float
    rrp = float(rrp[1:])
    current_price = float(current_price[1:])
    perc_saving = (rrp-current_price)/rrp
    current_date = str(date.today())

    if current_price <= 0.9*rrp: #Emails if 10% saving or larger
        email_notif(title, current_price, rrp, url)

    #Creates CSV with correct headers if one doesn't exist:
    try:   #If CSV file doesn't yet exist, create one with headers:
        with open('price-drop.csv', 'r') as f:
            pass
    except:
        with open('price-drop.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['Date','Product','RRP','Current Price','Percentage Saving','Link'])
    finally:
        with open('price-drop.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            data   = [current_date, title, rrp, current_price, perc_saving,url]
            writer.writerow(data)