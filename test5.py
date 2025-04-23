import requests
import json
from datetime import datetime

SERP_API_KEY = os.getenv("SERP_API_KEY")
MAPS_REVIEWS_URL = "https://serpapi.com/search"
MAPS_SEARCH_URL = "https://serpapi.com/search.json"

def get_place_data_id(place_name):
    params = {
        'engine': 'google_maps',
        'q': place_name,
        'api_key': SERP_API_KEY,
        'type': 'search',
        'hl': 'en'
    }
    
    try:
        print(f"\nSearching for place: {place_name}")
        response = requests.get(MAPS_SEARCH_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if 'place_results' in data:
            return data['place_results']['data_id']
        elif 'local_results' in data and 'places' in data['local_results']:
            return data['local_results']['places'][0]['data_id']
            
        print("Could not find the place in search results.")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error searching for place: {e}")
        return None
    except (json.JSONDecodeError, KeyError):
        print("Error processing SerpAPI response.")
        return None

def get_reviews_from_data_id(data_id, num_reviews=50):
    all_reviews = []
    next_page_token = None
    attempts = 0
    
    while len(all_reviews) < num_reviews and attempts < 6:
        params = {
            'engine': 'google_maps_reviews',
            'data_id': data_id,
            'api_key': SERP_API_KEY,
            'hl': 'en',
            'sort_by': 'newestFirst',
            'limit': 20,
        }
        
        if next_page_token:
            params['next_page_token'] = next_page_token
            
        try:
            print(f"\nFetching reviews batch (attempt {attempts + 1})")
            response = requests.get(MAPS_REVIEWS_URL, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            batch_reviews = data.get('reviews', [])
            all_reviews.extend(batch_reviews)
            
            print(f"Fetched {len(batch_reviews)} reviews (total: {len(all_reviews)})")
            
            next_page_token = data.get('serpapi_pagination', {}).get('next_page_token')
            if not next_page_token or not batch_reviews:
                break
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching reviews: {e}")
            break
        except json.JSONDecodeError:
            print("Error decoding response.")
            break
            
        attempts += 1
    
    all_reviews = sorted(
        all_reviews,
        key=lambda x: datetime.strptime(x['published_date'], '%B %d, %Y') if 'published_date' in x else datetime.min,
        reverse=True
    )[:num_reviews]
    
    return [{
        'rating': review.get('rating'),
        'text': review.get('snippet')
    } for review in all_reviews]

