import datetime

import gevent
import lymph


class SentimentClient(lymph.Interface):

    crunching = lymph.proxy('crunching')

    @lymph.event('tweet.received')
    def on_tweet_received(self, event):
        print 'Tweet received: "{}"'.format(event.body)

    def on_start(self):
        super(SentimentClient, self).on_start()
        self._loop = gevent.spawn(self.loop)

    def loop(self):
        while True:
            print datetime.datetime.now()
            print u'Tweet count: {}'.format(self.crunching.count())
            print u'Avg sentiment: {}'.format(self.crunching.avg())
            last_tweet = self.crunching.recent(limit=1)[0]
            print u'Last tweet: {}'.format(last_tweet['text'])
            print 
            gevent.sleep(1)

    def on_stop(self, *args, **kwargs):
        self._loop.kill()
        super(SentimentClient, self).on_stop(*args, **kwargs)
