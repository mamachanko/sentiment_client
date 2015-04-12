# sentiment_client
A simple shell client for github.com/mamachanko/sentiment

It's listening for incomming tweets and outputs general information every
second.

## Auto-magical installation

``` shell
curl git.io/vvfK5 | sh
```

You need to have installed:
 * git
 * pip
 * virtualenv

## Manual installation

Clone this repository
``` shell
git clone git@github.com/mamachanko/sentiment_client
```

Go into its directory
``` shell
cd sentiment_client
```

Make sure that both the registry and event-system point to mamachanko:
``` shell
cat .lymph.yml
```

Create a virtualenv
```
virtualenv venv
```
If you don't have virtualenv you can install it with `pip install virtualenv`.
If you don't have `pip`, ask for help :)

Install lymph
``` shell
pip install git+ssh://git@github.com/deliveryhero/lymph@master#egg=lymph 
```

Run the client
```
PYTHONPATH=. lymph node
```

or find other services:
``` shell
lymph discover
```
