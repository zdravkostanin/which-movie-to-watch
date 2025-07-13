import requests
from bs4 import BeautifulSoup

year = input("What year of movies would you like to explore? (default: 2020): ")

if not year:
    year = '2020'
    
url = f"https://www.imdb.com/search/title/?release_date={year},{year}&title_type=feature&sort=num_votes,desc"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
i = 1

movieList = soup.find_all('div', attrs={'class': 'ipc-metadata-list-summary-item__c'})

for div_item in movieList:    
    # look for the link that contains "sr_t_" in href (that's the title link)
    title_link = div_item.find('a', href=lambda x: x and 'sr_t_' in x)
    
    if title_link:
        full_text = title_link.get_text(strip=True)
        # Remove the number at the beginning (e.g., "1. Tenet" -> "Tenet")
        title = full_text.split('. ', 1)[-1] if '. ' in full_text else full_text
        print(f"{i}. Movie: {title}")
        i += 1
    else:
        print('Movie: Title not found')