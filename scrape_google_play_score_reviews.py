import pandas as pd 
from google_play_scraper import Sort, reviews, app

apps = pd.read_csv('Google Play Store Apps.zip')

# Select 10000 random apps 
apps = apps.sample(10000)

app_ids = apps['App Id']

app_reviews_df = pd.DataFrame(columns=['app_id', 'user_name', 'score', 'content', 'likes'])

# Inspired by https://www.kaggle.com/therealsampat/scraping-google-play-app-reviews/notebook#Scraping-App-Reviews
for app in app_ids: 
    app_reviews, _ = reviews(
        app,
        lang='en',
        country='us',
        sort=Sort.MOST_RELEVANT,
        count=100
    )
    
    for review in app_reviews: 
            user_name = review['userName']
            score = review['score']
            content = review['content']
            likes = review['thumbsUpCount']

            new_entry = pd.DataFrame({'app_id': [app], 
                                      'user_name': [user_name],
                                      'score': [score],
                                      'content': [content],
                                      'likes': [likes]}, 
                                      columns=['app_id', 'user_name', 'score', 'content', 'likes'])
                                      
            app_reviews_df = app_reviews_df.append(new_entry)

app_reviews_df.to_csv('googleplaystore_reviews.csv')


