# Bitcoinstatistics

## Actual status:
In development

## App description
This is a Python Dash Web App built with PostgreSQL as database. It is deployed on [Heroku](https://www.heroku.com) and you could find it here [https://bitcoinstatistics.herokuapp.com](https://bitcoinstatistics.herokuapp.com).

The App shows an indication how "hot" the term Bitcoin is based on tweets and google statistics. It display the "hotness factor" in a heatmeter based on 24h data.

## Running code local on your Mac
### Installation of PostgreSQL as DATABASE
1. Install [PostgreSQL](https://www.postgresql.org). PostgreSQL is required for deploying to [Heroku](https://www.heroku.com)
2. Install a GUI like [Postico](https://eggerapps.at/postico/) for interaction with database without command line.
3. Check if Heroku it installed with: ```heroku --version```
4. Create an account on Heroku's website
5. After account creation, run in Terminal: ```heroku login```
6. Create database directly in the Postico app or with: ```sudo -u name_of_user createdb bitcoinstats```

### Make Code running locally
1. Clone/ download repository
2. cd into project folder

in Terminal/ CMD:

3. ```pip install virtualenv```   
4. Create virtual environment: ```virtualenv env```
5. Activate virtual environment:   
For macOS: ```source env/bin/activate```   
For Win: Copy in CMD:```"<PATH TO PROJECT>\env\Scripts\activate.bat"``` 
6. Intall dependencies:   
For macOS: ```pip3 install -r requirements.txt```   
For Win: ```pip install -r requirements.txt```   
7. Run app locally:
For macOS: ```python3 app.py```   
For Win: ```python app.py```

### Deploy to Heroku
The App is already deployed on Heroku. Following you find the work flow how I did that. Note: Example below decribes the process of deploying to a production (prod) app called *bitcoinstatistics*. You could add a second staging app (stage) *bitcoinstatistics-stage* with a *stage* remote. For that change "prod" to "stage" or similiar word.

1. ```pip install gunicorn```
2. Create new App on Heroku: ```heroku create <APP NAME (eg bitcoinstatistics)>```
3. Add git remote link to our local git repository. Name our remote as *prod* for the meaning of production: ```git remote add prod https://git.heroku.com/bitcoinstatistics.git```
4. ```heroku config:set APP_SETTINGS=config.ProductionConfig --remote prod```
5. ```heroku addons:create heroku-postgresql:hobby-dev --app bitcoinstatistics```
6. Check if everything is set correct:```heroku config --app bitcoinstatistics```. It should return “APP_SETTINGS” and “DATABASE_URL”
7. ```git push prod master```
8. ```heroku run python manage.py db upgrade --app bitcoinstatistics```
9. On Heroku, you could connect the App with your GitHub account. You could set the master branch as default, and every push to GitHub master will automatically update Heroku.


## Credits
* [Create a web application with Python, Flask, Postgres on Heroku](https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc)
* [Flask by Example – Setting up Postgres, SQLAlchemy](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)   
* [DASH Tutorial](https://dash.plot.ly/)
* [Twitter Developer Documentation](https://developer.twitter.com/#)   
* [Tweepy Documentation](http://docs.tweepy.org/en/v3.4.0/index.html)   
* [Article Tweepy and Twitter from PirateFache](https://piratefache.ch/display-real-time-tweets-on-a-map-with-basemap-and-tweepy/)   
* [YouTube Tutorial by LucidProgramming](https://www.youtube.com/watch?v=wlnx-7cm4Gg)   
* [Capturing Tweets from Twitter's Streaming Endpoints](https://iseverythingstilltheworst.com/blog/2016/05/28/capturing_twitter_streams/)


## Troubleshooting
### Error: Multiple apps in git remotes
It is not an error, but you have to add following code:   
```<COMMAND> --app bitcoinstatistics```