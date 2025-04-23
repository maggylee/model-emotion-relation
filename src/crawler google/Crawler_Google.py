#!/usr/bin/python

import urllib2
import json
import pprint

keywords=['love','anger','hate','depression','fear','jealousy','happiness','passion','affection','sadness','grief','rage','aggravation','ecstasy','sorrow','joy','compassion','envy','fright','terror','elation','guilt','excitemen','anguish','embarrassment','worry','panic','unhappiness','anxiety','desire','horror','sympathy','shame','lust','disgust','hostility','jubilation','loneliness','delight','pleasure','tenderness','pity','bitterness','disappointment','humiliation','dejection','despair','frustration','hurt','adoration','agony','thrill','fury','remorse','agitation','outrage','resentment','dislike','glee','alienation','distress','enjoyment','relief','gloom','misery','euphoria','bliss','gladness','regret','rejection','pride','gaiety','homesickness','jolliness','nervousness','woe','longing','loathing','satisfaction','hope','insecurity','defeat','dread','fondness','enthusiasm','sentimentality','hopelessness','annoyance','cheerfulness','displeasure','melancholy','glumness','shock','spite','suffering','dismay','exasperation','infatuation','apprehension','caring','isolation','exhilaration','rapture','uneasiness','grouchiness','triumph','joviality','wrath','arousal','attraction','contentment','grumpiness','irritation','ferocity','enthrallment','revulsion','alarm','eagerness','hysteria','liking','neglect','insult','mortification','tenseness','contempt','amazement','amusement','zeal','scorn','zest','astonishment','torment','optimism','vengefulness','surprise']

#Key/Busca - Conta Lucas
#'AIzaSyA6pMUS0G-VWvFPsJfTluRyOuItWNJT458'
#'012812793397482785795:vt6l5dac1am'
#Key/Busca - Conta Daniel
#'AIzaSyBq67HWLb1aTdmtE3v0pnI4iKd_uaYy0DI'
#009855774861628117174:g7uv4zptiae
#Key/Busca - Conta Martha
#'AIzaSyAMz_EE1kowBm2F6MmKOjFWrt9bGkI0vos'
#013992414622699323096:56bidb5h7a0 
#Key/Busca - Conta Amanda
#AIzaSyCJTYE5EHd5FPNxcspuUP9ofIcfQvDYJxE
#015582923721677434030:irgahjjxcx8 

chaves=[('012812793397482785795:vt6l5dac1am','AIzaSyA6pMUS0G-VWvFPsJfTluRyOuItWNJT458'),('013992414622699323096:56bidb5h7a0','AIzaSyAMz_EE1kowBm2F6MmKOjFWrt9bGkI0vos'),('015582923721677434030:irgahjjxcx8','015582923721677434030:irgahjjxcx8'),('009855774861628117174:g7uv4zptiae','AIzaSyBq67HWLb1aTdmtE3v0pnI4iKd_uaYy0DI')]

def google_catch(keyword,links,startIndex,custom_search,key): #crawler da busca do google
    while startIndex<100: 
        name_url='https://www.googleapis.com/customsearch/v1?key='+key+'&cx='+custom_search+'&hl=en&num=10&start='+str(startIndex)+'&q='+keyword+'&pws=0'
        print '[',str(startIndex).strip(),'->',str(startIndex+9).strip(),']'
        try: #condicao para o google deixar eu crawlear
            data=urllib2.urlopen(name_url)
            data=json.load(data)
            for elem in data['items']: links.append((str(elem['link'])).strip())
            print 'Crawled!'
            startIndex+=10
        except IOError:
            print 'Too mutch requisitions ... Google angry >.<'
            for x in range(10): links.append('')
            startIndex+=10

def print_exit(file_name,links): #escrita no arquivo de saida
    file_exit=open(file_name,'w')
    links=[elem.strip() for elem in links if len(elem)>0]
    for elem in links:
        file_exit.write(str(elem).strip())
        file_exit.write('\n')    
    file_exit.close()

max_links=100 #tamanho maximo links por palavra
keywords=sorted(keywords)  #organizamos as palavras em ordem alfabetica
for data in chaves:
    for keyword in keywords:
        print 'Keyword:',keyword.strip()
        file_name='links_'+keyword+'.txt'
        try: #caso em que o arquivo exista
            file_old_links=open(file_name,'r')
            links=file_old_links.readlines()
            file_old_links.close()
            links=[elem.strip() for elem in links if len(elem)>0]
            if len(links) < max_links:
                print 'Completando elementos'
                while len(links) < max_links:
                    startIndex=len(links)+1
                    google_catch(keyword,links,startIndex,data[0],data[1])
                    print_exit(file_name,links)
                else:
                    print 'Arquivo completo'
        except IOError:
            print 'Gerando arquivo'
            links=[] #inicialmente a lista de links e nula
            while len(links) < max_links:
                startIndex=1
                google_catch(keyword,links,startIndex,data[0],data[1])
            print_exit(file_name,links)
