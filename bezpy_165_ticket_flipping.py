# 1. Data Scraping:
    # BeautifulSoup: A popular library for parsing HTML and extracting data from websites.
    # Scrapy: A powerful framework for building web crawlers and extracting structured data.
    # Selenium: A tool for automating web browsers, useful for websites that rely heavily on JavaScript.

# 2. Ticket APIs:
    # Ticketmaster API: Provides access to ticket listings and pricing data from Ticketmaster.
    # StubHub API: Offers access to ticket listings on the StubHub marketplace.
    # SeatGeek API: Provides access to ticket listings and pricing data from SeatGeek.

# 3. Data Analysis & Manipulation:
    # Pandas: A powerful library for data manipulation and analysis.
    # NumPy: A library for numerical computing in Python.

# 4. Automation & Scheduling:
    # APScheduler: A library for scheduling tasks in Python.
    # Celery: A distributed task queue for handling more complex workflows.


# https://github.com/mariamills/Ticket-Selling-Python
# https://www.youtube.com/watch?v=F2bIgf54_iU
# https://github.com/Nedervino/TicketCrawler


# In the United States, using automated bots to purchase and resell event tickets is illegal under the Better Online Ticket Sales (BOTS) Act of 2016. This law prohibits the use of bots to bypass purchasing restrictions, such as ticket limits or security measures, on ticketing websites for events like concerts, theater performances, and sports.
# The BOTS Act makes it illegal not only to acquire tickets through these means but also to resell tickets obtained in violation of the statute if the seller was involved in or knowingly benefited from the illegal purchase. Enforcement of this law falls under the Federal Trade Commission (FTC) and state attorneys general.

# Automating purchases may not be allowed, so make sure you comply with the platform’s terms
# Check the API documentation for rate limits (e.g., requests per minute/hour) to avoid getting blocked.
# Review terms of service carefully to ensure your app adheres to usage policies. For example, some platforms may restrict reselling behavior
# Even with API access, ensure that you're buying tickets within platform limits (e.g., 4-6 tickets per user). Automating ticket purchasing could inadvertently violate rules, even if your intent is legal.


import requests


def search_tickets(event_name):
    client_id = ''
    url = f"https://api.seatgeek.com/2/events?client_id={client_id}&q={event_name}"

    response = requests.get(url)

    if response.status_code == 200:
        events = response.json().get('events', [])
        for event in events:
            print(f"Event: {event['title']}")
            print(f"Date: {event['datetime_local']}")
            print(f"Venue: {event['venue']['name']}")
            print(f"Location: {event['venue']['city']}, {event['venue']['state']}")
            print("-" * 40)
    else:
        print(f"Failed to retrieve data: {response.status_code}")


# Example usage
search_tickets("Taylor Swift")