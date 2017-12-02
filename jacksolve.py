import urllib.request, json
import operator
with urllib.request.urlopen("https://s3-eu-west-1.amazonaws.com/yoco-testing/tests.json") as url:
    data = json.loads(url.read().decode())


tens = {'J','Q','K'}

# print(data)

def checkFaceCard(cardValue):
	if cardValue in tens:
		return 10
	elif cardValue == 'A':
		return 11
	else:
		return int(cardValue)

def sortCards(hand):
	cardlist = {}
	for idx, card in enumerate(hand):
		cardlist[card[-1:]] = checkFaceCard(card[0:-1])
		cardListSorted = sorted(cardlist.items(), key=operator.itemgetter(1), reverse = True)
		return cardListSorted


# loop through json results
for result in data:
	for key in result:
		playerAHand = sortCards(result['playerA'])
		playerBhand = sortCards(result['playerB'])