import random


response_drinking="I don't feel like i need to drink or eat anything as I'm a bot created by a human"

def unkown():
    response=["Could you clarify yourself again?: ",
              "..............",
              "Sounds just right",
              "What do you mean by that?"][random.randrange(4)]
    return response