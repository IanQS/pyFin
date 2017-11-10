## PyFin ##

Contains the work I have in building an entire ML pipeline with the goal of:

1. Running some predictions on the stock market:
	* classification: whether to buy, hold, or sell the stock in question
	* regression: the predicted change in the stocks price

2. Quantopian backtesting

3. Sentiment analysis of news: politics, financial articles, world events and such to feed to 3) to aid in policy

4. Company clustering: allows us to speed up inference about different industries

5. Reinforcement Learning model: self-tuning trading algorithm

All this will also function as a general timeline for what will be implemented in the process.

I'm still very new to finance but I'm basing most of my explorations, and "traditional" machine learning algorithms off [Analysis of Financial Time Series](http://www.wiley.com/WileyCDA/WileyTitle/productCd-EHEP002380.html) and some theory I'm picking up from [Peter A. Forsyth's Painless Intro to CTF](https://cs.uwaterloo.ca/~paforsyt/agon.pdf)

-------------------------------------------------------------------------------

# Installation
If you use virtual environments (and IMO you should) just run

`mkvirtualenv pyFin -r packages.txt`

assuming you have [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html) installed. Find out more about [virtualenv](https://virtualenv.pypa.io/en/stable/)

you'll need to then install PyTorch from the [PyTorch website](http://pytorch.org/)


-------------------------------------------------------------------------------
# General Notes

1. You'll want to look in each folder for the scripts subfolder which will contain the most updated version of the code. I don't personally like how jupyter handles importing from notebooks so I convert my notebooks to python scripts

2. Obviously don't actually use this to trade.... this is just an experiment
