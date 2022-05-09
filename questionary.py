import questionary

coin = questionary.select(
    "What crypto currency would you like analyse?",
    choices=[
        "BTC",
        "ETH",
        "LUNA1",
        "BNB",
        "ADA"
    ]).ask()

if coin == "BTC":
    weights = [1,0,0,0,0]
elif coin == "ETH":
    weights = [0,1,0,0,0]
elif coin == "LUNA1":
    weights = [0,0,1,0,0]
elif coin == "BNB":
    weights = [0,0,0,1,0]
elif coin == "ADA":
    weights = [0,0,0,0,1]

print(weights)
