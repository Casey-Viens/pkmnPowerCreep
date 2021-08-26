import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#function to calculate stats based on math operation
def calcmath(ver, stat, mathop):
    if(ver == 'all'):
        results = []
        results.append(mathop(gen1[stat]))
        results.append(mathop(gen2[stat]))
        results.append(mathop(gen3[stat]))
        results.append(mathop(gen4[stat]))
        results.append(mathop(gen5[stat]))
        results.append(mathop(gen6[stat]))
        results.append(mathop(gen7[stat]))
        return results
    else:
        results = []
        results.append(mathop(gen1_10[stat]))
        results.append(mathop(gen2_10[stat]))
        results.append(mathop(gen3_10[stat]))
        results.append(mathop(gen4_10[stat]))
        results.append(mathop(gen5_10[stat]))
        results.append(mathop(gen6_10[stat]))
        results.append(mathop(gen7_10[stat]))
        return results 

#function to call math function for each stat line and store in dictionary
def getstats(ver, math):
    dict = {
        "hp": calcmath(ver, 'hp', math),
        "atk": calcmath(ver, 'attack', math),
        "spatk": calcmath(ver, 'sp_attack', math),
        "def": calcmath(ver, 'defense', math),
        "spdef": calcmath(ver, 'sp_defense', math),
        "spd": calcmath(ver, 'speed', math),
        "dmg_eff": calcmath(ver, 'avg_dmg_eff', math),
        "base": calcmath(ver, 'base_total', math)
    }
    return dict

#function to draw graphs
def drawgraph(title, dict):
    fig, axs = plt.subplots(2,4)
    fig.suptitle(title)
    fig.canvas.set_window_title(title)
    axs[0,0].bar(gen_labels, dict['hp'])
    axs[0,0].set_title('HP')
    axs[1,0].bar(gen_labels, dict['spd'])
    axs[1,0].set_title('Speed')
    axs[0,1].bar(gen_labels, dict['atk'])
    axs[0,1].set_title('Attack')
    axs[1,1].bar(gen_labels, dict['def'])
    axs[1,1].set_title('Defense')
    axs[0,2].bar(gen_labels, dict['spatk'])
    axs[0,2].set_title('Special Attack')
    axs[1,2].bar(gen_labels, dict['spdef'])
    axs[1,2].set_title('Special Defense')
    axs[0,3].bar(gen_labels, dict['base'])
    axs[0,3].set_title('Base Stats')
    axs[1,3].bar(gen_labels, dict['dmg_eff'])
    axs[1,3].set_title('Damage Effectiveness')
    axs[1,3].set_ylim(.6,1.5)
    return

def calc_dmg_eff(gen):
    gen['avg_dmg_eff']=(
        gen['against_bug']+
        gen['against_dark']+
        gen['against_dragon']+
        gen['against_electric']+
        gen['against_fairy']+
        gen['against_fight']+
        gen['against_fire']+
        gen['against_flying']+
        gen['against_ghost']+
        gen['against_grass']+
        gen['against_ground']+
        gen['against_ice']+
        gen['against_normal']+
        gen['against_poison']+
        gen['against_psychic']+
        gen['against_rock']+
        gen['against_steel']+
        gen['against_water']
        )/18
    return 

def tiercount(gen):
    uber = gen[gen['Tier']=='Uber']
    ou = gen[gen['Tier']=='OU']
    uubl = gen[gen['Tier']=='UUBL']
    uu = gen[gen['Tier']=='UU']
    rubl = gen[gen['Tier']=='RUBL']
    ru = gen[gen['Tier']=='RU']
    nubl = gen[gen['Tier']=='NUBL']
    nu = gen[gen['Tier']=='NU']
    publ = gen[gen['Tier']=='PUBL']
    pu = gen[gen['Tier']=='PU']
    lc = gen[gen['Tier']=='LC']
    lcuber = gen[gen['Tier']=='LCUber']
    nfe = gen[gen['Tier']=='NFE']

    tiercounts = []
    tiercounts.append(uber['name'].count())
    tiercounts.append(ou['name'].count()+uubl['name'].count())
    tiercounts.append(uu['name'].count()+rubl['name'].count())
    tiercounts.append(ru['name'].count()+nubl['name'].count())
    tiercounts.append(nu['name'].count()+publ['name'].count())
    tiercounts.append(pu['name'].count())
    tiercounts.append(lc['name'].count())
    tiercounts.append(lcuber['name'].count())
    tiercounts.append(nfe['name'].count())
    return tiercounts

#Reading in the dataset
pokemon = pd.read_csv('pokemon.csv')

pokemon_smogon = pd.read_csv('pokemon-data1.csv')

#List for x-axis labels
gen_labels = ['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6', 'Gen 7']

#Removing Legendaries from the data
pokemon_noleg = pokemon[pokemon['is_legendary']==0]

#Merges the Smogon data with the base stats data in one array
poke = pokemon_noleg.join(pokemon_smogon.set_index('Name'), on='name')

#test for checking tier of mons
#test = poke[poke['name']=='Wingull']
#print(test['Tier'])

#Creating Seperate Arrays for each gen
gen1 = poke[poke['generation']==1]
gen2 = poke[poke['generation']==2]
gen3 = poke[poke['generation']==3]
gen4 = poke[poke['generation']==4]
gen5 = poke[poke['generation']==5]
gen6 = poke[poke['generation']==6]
gen7 = poke[poke['generation']==7]

calc_dmg_eff(gen1)
calc_dmg_eff(gen2)
calc_dmg_eff(gen3)
calc_dmg_eff(gen4)
calc_dmg_eff(gen5)
calc_dmg_eff(gen6)
calc_dmg_eff(gen7)

#Creating Seperate Arrays for each gen's top 10 percent based on total base stats
gen1_10 = gen1.nlargest(int(len(gen1)*.1),'base_total')
gen2_10 = gen2.nlargest(int(len(gen2)*.1),'base_total')
gen3_10 = gen3.nlargest(int(len(gen3)*.1),'base_total')
gen4_10 = gen4.nlargest(int(len(gen4)*.1),'base_total')
gen5_10 = gen5.nlargest(int(len(gen5)*.1),'base_total')
gen6_10 = gen6.nlargest(int(len(gen6)*.1),'base_total')
gen7_10 = gen7.nlargest(int(len(gen7)*.1),'base_total')

poke_tiers = tiercount(poke)
gen1_tiers = tiercount(gen1)
gen2_tiers = tiercount(gen2)
gen3_tiers = tiercount(gen3)
gen4_tiers = tiercount(gen4)
gen5_tiers = tiercount(gen5)
gen6_tiers = tiercount(gen6)
gen7_tiers = tiercount(gen7)

tierdict = {
    'uber': (gen1_tiers[0]/gen1['name'].count(), gen2_tiers[0]/gen2['name'].count(), gen3_tiers[0]/gen3['name'].count(), gen4_tiers[0]/gen4['name'].count(), gen5_tiers[0]/gen5['name'].count(), gen6_tiers[0]/gen6['name'].count(), gen7_tiers[0]/gen7['name'].count()),
    'ou': (gen1_tiers[1]/gen1['name'].count(), gen2_tiers[1]/gen2['name'].count(), gen3_tiers[1]/gen3['name'].count(), gen4_tiers[1]/gen4['name'].count(), gen5_tiers[1]/gen5['name'].count(), gen6_tiers[1]/gen6['name'].count(), gen7_tiers[1]/gen7['name'].count()),
    'uu': (gen1_tiers[2]/gen1['name'].count(), gen2_tiers[2]/gen2['name'].count(), gen3_tiers[2]/gen3['name'].count(), gen4_tiers[2]/gen4['name'].count(), gen5_tiers[2]/gen5['name'].count(), gen6_tiers[2]/gen6['name'].count(), gen7_tiers[2]/gen7['name'].count()),
    'ru': (gen1_tiers[3]/gen1['name'].count(), gen2_tiers[3]/gen2['name'].count(), gen3_tiers[3]/gen3['name'].count(), gen4_tiers[3]/gen4['name'].count(), gen5_tiers[3]/gen5['name'].count(), gen6_tiers[3]/gen6['name'].count(), gen7_tiers[3]/gen7['name'].count()),
    'nu': (gen1_tiers[4]/gen1['name'].count(), gen2_tiers[4]/gen2['name'].count(), gen3_tiers[4]/gen3['name'].count(), gen4_tiers[4]/gen4['name'].count(), gen5_tiers[4]/gen5['name'].count(), gen6_tiers[4]/gen6['name'].count(), gen7_tiers[4]/gen7['name'].count()),
    'pu': (gen1_tiers[5]/gen1['name'].count(), gen2_tiers[5]/gen2['name'].count(), gen3_tiers[5]/gen3['name'].count(), gen4_tiers[5]/gen4['name'].count(), gen5_tiers[5]/gen5['name'].count(), gen6_tiers[5]/gen6['name'].count(), gen7_tiers[5]/gen7['name'].count()),
    'lc': (gen1_tiers[6]/gen1['name'].count(), gen2_tiers[6]/gen2['name'].count(), gen3_tiers[6]/gen3['name'].count(), gen4_tiers[6]/gen4['name'].count(), gen5_tiers[6]/gen5['name'].count(), gen6_tiers[6]/gen6['name'].count(), gen7_tiers[6]/gen7['name'].count()),
    'lcuber': (gen1_tiers[7]/gen1['name'].count(), gen2_tiers[7]/gen2['name'].count(), gen3_tiers[7]/gen3['name'].count(), gen4_tiers[7]/gen4['name'].count(), gen5_tiers[7]/gen5['name'].count(), gen6_tiers[7]/gen6['name'].count(), gen7_tiers[7]/gen7['name'].count()),
    'nfe': (gen1_tiers[8]/gen1['name'].count(), gen2_tiers[8]/gen2['name'].count(), gen3_tiers[8]/gen3['name'].count(), gen4_tiers[8]/gen4['name'].count(), gen5_tiers[8]/gen5['name'].count(), gen6_tiers[8]/gen6['name'].count(), gen7_tiers[8]/gen7['name'].count())
}

tier_labels = ['Uber', 'OU', 'UU', 'RU', 'NU', 'PU', 'LC', 'LCUber', 'NFE']

fig, axs = plt.subplots(2,5)
fig.suptitle('Tiers')
fig.canvas.set_window_title('Tiers')
axs[0,0].bar(tier_labels, poke_tiers)
axs[0,0].set_title('Tier Totals')
axs[1,0].bar(gen_labels, tierdict['uber'])
axs[1,0].set_title('Uber')
axs[0,1].bar(gen_labels, tierdict['ou'])
axs[0,1].set_title('OU + UUBL')
axs[1,1].bar(gen_labels, tierdict['uu'])
axs[1,1].set_title('UU + RUBL')
axs[0,2].bar(gen_labels, tierdict['ru'])
axs[0,2].set_title('RU + NUBL')
axs[1,2].bar(gen_labels, tierdict['nu'])
axs[1,2].set_title('NU + PUBL')
axs[0,3].bar(gen_labels, tierdict['pu'])
axs[0,3].set_title('PU')
axs[1,3].bar(gen_labels, tierdict['nfe'])
axs[1,3].set_title('NFE')
axs[0,4].bar(gen_labels, tierdict['lc'])
axs[0,4].set_title('LC')
axs[1,4].bar(gen_labels, tierdict['lcuber'])
axs[1,4].set_title('LC Uber')

avgdict = getstats('all', lambda stat: stat.mean())
meddict = getstats('all', lambda stat: np.median(stat))
mindict = getstats('all', lambda stat: stat.min())
maxdict = getstats('all', lambda stat: stat.max())

avgdict_10 = getstats('top', lambda stat: stat.mean())
meddict_10 = getstats('top', lambda stat: np.median(stat))
mindict_10 = getstats('top', lambda stat: stat.min())
#maxdict_10 = getstats('top', lambda stat: stat.max())

drawgraph('Average', avgdict)
drawgraph('Median', meddict)
drawgraph('Min', mindict)
drawgraph('Max', maxdict)

drawgraph('Average Top 10%', avgdict_10)
drawgraph('Median Top 10%', meddict_10)
drawgraph('Min Top 10%', mindict_10)
#drawgraph('Max Top 10%', maxdict_10)


plt.show()