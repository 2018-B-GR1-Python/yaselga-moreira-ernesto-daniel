from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#  API CREDENTIALS

ckey = "XTwJNYD8b9bekoIvJ4q5j1JUf"
csecret = "cmIe1H37tPXYgYqRKa5PyeQKhCkc62f3BDgaquRIEpCJlHBPTY"
atoken = "1012062505617805312-Y2wGE78wLUweV4zYVBLK0ogoeAOmdd"
asecret = "zC3CggazLLUcHJhTjl7la95m70ZeVPK4QqGytVYJNQnMu"

# UBICACIONES en CSV
# http://boundingbox.klokantech.com/
USA     =   [-120.3,29.7,-87.8,46.3]
CHINA   =   [73.5,8.8,134.8,53.6]
TAIWAN  =   [119.82,21.77,122.24,25.52]
ECUADOR =   [-92.21,-5.02,-75.19,1.88]
class listener(StreamListener):
    def on_data(self, data):
        with open('tweets_USA_nvidia.json', 'a') as diccionario:
            diccionario.write(data+",")
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

filters = [
    'Bitcoin',
    'Crypto',
    'nvidia'
]

twitterStream.filter(locations=USA, track=filters)