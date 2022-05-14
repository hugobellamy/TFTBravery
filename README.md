# TFTBravery
This code allows for a tft ultimate bravery team to be made using python. This can be implemented into a discord bot, as shown in discord_bot_example.py. The team data is loaded in the file bravery_functions.py, using the make_data function. This function takes two arguments that effect the game:  
- remove5 - this ignores 5 cost units - causing 5 cost only traits and 5 cost carries are not possible to get - this generally makes the game better as 5 cost traits gives you too few units and a 5 cost carry can be too strong as it allows you free use of items  
- remove_traits - a list of traits to ignore - can be good if players agree a certain trait should not be used - for example you may wish to remove rival in the current set

Once the team data is loaded, team selection can be made using the make_team() function. A simple example is shown in basic_example.py. 

# TFT ultimate Bravery Rules  
Basic Rules  
1 - You are only allowed to buy champions that belong to the origin/class you are assigned to!  
2 - You are allowed to take any champion you want in carousel, so you can expand your team buffs!  
3 - You have to always buy your king if it's possible and he must be on the field!  
4 - When you own your king, he has to have the most items  
5 - If caught cheating you must sell all your units except 1  

Notes   
- Thieves gloves counts as 1 item
- A unit may have the same number of items as the king (but not more)
- You can buy extra units to prevent losing minion rounds, but these must be sold before the next player combat


