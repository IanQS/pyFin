## PyFin ##

Contains the work I have in building an entire ML pipeline with the goal of

1) Running some predictions on the stock market:
	* classification: whether to buy, hold, or sell the stock in question
	* regression: the predicted change in the stocks price

2) Sentiment analysis of news: politics, financial articles, world events and such to feed to 3) to aid in policy

3) Company clustering: allows us to speed up inference about different industries

4) Reinforcement Learning model: self-tuning trading algorithm

I'm still very new to finance but I'm basing most of my explorations, and "traditional" machine learning algorithms off [Analysis of Financial Time Series](http://www.wiley.com/WileyCDA/WileyTitle/productCd-EHEP002380.html)

-------------------------------------------------------------------------------

# Installation
If you use virtual environments (and IMO you should) just run

`mkvirtualenv dearlyBeloved -r packages.txt`

you'll need to then install PyTorch from the [PyTorch website](http://pytorch.org/)
