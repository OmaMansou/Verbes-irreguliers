import random

Tab = [['abide', ('abode', 'abided'), ('abode', 'abided'), 'demeurer'], ['arise', 'arose', 'arisen', 'surgir / survenir / provenir de'], ['awake', 'awoke','awoken', 'réveiller'], ['be', ('was', 'were'), 'been', 'être'], ['bear', 'bore', 'borne', 'porter / supporter / soutenir'], ['beat', 'beat', 'beaten', 'battre'], ['become', 'became', 'become', 'devenir'], ['beget', 'begat', 'begotten', 'engendrer'], ['begin', 'began', 'begun', 'commencer'], ['bend', 'bent', 'bent', 'plier / tordre / courber'], ['bereave', ('bereft', 'bereaved'), ('bereft', 'bereaved'), 'déposséder / priver'], ['beseech', ('besought', 'beseeched'), ('besought', 'beseeched'), 'supplier'], ['beset', 'beset', 'beset', 'entourer de / assaillir'], ['bet', 'bet', 'bet', 'parier'], ['bid', 'bid', 'bid', 'faire une enchère de'], ['bind', 'bound', 'bound', 'attacher / lier'], ['bite', 'bit', 'bitten', 'mordre'], ['bleed', 'bled', 'bled', 'saigner'], ['blow', 'blew', 'blown', 'souffler'], ['breed', 'bred', 'bred', 'élever (animaux ou plantes)'], ['break', 'broke', 'broken', 'casser'], ['bring', 'brought', 'brought', 'amener / apporter'], ['broadcast', 'broadcast', 'broadcast', 'diffuser / téléviser'], ['build', 'built', 'built', 'construire / bâtir'], ['burn', ('burned', 'burnt'), ('burned', 'burnt'), 'brûler / se brûler'], ['burst', 'burst', 'burst', 'éclater'], ['buy', 'bought', 'bought', 'acheter'], ['cast', 'cast', 'cast', 'jeter / donner un rôle à'], ['catch', 'caught', 'caught', 'attraper'], ['chide', 'chid', 'chidden', 'gronder / réprimander'], ['choose', 'chose', 'chosen', 'choisir'], ['cleave', ('cleft','clove'), ('cleft','clove'), 'fendre / coller'], ['cling', 'clung', 'clung', "s'accrocher à"], ['clothe', ('clothed', 'clad'), ('clothed', 'clad'), 'habiller'], ['come', 'came', 'come', 'venir'], ['cost', 'cost', 'cost', 'coûter'], ['creep', 'crept', 'crept', 'avancer au pas / se glisser'], ['crow', ('crew', 'crowed'), 'crowed', 'chanter (un coq) / jubiler'], ['cut', 'cut', 'cut', 'couper'], ['deal', 'dealt', 'dealt', "faire le commerce / s'occuper de"], ['dig', 'dug', 'dug', 'creuser'], ['dive', 'dove', 'dived', 'plonger'], ['do', 'did', 'done', 'faire'], ['draw', 'drew', 'drawn', 'tirer / dessiner / attirer'], ['dream', ('dreamed', 'dreamt'), ('dreamed', 'dreamt'), 'rêver'], ['drink', 'drank', 'drunk', 'boire'], ['drive', 'drove', 'driven', 'conduire'], ['dwell', ('dwelt', 'dwelled'), ('dwelt', 'dwelled'), 'habiter / rester'], ['eat', 'ate', 'eaten', 'manger'], ['fall', 'fell', 'fallen', 'tomber'], ['feed', 'fed', 'fed', 'nourrir'], ['feel', 'felt', 'felt', 'sentir / ressentir'], ['fight', 'fought', 'fought', 'se battre contre / avec'], ['find', 'found', 'found', 'trouver'], ['fit', 'fit', 'fit', 'correspondre à'], ['flee', 'fled', 'fled', 'fuir'], ['fling', 'flung', 'flung', 'lancer'], ['fly', 'flew', 'flown', 'transporter par avion'], ['forbid', 'forbade', 'forbidden', 'interdire / défendre'], ['forecast', 'forecast', 'forecast', 'prévoir'], ['forget', 'forgot', 'forgotten', 'oublier'], ['forgive', 'forgave', 'forgiven', 'pardonner'], ['forsake', 'forsook', 'forsaken', 'abandonner'], ['foresee', 'foresaw', 'foreseen', 'prévoir'], ['freeze', 'froze', 'frozen', 'geler / congeler'], ['get', 'got', ('gotten', 'got'), 'obtenir / recevoir / prendre'], ['gird', ('girt', 'girded'), ('girt', 'girded'), 'ceindre'], ['give', 'gave', 'given', 'donner'], ['go', 'went', 'gone', 'aller'], ['grind', 'ground', 'ground', 'moudre'], ['grow', 'grew', 'grown', 'pousser / se développer'], ['hang', 'hung', 'hung', 'suspendre / pendre / être accroché(e)'], ['have', 'had', 'had', 'avoir'], ['hear', 'heard', 'heard', 'entendre'], ['heave', ('hove', 'heaved'), ('hove', 'heaved'), 'lever'], ['hew', 'hewed', ('hewn', 'hewed'), 'couper / tailler'], ['hide', 'hid', 'hidden', 'cacher / se cacher'], ['hit', 'hit', 'hit', 'frapper / heurter'], ['hold', 'held', 'held', 'tenir / maintenir'], ['hurt', 'hurt', 'hurt', 'blesser / faire mal'], ['keep', 'kept', 'kept', 'garder'], ['kneel', ('kneeled', 'knelt'), ('kneeled', 'knelt'), 'se mettre à genoux'], ['knit', ('knit', 'knitted'), ('knit', 'knitted'), 'tricoter'], ['know', 'knew', 'known', 'savoir'], ['lay', 'laid', 'laid', 'poser / mettre / pondre'], ['lead', 'led', 'led', 'mener / guider'], ['lean', ('leant', 'leaned'), ('leant', 'leaned'), 'pencher'], ['leap', ('leaped', 'leapt'), ('leaped', 'leapt'), 'bondir / sauter'], ['learn', ('learned', 'learnt'), ('learned', 'learnt'), 'apprendre'], ['leave', 'left', 'left', 'quitter'], ['lend', 'lent', 'lent', 'prêter'], ['let', 'let', 'let', "laisser quelqu'un faire quelque chose"], ['lie', 'lay', 'lain', "s'allonger / se coucher"], ['light', ('lit', 'lighted'), ('lit', 'lighted'), 'allumer'], ['lose', 'lost', 'lost', 'perdre'], ['make', 'made', 'made', 'faire'], ['mean', 'meant', 'meant', 'signifier'], ['meet', 'met', 'met', 'rencontrer'], ['mislead', 'misled', 'misled', 'induire en erreur'], ['mistake', 'mistook', 'mistaken', 'mal comprendre'], ['outdo', 'outdid', 'outdone', 'surpasser'], ['outrun', 'outran', 'outrun', 'distancer'], ['overcome', 'overcame', 'overcome', 'surmonter'], ['overdo', 'overdid', 'overdone', 'exagérer / trop cuire'], ['overdraw', 'overdrew', 'overdrawn', 'mettre son compte à découvert'], ['overrun', 'overran', 'overrun', 'dépaser (le temps alloué)'], ['oversee', 'oversaw', 'overseen', 'surveiller / superviser'], ['overtake', 'overtook', 'overtaken', 'doubler / dépasser'], ['overthrow', 'overthrew', 'overthrown', 'renverser (gouvernement)'], ['pay', 'paid', 'paid', 'payer'], ['plead', 'pled', 'pled', 'plaider / supplier'], ['prove', 'proved', ('proved', 'proven'), 'prouver'], ['put', 'put', 'put', 'mettre / poser / placer'], ['quit', 'quit', 'quit', 'abandonner / démissionner'], ['read', 'read', 'read', 'lire'], ['relay', 'relaid', 'relaid', 'transmettre / communiquer'], ['rend', 'rent', 'rent', 'déchirer'], ['rewind', 'rewound', 'rewound', 'rembobiner'], ['rid', 'rid', 'rid', 'débarasser'], ['ride', 'rode', 'ridden', 'monter à cheval / en vélo'], ['ring', 'rang', 'rung', 'sonner / téléphoner à / appeler'], ['rise', 'rose', 'risen', 'monter / se lever'], ['run', 'ran', 'run', 'courir'], ['say', 'said', 'said', 'dire'], ['saw', 'sawed', 'sawn', 'scier'], ['see', 'saw', 'seen', 'voir'], ['seek', 'sought', 'sought', 'chercher / rechercher'], ['sell', 'sold', 'sold', 'vendre'], ['send', 'sent', 'sent', 'envoyer'], ['set', 'set', 'set', 'placer / régler / fixer'], ['sew', 'sewed', ('sewn', 'sewed'), 'coudre'], ['shake', 'shook', 'shaken', 'secouer / se serrer la main'], ['shear', 'sheared', 'shorn', 'tondre'], ['shed', 'shed', 'shed', 'verser (larmes/sang) / perdre (feuilles)'], ['shine', 'shone', 'shone', '(faire) briller'], ['shoe', 'shod', 'shod', 'chausser'], ['shoot', 'shot', 'shot', "tuer ou blesser d'un coup de feu"], ['show', 'showed', ('shown', 'showed'), 'montrer'], ['shrink', 'shrank', 'shrunk', 'rétrécir'], ['shrive', ('shrove', 'shrived'), ('shriven', 'shrived'), 'absoudre'], ['shut', 'shut', 'shut', 'fermer'], ['sing', 'sang', 'sung', 'chanter'], ['sink', 'sank', 'sunk', 'couler'], ['sit', 'sat', 'sat', "s'asseoir"], ['slay', 'slew', 'slain', 'tuer'], ['sleep', 'slept', 'slept', 'dormir'], ['slide', 'slid', 'slid', 'faire glisser / glisser'], ['sling', 'slung', 'slung', 'lancer'], ['slink', 'slunk', 'slunk', 'aller furtivement'], ['slit', ('slit', 'slitted'), ('slit', 'slitted'), '(se) fendre'], ['smell', ('smelled', 'smelt'), ('smelled', 'smelt'), 'sentir'], ['smite', 'smote', 'smitten', 'frapper / vaincre'], ['sneak', ('snuck', 'sneaked'), ('snuck', 'sneaked'), 'se glisser (sans faire du bruit)'], ['sow', 'sowed', 'sown', 'semer'], ['speak', 'spoke', 'spoken', 'parier'], ['speed', ('sped', 'speeded'), ('sped', 'speeded'), 'faire un excès de vitesse'], ['spell', ('spelled', 'spelt'), ('spelled', 'spelt'), 'épeler'], ['spend', 'spent', 'spent', "dépenser de l'argent (pour)"], ['spill', ('spilled', 'spilt'), ('spilled', 'spilt'), 'renverser'], ['spin', 'spun', 'spun', 'faire tourner'], ['spit', ('spit', 'spat'), ('spit', 'spat'), 'cracher'], ['split', 'split', 'split', 'fendre / déchirer / diviser'],['spoil', 'spoilt', 'spoilt', "gâcher / gâter"], ['spoonfeed', 'spoonfed', 'spoonfed', 'nourrir à la cuillère'], ['spread', 'spread', 'spread', 'étaler / écarter / propager'], ['spring', 'sprang', 'sprung', 'sauter / bondir'], ['stand', 'stood', 'stood', 'mettre (debout) / supporter'], ['stave', ('stove', 'staved'), ('stove', 'staved'), 'défoncer / crever'], ['steal', 'stole', 'stolen', 'voler / dérober'], ['stick', 'stuck', 'stuck', 'coller / se coincer'], ['sting', 'stung', 'stung', 'piquer'], ['stink', ('stank', 'stunk'), 'stunk', 'puer / empester'], ['strew', 'strew', 'strewn', 'semer / joncher'], ['stride', 'strode', 'stridden', 'marcher à grands pas'], ['string', 'strung', 'strung', 'ficeler'], ['strike', 'struck', 'struck', 'frapper / heurter / frotter'], ['strive', 'strove', 'striven', "s'efforcer de faire qqch"], ['swear', 'swore', 'sworn', 'jurer'], ['sweat', ('sweat', 'sweated'), ('sweat', 'sweated'), 'transpirer / suer'], ['swell', 'swelled', 'swollen', 'se gonfler'], ['sweep', 'swept', 'swept', 'balayer'], ['swim', 'swam', 'swum', 'nager'], ['swing', 'swung', 'swung', 'balancer / se balancer'], ['take', 'took', 'taken', 'prendre'], ['teach', 'taught', 'taught', 'apprendre qqch à qqun'], ['tear', 'tore', 'torn', 'déchirer'], ['tell', 'told', 'told', 'raconter'], ['think', 'thought', 'thought', 'penser'], ['throw', 'threw', 'thrown', 'jeter / lancer'], ['thrust', 'thrust', 'thrust', 'enfoncer / fourrer'], ['tread', 'trod', 'trodden', 'piétiner / fouler / marcher'], ['undergo', 'underwent', 'undergone', 'subir (douleur, difficultés) / éprouver'], ['understand', 'understood', 'understood', 'comprendre'], ['undertake', 'undertook', 'undertaken', "entreprendre / s'engager à"], ['uphold', 'upheld', 'upheld', 'maintenir (loi) / soutenir (décision)'], ['upset', 'upset', 'upset', 'déranger / renverser'], ['wake', 'woke', 'woken', 'réveiller / se réveiller'], ['wear', 'wore', 'worn', 'porter / user'], ['weave', 'wove', 'woven', 'tisser'], ['wed', ('wed', 'wedded'), ('wed', 'wedded'), 'épouser / marier'], ['weep', 'wept', 'wept', 'pleurer'], ['wet', 'wet', 'wet', 'mouiller'], ['win', 'won', 'won', 'gagner'], ['wind', 'wound', 'wound', 'enrouler (fil) / remonter (horloge)'], ['withhold', 'withheld', 'withheld', 'cacher (information)'], ['withstand', 'withstood', 'withstood', 'résister à'], ['wring', 'wrung', 'wrung', 'essorer (linge)'], ['write', 'wrote', 'written', 'écrire']]

Tfacile = [['be', ('was', 'were'), 'been', 'être'], ['bear', 'bore', 'borne', 'porter / supporter / soutenir'], ['become', 'became', 'become', 'devenir'], ['begin', 'began', 'begun', 'commencer'], ['bet', 'bet', 'bet', 'parier'], ['bite', 'bit', 'bitten', 'mordre'], ['blow', 'blew', 'blown', 'souffler'], ['break', 'broke', 'broken', 'casser'], ['bring', 'brought', 'brought', 'amener / apporter'], ['bring', 'brought', 'brought', 'amener / apporter'], ['build', 'built', 'built', 'construire / bâtir'], ['burn', ('burned', 'burnt'), ('burned', 'burnt'), 'brûler / se brûler'], ['buy', 'bought', 'bought', 'acheter'], ['catch', 'caught', 'caught', 'attraper'], ['choose', 'chose', 'chosen', 'choisir'], ['come', 'came', 'come', 'venir'], ['cost', 'cost', 'cost', 'coûter'], ['cut', 'cut', 'cut', 'couper'], ['do', 'did', 'done', 'faire'], ['draw', 'drew', 'drawn', 'tirer / dessiner / attirer'], ['dream', ('dreamed', 'dreamt'), ('dreamed', 'dreamt'), 'rêver'], ['drink', 'drank', 'drunk', 'boire'], ['drive', 'drove', 'driven', 'conduire'], ['eat', 'ate', 'eaten', 'manger'], ['fall', 'fell', 'fallen', 'tomber'], ['feel', 'felt', 'felt', 'sentir / ressentir'], ['fight', 'fought', 'fought', 'se battre contre / avec'], ['find', 'found', 'found', 'trouver'], ['fly', 'flew', 'flown', 'transporter par avion'], ['forget', 'forgot', 'forgotten', 'oublier'], ['forgive', 'forgave', 'forgiven', 'pardonner'], ['get', 'got', ('gotten', 'got'), 'obtenir / recevoir / prendre'], ['give', 'gave', 'given', 'donner'], ['go', 'went', 'gone', 'aller'], ['have', 'had', 'had', 'avoir'], ['hear', 'heard', 'heard', 'entendre'], ['keep', 'kept', 'kept', 'garder'], ['leave', 'left', 'left', 'quitter'], ['know', 'knew', 'known', 'savoir'], ['lose', 'lost', 'lost', 'perdre'], ['make', 'made', 'made', 'faire'], ['meet', 'met', 'met', 'rencontrer'], ['read', 'read', 'read', 'lire'], ['ring', 'rang', 'rung', 'sonner / téléphoner à / appeler'], ['say', 'said', 'said', 'dire'], ['see', 'saw', 'seen', 'voir'], ['sit', 'sat', 'sat', "s'asseoir"], ['sleep', 'slept', 'slept', 'dormir'], ['swim', 'swam', 'swum', 'nager'], ['take', 'took', 'taken', 'prendre'], ['think', 'thought', 'thought', 'penser'], ['write', 'wrote', 'written', 'écrire']]

Tmoyen = Tfacile + [['abide', ('abode', 'abided'), ('abode', 'abided'), 'demeurer'], ['arise', 'arose', 'arisen', 'surgir / survenir / provenir de'], ['awake', 'awoke','awoken', 'réveiller'], ['breed', 'bred', 'bred', 'élever (animaux ou plantes)'], ['beat', 'beat', 'beaten', 'battre'], ['bend', 'bent', 'bent', 'plier / tordre / courber'], ['bid', 'bid', 'bid', 'faire une enchère de'], ['bind', 'bound', 'bound', 'attacher / lier'], ['bleed', 'bled', 'bled', 'saigner'], ['burst', 'burst', 'burst', 'éclater'], ['cast', 'cast', 'cast', 'jeter / donner un rôle à'],  ['cling', 'clung', 'clung', "s'accrocher à"], ['creep', 'crept', 'crept', 'avancer au pas / se glisser'], ['deal', 'dealt', 'dealt', "faire le commerce / s'occuper de"], ['dig', 'dug', 'dug', 'creuser'], ['dwell', ('dwelt', 'dwelled'), ('dwelt', 'dwelled'), 'habiter / rester'], ['feed', 'fed', 'fed', 'nourrir'], ['flee', 'fled', 'fled', 'fuir'], ['fling', 'flung', 'flung', 'lancer'], ['forbid', 'forbade', 'forbidden', 'interdire / défendre'], ['freeze', 'froze', 'frozen', 'geler / congeler'], ['grind', 'ground', 'ground', 'moudre'], ['grow', 'grew', 'grown', 'pousser / se développer'], ['hang', 'hung', 'hung', 'suspendre / pendre / être accroché(e)'], ['hide', 'hid', 'hidden', 'cacher / se cacher'], ['hit', 'hit', 'hit', 'frapper / heurter'], ['hold', 'held', 'held', 'tenir / maintenir'], ['hurt', 'hurt', 'hurt', 'blesser / faire mal'], ['kneel', ('kneeled', 'knelt'), ('kneeled', 'knelt'), 'se mettre à genoux'], ['lay', 'laid', 'laid', 'poser / mettre / pondre'], ['lead', 'led', 'led', 'mener / guider'], ['lean', ('leant', 'leaned'), ('leant', 'leaned'), 'pencher'], ['leap', ('leaped', 'leapt'), ('leaped', 'leapt'), 'bondir / sauter'], ['learn', ('learned', 'learnt'), ('learned', 'learnt'), 'apprendre'], ['lend', 'lent', 'lent', 'prêter'], ['let', 'let', 'let', "laisser quelqu'un faire quelque chose"], ['lie', 'lay', 'lain', "s'allonger / se coucher"], ['light', ('lit', 'lighted'), ('lit', 'lighted'), 'allumer'], ['mean', 'meant', 'meant', 'signifier'], ['pay', 'paid', 'paid', 'payer'], ['put', 'put', 'put', 'mettre / poser / placer'], ['quit', 'quit', 'quit', 'abandonner / démissionner'], ['rid', 'rid', 'rid', 'débarasser'], ['ride', 'rode', 'ridden', 'monter à cheval / en vélo'], ['rise', 'rose', 'risen', 'monter / se lever'], ['run', 'ran', 'run', 'courir'], ['saw', 'sawed', 'sawn', 'scier'], ['seek', 'sought', 'sought', 'chercher / rechercher'], ['sell', 'sold', 'sold', 'vendre'], ['send', 'sent', 'sent', 'envoyer'], ['set', 'set', 'set', 'placer / régler / fixer'], ['sew', 'sewed', ('sewn', 'sewed'), 'coudre'], ['shake', 'shook', 'shaken', 'secouer / se serrer la main'], ['shear', 'sheared', 'shorn', 'tondre'], ['shed', 'shed', 'shed', 'verser (larmes/sang) / perdre (feuilles)'], ['shine', 'shone', 'shone', '(faire) briller'], ['shoe', 'shod', 'shod', 'chausser'], ['shoot', 'shot', 'shot', "tuer ou blesser d'un coup de feu"], ['show', 'showed', ('shown', 'showed'), 'montrer'], ['shrink', 'shrank', 'shrunk', 'rétrécir'], ['shut', 'shut', 'shut', 'fermer'], ['sing', 'sang', 'sung', 'chanter'], ['slide', 'slid', 'slid', 'faire glisser / glisser'], ['sling', 'slung', 'slung', 'lancer'], ['slink', 'slunk', 'slunk', 'aller furtivement'], ['slit', ('slit', 'slitted'), ('slit', 'slitted'), '(se) fendre'], ['smell', ('smelled', 'smelt'), ('smelled', 'smelt'), 'sentir'], ['sow', 'sowed', 'sown', 'semer'], ['speak', 'spoke', 'spoken', 'parier'], ['speak', 'spoke', 'spoken', 'parier'], ['speed', ('sped', 'speeded'), ('sped', 'speeded'), 'faire un excès de vitesse'], ['spell', ('spelled', 'spelt'), ('spelled', 'spelt'), 'épeler'], ['spend', 'spent', 'spent', "dépenser de l'argent (pour)"], ['spill', ('spilled', 'spilt'), ('spilled', 'spilt'), 'renverser'], ['spit', ('spit', 'spat'), ('spit', 'spat'), 'cracher'], ['split', 'split', 'split', 'fendre / déchirer / diviser'], ['spread', 'spread', 'spread', 'étaler / écarter / propager'], ['spring', 'sprang', 'sprung', 'sauter / bondir'], ['stand', 'stood', 'stood', 'mettre (debout) / supporter'], ['steal', 'stole', 'stolen', 'voler / dérober'], ['stick', 'stuck', 'stuck', 'coller / se coincer'], ['sting', 'stung', 'stung', 'piquer'], ['stink', ('stank', 'stunk'), 'stunk', 'puer / empester'], ['stride', 'strode', 'stridden', 'marcher à grands pas'], ['string', 'strung', 'strung', 'ficeler'], ['strike', 'struck', 'struck', 'frapper / heurter / frotter'], ['strive', 'strove', 'striven', "s'efforcer de faire qqch"], ['swear', 'swore', 'sworn', 'jurer'], ['sweep', 'swept', 'swept', 'balayer'], ['swell', 'swelled', 'swollen', 'se gonfler'], ['swing', 'swung', 'swung', 'balancer / se balancer'], ['teach', 'taught', 'taught', 'apprendre qqch à qqun'], ['tear', 'tore', 'torn', 'déchirer'], ['tell', 'told', 'told', 'raconter'], ['throw', 'threw', 'thrown', 'jeter / lancer'], ['thrust', 'thrust', 'thrust', 'enfoncer / fourrer'], ['tread', 'trod', 'trodden', 'piétiner / fouler / marcher'], ['understand', 'understood', 'understood', 'comprendre'], ['wake', 'woke', 'woken', 'réveiller / se réveiller'], ['wear', 'wore', 'worn', 'porter / user'], ['weave', 'wove', 'woven', 'tisser'], ['weep', 'wept', 'wept', 'pleurer'], ['win', 'won', 'won', 'gagner'], ['wind', 'wound', 'wound', 'enrouler (fil) / remonter (horloge)'], ['wring', 'wrung', 'wrung', 'essorer (linge)'], ['write', 'wrote', 'written', 'écrire'], ['spoil', 'spoilt', 'spoilt', "gâcher / gâter"]]

def tupler(T): 
    for i in range(len(T)):
        for j in range(1, 3):
            if type(T[i][j]) == str:
                T[i][j] = (T[i][j],)
    return T

TabTuple = tupler(Tab) # On transforme Tab en un tableau à éléments faciles à manipuler

Verbs2 = [TabTuple[i][0] for i in range(208)]
#SP = [T[i][1] for i in range(206)]
#PP = [T[i][2] for i in range(206)]
#Fr = [T[i][3] for i in range(206)]


def quizz(Tab):
    Verbs = [Tab[i][0] for i in range(len(Tab))]
    nombre = [i for i in range(len(Tab))] # Ensemble des indices
    T = tupler(Tab)
    answer = [] # On initialise une liste contenant les réponses
    indices = 0
    reussis = 0
    while len(nombre) > 0:
        i = random.choice(nombre) # Choisit un indice au hasard 
        nombre.pop(nombre.index(i)) # Enlève l'indice de nombre afin ne de pas le repiocher
        print("The verb : " + T[i][0]) 
        sp = input("The simple past : ").lower() # L'utilisateur répond au Simple Past
        pp = input("The past participle : ").lower() # L'utilisateur répond au Past Participle
        verb = (i , sp in T[i][1], pp in T[i][2]) # Tuple (indice, bool sp, bool pp)
        reussis += 1*(sp in T[i][1]) + 1*(pp in T[i][2]) # Nombre de questions réussies
        answer += [verb] # Tableau des tuples susmentionnés
        command = input("Voulez-vous continuer (Appuyez sur Entrer si oui/ n sinon) : ")
        indices += 2 # On ajoute 2 au nombre de questions posées (pp et sp)
        if command == 'n':
            break

    print("****************************************")
    print("Votre score est : " + str((reussis/indices)*20)[:5]+ '/20')
    print("\n")
    
    if indices != reussis:
        print("Correction :") # Donne la correction des questions auxquelles on a mal répondu
        for tpl in answer:
            if not (tpl[1] and tpl[2]):
                if not tpl[1]:
                    print("The simple past of " + T[tpl[0]][0] + " is : ")
                    for e in T[tpl[0]][1]:
                        print(e)
                if not tpl[2]:
                    print("The past participle of " + T[tpl[0]][0] + " is : ")
                    for e in T[tpl[0]][2]:
                        print(e)
                print("****************************************")
                print("\n")
            

def infos(verb):
    """Donne les informations sur les verbes (Infinitive, Simple past, Past participle)"""
    if verb in Verbs2:
        print("The verb : " + str(Tab[Verbs2.index(verb)][0]))
        if len(Tab[Verbs2.index(verb)][1]) == 1:
            print("The simple past : " + Tab[Verbs2.index(verb)][1][0])
        elif len(Tab[Verbs2.index(verb)][1]) == 2:
            print("The simple past : " + Tab[Verbs2.index(verb)][1][0] + " or " + Tab[Verbs2.index(verb)][1][1])
        if len(Tab[Verbs2.index(verb)][2]) == 1:
            print("The past participle : " + Tab[Verbs2.index(verb)][2][0])
        elif len(Tab[Verbs2.index(verb)][2]) == 2:
            print("The past participle : " + Tab[Verbs2.index(verb)][2][0] + " or " +Tab[Verbs2.index(verb)][2][1])
        #print("The French translation : " + Tab[Verbs2.index(verb)][3])
    else:
        print("Le verbe que vous avez saisi n'est pas disponible. Si c'est un verbe irrégulier, contactez-nous s'il vous plait")

def traduction(verb): # Donne la traduction du verbe en français
    if verb in Verbs2:
        print("La traduction en français est : " + Tab[Verbs2.index(verb)][3])
    else:
        print("Le verbe que vous avez saisi n'est pas disponible. Si c'est un verbe irrégulier, contactez-nous s'il vous plait.")


# Menu 
print("Bienvenue ! Allons découvrir les verbes irréguliers anglais !")
print("\n")
while True:
    print("Choisissez une option :") # Affiche les options du programme
    print("1) Quizz")
    print("2) Informations sur les verbes")
    print("3) Traduction Anglais -> Français")
    print("4) Des suggestions ? Des verbes manquants ? Contactez-nous.")
    print("5) Quitter")
    print("\n")
    try:
        indice = int(input("Option : "))
    except ValueError: # Au cas où l'utilisateur introduit une valeur incompatible
        print("Option incorrecte")
    if indice == 1: # Quizz
        print("Choisissez un niveau de difficulté")
        print("1) Facile")
        print("2) Moyen")
        print("3) Expert")
        try:
            diff = int(input("Difficulté : "))
        except ValueError: # Au cas où l'utilisateur introduit une valeur incompatible
            print("Option incorrecte")
        print("\n")
        if diff == 1:
            quizz(Tfacile)
        elif diff == 2:
            quizz(Tmoyen)
        elif diff == 3:
            quizz(Tab)
        else:
            print("Option incorrecte")
        q = input("Entrez q pour quitter, appuyez sur n'importe quel autre caractère pour continuer : ")
        if q == "q":
            break
    elif indice == 2: # Informations
        verbe = input("Quel verbe ? \n").lower()
        infos(verbe)
        print("\n")
        q = input("Entrez q pour quitter, appuyez sur n'importe quel autre caractère pour continuer : ")
        if q == "q":
            break
    elif indice == 3: # Traduction Anglais -> Français
        verbe = input("Quel verbe ? \n").lower()
        traduction(verbe)
        print("\n")
        q = input("Entrez q pour quitter, appuyez sur n'importe quel autre caractère pour continuer : ")
        if q == "q":
            break
    elif indice == 4: # Suggestions
        print("Contactez le développeur de cette application.")
        print("Adresse e-mail : irregular.verbs.contact@gmail.com")
        print("\n")
        q = input("Entrez q pour quitter, appuyez sur n'importe quel autre caractère pour continuer : ")
        if q == "q":
            break
    elif indice == 5: # Arrêt du programme
        break
    else:
        print("Option incorrecte")
    print("****************************************")
    print("\n")
    
""" Special thanks to Outhmane Itro and Abdelhamid Mouflih for their help.
© Omar Mansour -- 2018 """


"""Historique des mises à jour:

1.0 : Version originale.

1.0.1 : Donne la note du quizz avec 2 chiffres après la virgule au lieu des 15 d'un flottant normal.

1.0.2 : Corrige un bug dans la traduction anglais -> français.

1.1 : L'utilisateur n'est plus requis d'écrire ses réponses en minuscule uniquement. Corrige un bug dans la fonction traduction. Ajoute l'adresse e-mail de contact au menu 4).

1.2 : Ajout du verbe write. Ajout du verbe spoil. Introduction de la fonctionnalité du choix de difficulté lors du quizz.

1.2.1 : Correction mineur dans la fonction infos qui retourne à présent toutes les formes du simple past ou du past participle.
"""