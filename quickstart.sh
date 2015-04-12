# clone sentiment_client
git clone git@github.com:mamachanko/sentiment_client.git

# move into the directory
cd sentiment_client

# create a virtualenv and activate it
virtualenv venv

# install lymph
pip install git+ssh://git@github.com/deliveryhero/lymph@master#egg=lymph 

# run the service
PYTHONPATH=. lymph node
