import pandas as pd
import requests
from datetime import datetime, timedelta
import time

API_KEY = 'qlj7oodip2xf9kAUQhb7lGwCoy98EagC'
LIST_NAME = 'hardcover-fiction'
BASE_URL = 'https://api.nytimes.com/svc/books/v3/lists'
start_date = datetime(2019, 1, 6)
end_date = datetime.today()

def fetch_weekly_data(date):
    formatted_date = date.strftime('%Y-%m-%d')
    url = f"{BASE_URL}/{formatted_date}/{LIST_NAME}.json?api-key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data:
            return data['results']['books']
    return None

#Loop through weeks
all_books = []
current_date = start_date

while current_date <= end_date:
    print(f"Fetching data for {current_date.strftime('%Y-%m-%d')}...")
    weekly_books = fetch_weekly_data(current_date)

    if weekly_books:
        for book in weekly_books:
            book_info = {
                'date': current_date.strftime('%Y-%m-%d'),
                'title': book['title'],
                'author': book['author'],
                'publisher': book['publisher'],
                'rank': book['rank'],
                'weeks_on_list': book['weeks_on_list'],
                'description': book['description']
            }
            all_books.append(book_info)

    current_date += timedelta(weeks=1)
    time.sleep(1)

df = pd.DataFrame(all_books)
df.to_csv('nyt_books_data_2019_onwards.csv', index=False)
print("Data collection complete.")




