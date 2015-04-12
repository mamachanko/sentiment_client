import datetime
import json

import gevent
import lymph


class SentimentClient(lymph.Interface):

    crunching = lymph.proxy('crunching')

    @lymph.event('tweet.received')
    def on_tweet_received(self, event):
        tweet = json.loads(event.body)
        self._print_lines(u'Tweet received: {}'.format(tweet['text']))

    def on_start(self):
        super(SentimentClient, self).on_start()
        self._loop = gevent.spawn(self.loop)

    def loop(self):
        while True:
            last_tweet = self.crunching.recent(limit=1)[0]
            output = (
                unicode(datetime.datetime.now()),
                u'Tweet count: {}'.format(self.crunching.count()),
                u'Avg sentiment: {}'.format(self.crunching.avg()),
                u'Last tweet: "{}"'.format(last_tweet['text']),
            )
            self._print_lines(*output)
            gevent.sleep(1)

    def _print_lines(self, *lines):
        lines += (u'-' * 32,)
        print(u'\n'.join(lines))

    def on_stop(self, *args, **kwargs):
        self._loop.kill()
        super(SentimentClient, self).on_stop(*args, **kwargs)
