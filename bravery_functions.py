# -*- coding: utf-8 -*-

import urllib.request, json, random

def make_data(remove5, remove_traits, details):
    # this is to open file, making website think we are coming from normal browser so it lets us in
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    url = "https://raw.communitydragon.org/latest/cdragon/tft/en_us.json"

    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = json.load(response)['sets'] # load data into dict

    champ_info = data[list(data)[-1]]['champions']

    Origins = {}
    Classes = {}
    multi_class = []
    
    for champion in champ_info:
        name = champion['name']
        traits = champion['traits']
        cost = champion['cost']
        
        if cost*remove5!=5 and len(traits)==2:
            Origin = traits[0]
            Class = traits[1]
            
            if Origin not in Origins.keys():
                Origins[Origin] = [name]
            else:
                Origins[Origin].append(name)
                
            if Class not in Classes.keys():
                Classes[Class] = [name]
            else:
                Classes[Class].append(name)
                
        elif cost*remove5!=5 and len(traits)>2:
            multi_class.append([name, traits])
            
        elif details==True:
            print(f'skipped champion - {name}')
        
    for entry in multi_class:
        # this code assumes that if trait is unique to champions with 3 or more classes it is an Origin
        name, traits = entry
        for trait in traits:
            try:
                Classes[trait].append(name)
            except:
                try:
                    Origins[trait].append(name)
                except:
                    Origins[trait] = [name]
    
    # Remove any unwanted traits
    for trait in remove_traits:
        try:
            del Origins[trait]
        except:
            try:
                del Classes[trait]
            except:
                return(0, 'Remove trait error - trait not found, check spelling')

    return(Origins, Classes)

def make_team():
    ori = random.choice(list(Origins))
    trait = random.choice(list(Classes))
    return (ori, trait, random.choice(Classes[trait]+Origins[ori]))
    
    
def update_lists(remove5 = True, remove_traits=[], details=False):
    global Origins
    global Classes 
    Origins, Classes = make_data(remove5, remove_traits, details)

        