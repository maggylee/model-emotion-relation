#bibliotecas
import numpy as np #numpython

#programa principal
keywords=['acceptance','adoration','affection','aggravation','agitation','agony','alarm','alienation','amusement','anger','anguish','annoyance','anticipation','anxiety','apprehension','arousal','attraction','aversion','bitterness','bliss','compassion','contempt','courage','defeat','dejection','delight','depression','desire','despair','disappointment','disgust','dislike','dismay','displeasure','distress','dread','eagerness','ecstasy','elation','embarrassment','enthusiasm','envy','euphoria','exasperation','excitement','exhilaration','fear','ferocity','fondness','fright','frustration','fury','gaiety','gladness','glee','gloom','glumness','grief','grouchiness','grumpiness','guilt','happiness','hate','homesickness','hope','hopelessness','horror','hostility','humiliation','hurt','hysteria','infatuation','insecurity','insult','interest','irritation','isolation','jealousy','jolliness','joviality','joy','jubilation','liking','loathing','loneliness','love','lust','melancholy','misery','mortification','neglect','optimism','outrage','pain','panic','passion','pity','pleasure','pride','rage','rapture','regret','rejection','relief','remorse','resentment','revulsion','sadness','satisfaction','scorn','shame','shock','sorrow','spite','suffering','surprise','sympathy','tenderness','tenseness','terror','thrill','torment','triumph','uneasiness','unhappiness','vengefulness','woe','wonder','worry','wrath','zeal','zest'] #palavras chave
size=[5,20] #tamanhos usados para as bags
for i in size:
    simi_matrix=np.loadtxt('Sergey_132words_context'+str(i)+'.txt') #leitura dos dados do fonta
    file_return=open('Data_Similarity_Full_'+str(i)+'.txt','w')
    file_return.write('{0:8}\t'.format(' '))
    for key in keywords: file_return.write('{0:8}\t'.format(key))
    file_return.write('\n')
    for x in range(len(keywords)):
        file_return.write('{0:8}\t'.format(keywords[x]))
        for y in range(len(keywords)): file_return.write('{0:8f}\t'.format(simi_matrix[y][x]))
        file_return.write('\n')
    file_return.close()
