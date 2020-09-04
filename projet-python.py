import os
import requests as rq
from bs4 import BeautifulSoup
import json

def ex1():
    r = rq.get(' https://api.github.com/repositories')
    results =r.json()
    fichier = open('listeajout.txt',"w")
    for ajout in results:        
        fichier.write(ajout['name'])
        if ajout['description']:
            fichier.write(' : '+ajout['description']+'\n')
        else:    
            fichier.write(' \n ')
    fichier.close()
    print("done")    
    
def ex2():

    r = rq.get('https://api.github.com/search/repositories?q=sort=stars&order=desc&pushed:>=2020-01-01')
    rep =r.json()
    repertory=rep['items']
    fichier = open('listerep.txt',"w")
    for R in repertory:
        fichier.write(R['name'] )
        if R['description']:
            fichier.write(' : '+R['description'])
        fichier.write(' notes : '+str(R['stargazers_count'])+'\n')
    fichier.close()
    print("done")
