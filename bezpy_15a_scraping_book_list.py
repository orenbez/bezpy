# This scripts aims to get all book names on historic New York Time Best Sellers (middle_grade_paperback_monthly)
import os
import requests   # see bezpy_26_requests.py
import pandas as pd
from bs4 import BeautifulSoup

if __name__ == '__main__':
    nylist = pd.DataFrame()
    # the earliest list is 2019/10/01, so the starting year is 2019
    for i in [(2019,10),(2019,11),(2019,12),(2020,1),(2020,2)]:
        the_year, the_month = str(i[0]), str(i[1]).zfill(2)

        url = f'https://www.nytimes.com/books/best-sellers/{the_year}/{the_month}/middle-grade-paperback-monthly/'
        page = requests.get(url)
        print(f"requests.get({url}")

        # ensure proper result is returned
        if page.status_code != 200:
            continue

        # BeautifulSoup to parse the right elements out
        soup = BeautifulSoup(page.text, 'html.parser')

        # the specific class names are unique for this URL and they don't change across all URLs
        top_list = soup.findAll("ol", {"class": "css-12yzwg4"})[0].findAll("div", {"class": "css-xe4cfy"})
        print(the_year, the_month, len(top_list))

        # loop through the Best Sell    er list in each Year-Month, and append the information into a pandas DataFrame
        for i in range(len(top_list)):
            book = top_list[i].contents[0]
            title = book.findAll("h3", {"class": "css-5pe77f"})[0].text
            author = book.findAll("p", {"class": "css-hjukut"})[0].text
            review = book.get("href")

            # print("{0}, {1}; review: {2}".format(title, author, review))
            one_item = pd.Series([the_year, the_month, title, author, i+1, review], index=['year', 'month', 'title', 'author', 'rank', 'review'])
            nylist = nylist.append(one_item, ignore_index=True, sort=False)
    nylist = nylist.reindex(columns=['year', 'month', 'title', 'author', 'rank', 'review'])
    nylist.to_csv(r".\mydata\nylist.csv", index=False)

    # Set DataFrame display
    pd.set_option('display.max_rows', 10)  # FIVE from head, FIVE from tail
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 1000)  # chars display on one line
