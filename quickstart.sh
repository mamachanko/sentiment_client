git clone git@github.com:mamachanko/sentiment_client.git
cd sentiment_client
virtualenv venv
source venv/bin/activate
pip install git+ssh://git@github.com/deliveryhero/lymph@master#egg=lymph 
PYTHONPATH=. lymph node
