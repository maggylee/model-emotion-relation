#bibliotecas
import urllib  #manutencao (abertura e fechamento) de url
import urlparse #manutencao (parser) de url
import httplib #necessaria para pingar em urls
import string #manutencao de strings (remocao de pontuacoes)
import itertools #remocao de listas duplicadas 
import enchant #dicionario
from bs4 import BeautifulSoup #BS ... nao necessita comentarios

class MyOpener(urllib.FancyURLopener): 
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

def get_server_status_code(url): #da o ping no site
    host, path = urlparse.urlparse(url)[1:3]
    try:
        conn = httplib.HTTPConnection(host,timeout=30)
        conn.request('HEAD', path)
        return conn.getresponse().status
    except StandardError:
        return None
    except httplib.BadStatusLine:
        return None

def check_url(url): #funcao que verifica a validade de uma url
    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return get_server_status_code(url) in good_codes

def hyper_generator(link): #entra em um <link> e ggera uma lista de hyperlinks possiveis
    page = myopener.open(link) #eh feito desta forma pra nao deixar arquivos abertos
    text = page.read()
    page.close()
    return sorted(set([urlparse.urljoin(link, tag['href']) for tag in BeautifulSoup(text).findAll('a', href=True)])) #retorna os links distintos em ordem alfabetica

def text_list_generator(link): #dado um link retorna uma lista com as palavras jah filtadas
    import socket
    socket.setdefaulttimeout(30)
    try:
        page = myopener.open(link) #eh feito desta forma pra nao deixar arquivos abertos
        text = page.read()
        page.close()
        text_list=[elem.encode('utf-8').lower().strip(string.punctuation) for elem in BeautifulSoup(text).get_text().split()] #geracao da lista     
        return [elem for elem in text_list if elem.isalpha() and dictionary.check(elem) and len(elem)>2 and not elem in stopwords] #lista filtrada
    except IOError:
        print 'Error: Link Timeout'
        return []
    except UnicodeError:
        print 'Error: Unicode Error'
        return[]
    

keywords=['love','anger','hate','depression','fear','jealousy','happiness','passion','affection','sadness','grief','rage','aggravation','ecstasy','sorrow','joy','compassion','envy','fright','terror','elation','guilt','excitement','anguish','embarrassment','worry','panic','unhappiness','anxiety','desire','horror','sympathy','shame','lust','disgust','hostility','jubilation','loneliness','delight','pleasure','tenderness','pity','bitterness','disappointment','humiliation','dejection','despair','frustration','hurt','adoration','agony','thrill','fury','remorse','agitation','outrage','resentment','dislike','glee','alienation','distress','enjoyment','relief','gloom','misery','euphoria','bliss','gladness','regret','rejection','pride','gaiety','homesickness','jolliness','nervousness','woe','longing','loathing','satisfaction','hope','insecurity','defeat','dread','fondness','enthusiasm','sentimentality','hopelessness','annoyance','cheerfulness','displeasure','melancholy','glumness','shock','spite','suffering','dismay','exasperation','infatuation','apprehension','caring','isolation','exhilaration','rapture','uneasiness','grouchiness','triumph','joviality','wrath','arousal','attraction','contentment','grumpiness','irritation','ferocity','enthrallment','revulsion','alarm','eagerness','hysteria','liking','neglect','insult','mortification','tenseness','contempt','amazement','amusement','zeal','scorn','zest','astonishment','torment','optimism','vengefulness','surprise'] 
stopwords=['able','about','across','ad','add','adds','ads','adj','after','ago','agitprop','al','all','almost','also','am','among','an','and','ante','any','apr','are','as','at','be','because','been','bi','both','but','by','can','cannot','cant','check','cm','commands','copyright','could','dear','des','did','div','do','does','either','elem','else','em','end','esp','est','etc','even','ever','every','fa','fdr','for','from','get','gm','go','got','had','has','have','he','her','here','hers','him','his','how','however','ii','if','in','input','into','is','it','items ','its','itself','just','lat','least','let','lets','like','likely','login','lo','lot','main','magi','may','me','might','min','most','more','much','must','my','neither','no','nor','not','nun','of','off','often','on','only','or','os','other','our','own','pa','para','per','pm','rather','s','said','say','says','sh','she','should','since','sir','so','some','st','std','such','tag','tags','th','than','that','the','their','them','then','ther','there','these','they','this','thus','tis','to','too','twas','um','us','up','var','variable','very','wants','was','way','ways','wayshell','we','were','what','when','where','which','while','who','whoa','whom','why','will','with','would','ya','yeah','yes','yet','you','your','xi','xvi']
#keywords=['alarm']
dictionary=enchant.Dict('en_US') #definicao do dicionario
max_texts=100 #numero maximo de texto por palavras (condicao de parada)
myopener = MyOpener()
keywords=sorted(keywords)
for keyword in keywords:
    try: #verificacao da existencia de arquivos de texto
        print '{0:15}'.format(keyword),'Verificando os textos existentes'
        file_return=open('text_'+keyword+'.txt','r') #teste para verificar a existencia de textos antigos
        text_list=[[ele for ele in elem.split(',') if  ele.isalpha() and len(ele)>2 and dictionary.check(ele) and not ele in stopwords] for elem in file_return.readlines()] #geracao dos textos
        file_return.close()#fechamento do arquivo de saida
        text_list=[elem for elem in text_list if len(elem)>140 and elem.count(keyword)>0] #filtragem dos elementos invalidos
        print '{0:15}'.format(keyword),'Lista Inicial {0:4d}/{1:4d}'.format(len(text_list),max_texts)for elem2 in enumerate(b): match.extend([(elem1[0],elem2[0]) for elem1 in enumerate(a) if elem1[1]==elem2[1]])
    except IOError:
        print '{0:15}'.format(keyword),'Criando um arquivo de textos'
        file_return=open('text_'+keyword+'.txt','w') #criacao do arquivo de texto
        file_return.close()#fechamento do arquivo de saida
        text_list=[]#criacao da lista inicial
    if len(text_list) < max_texts:
        file_links=open('links_'+keyword+'.txt','r')
        print '{0:15}'.format(keyword),'Gerando a lista de links Validos'
        seed_links=[elem.strip() for elem in file_links.readlines() if not elem.strip().endswith('pdf') and not elem.strip().endswith('php') and not elem.strip().endswith('ppt')  and not elem.strip().endswith('doc') and not elem.strip().endswith('.mp3') and not elem.strip().endswith('.mm4a')  and not elem.strip().endswith('jpg') if check_url(elem.strip())]
        print '{0:15}'.format(keyword),'Gerando os textos iniciais'
        text_list.append([text_list_generator(elem) for elem in seed_links]) #geracao das listas
        text_list=[elem for elem in text_list if len(elem)>140 and elem.count(keyword)>0] #Filtragem das listas 
        text_list.sort()
        text_list=list(text_list for text_list,_ in itertools.groupby(text_list)) #remocao de possiveis duplicadas
        file_links.close()
        links=seed_links #lista com todos os links crawleados (lista final)
        sons=[] #lista com os filhos
        depth=0 #calculo da profundidade do crawling
        while len(text_list)<max_texts : #laco que aumenta a profundidade do craling (para chega no valor maximo de textos crawleados)
            depth+=1 #aumento da profundidade
            count_seed=0 #contador para acompanhamento 
            while (len(text_list) < max_texts) and count_seed < len(seed_links): #laco em todos os links geradores
                hyper=[elem.strip() for elem in hyper_generator(seed_links[count_seed]) if not elem.strip().endswith('pdf') and not elem.strip().endswith('php') and not elem.strip().endswith('ppt')  and not elem.strip().endswith('doc') and not elem.strip().endswith('.mp3') and not elem.strip().endswith('.m4a') and not elem.strip().endswith('jpg')] #filtro de hyperlinks que o BS nao faz parser (imagens entre outras coisas)
                sons.extend(hyper)
                count_hlink=0
                while (len(text_list) < max_texts) and count_hlink < len(hyper): #laco em todos os hyperlinks
                    print '{0:15}'.format(keyword),'Hyperlink [{0:4d}/{1:4d}-{2:4d}/{3:4d}-{4:4d}-{5:4d}/{6:4d}] - '.format(count_hlink+1,len(hyper),count_seed+1,len(seed_links),depth,len(text_list),max_texts),hyper[count_hlink].strip()
                    if check_url(hyper[count_hlink]): #condicao para ser um hyperlink valido
                        text=text_list_generator(hyper[count_hlink]) #geracao do texto
                        if (len(text)>140 and text.count(keyword)>0):
                            text_list.append(text) #adicao de um texto valido
                            print '{0:15}'.format(' '),'Adicionei'
                            print '{0:15}'.format(' '),'Tamanho:{0:4d}\n{1:15} Palavras-Chave{2:4d}'.format(len(text),' ',text.count(keyword))
                            text_list.sort()
                            text_list=list(text_list for text_list,_ in itertools.groupby(text_list)) #remocao de possiveis duplicadas
                            file_return=open('text_'+keyword+'.txt','w') #abertura do arquivo de saida
                            for text in text_list:
                                file_return.write(','.join(map(str,[ele.encode('utf-8') for ele in text])))
                                file_return.write('\n')
                            file_return.close()
                        else: 
                            print '{0:15}'.format(' '),'Error: Texto Invalido'
                            print '{0:15}'.format(' '),'Tamanho:{0:4d}\n{1:15} Palavras-Chave{2:4d}'.format(len(text),' ',text.count(keyword))
                    else: print '{0:15}'.format(' '),'Error: Link Invalido'
                    count_hlink+=1 #contagem dos hyperlinks
                count_seed+=1 #contagem dos links geradores
            seed_links=sorted(set(sons)) #muados as sementes para os filhos
            sons=[] #anulamos a lista de filhos
    else:
        print '{0:15}'.format(keyword),'Crawling desnecessario'
        text_list=text_list[:max_texts]
        file_return=open('text_'+keyword+'.txt','w') #abertura do arquivo de saida
        for text in text_list:
            file_return.write(','.join(map(str,[ele.encode('utf-8') for ele in text])))
            file_return.write('\n')
        file_return.close()
