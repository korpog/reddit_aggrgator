# Reddit top links aggregator
Get top links/submissions from a chosen subreddit

### How to run this script
1. Create a [Reddit account](https://www.reddit.com/)

2. Create a [Reddit app](https://www.reddit.com/prefs/apps/)

  * Write name, description of your app
  * Select `script` (Script for personal use. Will only have access to the developers accounts)
  * Redirect uri: `http://localhost:8080`
  
3. Save your `client_id` and `client_secret` somewhere

4. Make a directory for this project

5. Clone this repository
```
git clone https://github.com/korpog/reddit_aggrgator.git
```

6. Install requirements

  * with pip
 
```
pip install -r requirements.txt
```

  * or pipenv
 
```
pipenv install
```

7. Create a `praw.ini` file with the following structure:
```
[aggregator]
username: reddit_username
password: reddit_password
client_id: your_client_id
client_secret: your_client_secret
```

8. Run the script:
```
usage: main.py [-h] [--file] subreddit time results

positional arguments:
  subreddit   name of the subreddit you want to aggregate
  time        time filter for your query (allowed arguments: hour, day, week,
              month, year, all)
  results     number of results you want to receive (max=100)

optional arguments:
  -h, --help  show this help message and exit
  --file      enabling this flag will write results in an output file
```

e.g running `python main.py --file worldnews day 5` yields following results:
```
German Politicians Call Trump's Ambassador A 'Brat' And 'Total Diplomatic Failure,' Demand Immediate Expulsion :: 19 March 2019 22:05:13
https://www.newsweek.com/germany-trump-ambassador-brat-failure-1368713

Man who tackled 'Eggboy' has outstanding warrant on charges relating to church incident :: 20 March 2019 00:28:40
https://www.abc.net.au/news/2019-03-20/eggboy-thug-neil-erikson-wanted/10916948

Canada's oldest rape crisis centre stripped of city funding for refusing to accept trans women. :: 19 March 2019 20:16:59
https://nationalpost.com/news/canada/canadas-oldest-rape-crisis-centre-stripped-of-city-funding-for-refusing-to-accept-trans-women

EU regulators fine Google 1.49 billion euros for blocking advertising rivals :: 20 March 2019 11:11:53
https://www.reuters.com/article/us-eu-google-fine/eu-regulators-fine-google-1-49-billion-euros-for-blocking-advertising-rivals-idUSKCN1R117E?il=0

Video Released of Israeli Soldiers Laughing while Beating Palestinians in Custody :: 19 March 2019 21:30:27
http://www.palestinechronicle.com/video-released-of-israeli-soldiers-laughing-while-beating-palestinians-in-custody-video
```
