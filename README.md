# RASA: Russian language support example

An example trying to reuse pre-trained russia language models to propose basic level of transfer learning and increase language model quality.

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