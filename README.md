# RASA: Russian language support example

An example trying to reuse pre-trained russia language models to propose basic level of transfer learning to increase NLU quality.

## Install

* Install Python 3.7
* `virtualenv venv`
* `source venv/bin/activate`
* `pip3 install -r requirements.txt`

## Train

`export PYTHONPATH=$PWD/custom_nlu:$PYTHONPATH`
`rasa train`


## Verify

### NLU only 

`rasa run --enable-api`

### Shell chat

`rasa shell`

### Used links

1. https://gist.github.com/georgwiese/7c8e8170dfe336d94dbeba67d6b29aa7
1. https://kelijah.livejournal.com/259705.html