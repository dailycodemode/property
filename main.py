# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import os
import urllib.request
headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}
url = "https://www.myhome.ie/residential/dublin/property-for-sale"



def scrapePage(namedPage):
    response = requests.get(url, headers=headers)
    webpage = response.content
    soup = BeautifulSoup(webpage, "html.parser")

    pageResults = []

    for link in soup.find_all(class_="mb-3 ng-star-inserted"):
        soupPrice = link.find_all(class_="PropertyListingCard__Price")
        price = soupPrice[0].text.strip()

        soupAdd = link.find_all(class_="PropertyListingCard__Address")
        address = soupAdd[0].text.strip()
        targetURL = soupAdd[0].get('href')
        propertyID = os.path.basename(os.path.normpath(targetURL))

        bedTypeBathDetails = link.find_all(class_="PropertyInfoStrip__Detail")
        for detail in bedTypeBathDetails:
            # if detail.contains('icon="bed"'):
            for bed in detail.find_all(icon="bed"):
                beds = (detail.text.strip())
            for bath in detail.find_all(icon="bath"):
                baths = (detail.text.strip())
            for cube in detail.find_all(icon="cube"):
                cubes = (detail.text.strip())
            for home in detail.find_all(icon="home"):
                homes = (detail.text.strip())
            # for img in detail.find_all('img'):
            #     energyRating = (img.text.strip())
        propCard = [propertyID, targetURL, address, price, beds, baths, homes]
        pageResults.append(propCard)
    return(pageResults)
    # exit()
    # if link.get("class") == "MobilePropertyListing__Link":
    #     print(link.get('href'))

def getPageAmount(url):
    response = requests.get(url, headers=headers)
    webpage = response.content
    soup = BeautifulSoup(webpage, "html.parser")
    # for link in soup.find_all(class_="ng-star-inserted"):
    #     print(link)
    lastSection = soup.find_all(class_="ng-star-inserted")[-1]
    url = lastSection.find_all('a')[0].get('href')
    i = url.index("=")
    amnt = url[i+1:]
    return(amnt)
def getUrl(x):
    if x == 0:
        return url
    else:
        return url + "?page=" + str(x)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    results = []
    totalPageCnt = getPageAmount(url)

    for x in range(0, 3):
        fullURL = getUrl(x)
        results += scrapePage(url)

    print(results)
    # print(results)  # Press Ctrl+F8 to toggle the breakpoint.

# def get

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
