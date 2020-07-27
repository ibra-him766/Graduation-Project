#!/usr/bin/env python
# coding: utf-8

# # Step 1: Import important libraries

# In[1]:


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd


# In[ ]:





# # Step 2: Twitter API user credentials 

# In[2]:


#Variables that contains the user credentials to access Twitter API 
consumer_key        = 'hfmFEL425N7WBBGHEF7EVyO69'
consumer_secret = 'vtcwfXONTGnOO991q80rphRBhrDwenYYS6KbMBPhm0yZgCGYgc'
access_token        = '913380925601394693-2X9lT5IlEnv1LKPUe0zG1NdQcANPMv4'
access_token_secret = 'YLuAVg7LBqz3Nq2WiY74ia4pHqe1eQiqXGKVKtg7B6TE1'


# # Step 3: Establish contection to the API

# In[3]:


class FileWriteListener(StreamListener):

    def __init__(self):
        super(StreamListener, self).__init__()
        self.save_file = open('tweets.json','w')
        self.tweets = []

    def on_data(self, tweet):
        self.tweets.append(json.loads(tweet))
        self.save_file.write(str(tweet))

    def on_error(self, status):
        print(status)
        return True


# In[4]:


#This handles Twitter authetification and the connection to Twitter Streaming API

l = FileWriteListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)


# # Step 4: Stream Twitter data

# In[5]:


#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    
stream.filter(track=[u'أوت باك ستيك هاوس',
u'أسكودار ستيك هاوس',
u'سلطان ستيك هاوس',
u'سبرد',
u'تكساس رود هاوس',
u'تكساس رودهاوس',
u'ستِيك هاوس',
u'@SteakhouseKSA',
u'ستيك هاوس',
u'ستِيك هاس',
u'سِتيك هاوس',
u'ستيِك هاوس',
u'باك يارد جريل',
u'@backyardgrillsa',
u'برجر فيول',
u'@Burgerfuel_KSA',
u'برجرفيول',
u'برقر فيول',
u'برغر فيول',
u'برغرفيول',
u'بورتر هاوس',
u'@PORTERHOUSE_SA',
u'ستِيك هاوس',
u'@SteakhouseKSA',
u'ستيك هاوس',
u'ستِيك هاس',
u'سِتيك هاوس',
u'ستيِك هاوس',
u'فايف جايز',
u'@FiveGuysBahrain',
u'فايف قايز',
u'واقيو برجر',
u'واجيو برجر',
u'@Wagyu_burger',
u'واقيو برقر',
u'واقيو برغر',
u'مطعم سولت',
u'برغر بوتيك',
u'@BurgerBoutique_',
u'برقر بوتيك',
u'ريل برجر',
u'@real_burger_sa',
u'ريل برقر',
u'هامبرغيني',
u'هامبرقيني',
u'همبرغيني',
u'هابرغيني',
u'@HamburginiSA',
u'هامبرجيني',
u'سكشن-بي',
u'سكشن بي',
u'@sectionb_sa',
u'32 قرمب ',
u'@32grimp',
u'شرمبشاك',
u'@shrimpshacksa',
u'اسماك دله',
u'اسماك دلة',
u'شريمبلس ',
u'@shrimplus',
u'سمكيات',
u'بي.اف. تشانغز',
u'مطعم طوكيو',
u'مطعم نوزومي',
u'نزومي',
u'مطعم يوكاري',
u'@Yokari_Riyadh',
u'بنيهانا',
u'سوشي يوشي',
u'يمي ووك',
u'مطعم ووك تو ووك',
u'مطعم ووك تو والك',
u'@WoktoWalkMe',
u'نودلز فاكتوري',
u'@noodlesfactory1',
u'ووك كونج',
u'مايسترو بيتزا',
u'@MaestroPizzaKSA',
u'ماسترو بيتزا',
u'مايستر بيتزا',
u'مايستروبيتزا',
u'مطعم مايسترو بيتزا',
u'"بليز بيتزا"',
u'ليتس بيتزا',
u'@Letspizza_sa',
u'لتس بيتزا',
u'بيتزاراتي',
u'@pizzaratti',
u'مطعم بوقا',
u'صب واي',
u'مطعم صب واي',
u'@SubwaySaudi',
u'مطعم صبواي',
u'مطعم ماما نوره',
u'مطعم مامانوره',
u'مامانوره',
u'ويتش وتش',
u'@WhichWichOman',
u'مطعم أسكودار ستيك هاوس',
u'مطعم تكساس رود هاوس',
u'مطعم ستيك هاوس',
u'مطعم برقر فيول',
u'مطعم بورتر هاوس',
u' مطعم بورترهاوس',
u'مطعم فايف جايز',
u'مطعم واقيو برجر',
u'مطعم ريل برقر',
u'مطعم واقيو برقر',
u'مطعم سولت',
u'مطعم برقر بوتيك',
u'مطعم برغر بوتيك',
u'مطعم برجر بوتيك',
u'مطعم ريل برجر',
u'مطعم هامبرغيني',
u' مطعم همبرغيني',
u'مطعم سكشن-بي',
u'شرمب شاك',
u'مطعم شرمبشاك',
u'مطعم 32 قرمب ',
u' مطعم 32 قرمب',
u'مطعم اسماك دله',
u'مطعم بي.اف. تشانغز',
u'مطعم شرمب شاك',
u'مطعم نوزومي',
u' مطعم نزومي',
u'مطعم طوكيو',
u'بي اف تشانغز',
u' بنيهانا',
u'مايسترو بيتزا',
u'سوشي يوشي',
u'مطعم مايسترو بيتزا',
u'صب واي',
u'مطعم صب واي',
u'مطعم بوقا',
u'مطعم ماما نوره'])
    


# # Step 4: Read Twitter data

# In[ ]:


# read the file stored
tweets_data_path = 'tweets.json'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue




# create a list to capture all of the tweets
tweets_list = []

for tweet in tweets_data:
    
        tweet_id = tweet['id']
        
        whole_tweet = tweet['text']
        
        lang= tweet['lang']
        
        if tweet['place'] != None:
            country = tweet['place']['country'] 
        else:
            country= 'None'
        
        only_url = whole_tweet[whole_tweet.find('https'):]
        url = only_url
        
        favorite_count = tweet['favorite_count']
        
        retweet_count = tweet['retweet_count']
        
        created_at = tweet['created_at']
        
        whole_source = tweet['source']
        
        only_device = whole_source[whole_source.find('rel="nofollow">') + 15:-4]
        source = only_device
        
        retweeted_status = tweet['retweeted_status'] = tweet.get('retweeted_status', 'Original tweet')
        if retweeted_status != 'Original tweet':
            retweeted_status = 'This is a retweet'

        tweets_list.append({'tweet_id': str(tweet_id),
                            'text' : str(whole_tweet),
                            'lang' : str(lang),
                            'country' : str(country),
                             'favorite_count': int(favorite_count),
                             'retweet_count': int(retweet_count),
                             'url': url,
                             'created_at': created_at,
                             'source': source,
                             'retweeted_status': retweeted_status,
                            })

#create data frame for tweets
tweets = pd.DataFrame(tweets_list, columns = ['tweet_id','text','lang','country', 
                                              'favorite_count', 'retweet_count', 'created_at',
                                              'source', 'retweeted_status', 'url'])
