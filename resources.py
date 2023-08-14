from random import choice
from unidecode import unidecode
from requests import get, post
from time import time
words5 = ('abada', 'abade', 'abono', 'abril', 'abrir', 'acaso', 'aceda', 'acesa', 'achar', 'achém', 'acida', 'acima', 'acolá', 'adaga', 'adega', 'adeus', 'adiar', 'advir', 'afins', 'agora', 'aguda', 'agudo', 'ainda', 'alado', 'alemã', 'algas', 'algoz', 'algum', 'alhos', 'aliar', 'aliás', 'almas', 'alpes', 'altar', 'altas', 'alter', 'altos', 'aluna', 'aluno', 'alvos', 'alçar', 'amada', 'amaro', 'ambas', 'ambos', 'amena', 'ameno', 'amido', 'amora', 'amoré', 'ampla', 'amplo', 'anais', 'andar', 'angra', 'angus', 'anjos', 'antas', 'antes', 'antão', 'anual', 'anzol', 'anéis', 'anões', 'aonde', 'aptas', 'aptos', 'aquém', 'arame', 'arcar', 'arcos', 'arder', 'ardor', 'areal', 'areia', 'arena', 'armar', 'aroma', 'arroz', 'artes', 'aspas', 'assar', 'assim', 'assis', 'astro', 'atlas', 'atriz', 'atroz', 'atrás', 'atual', 'atuar', 'aulas', 'autor', 'autos', 'avaré', 'aveia', 'avelã', 'avião', 'axila', 'açude', 'ações', 'aérea', 'aéreo', 'babar', 'babás', 'bacia', 'bacon', 'bahia', 'baias', 'baita', 'balas', 'balde', 'balsa', 'balão', 'bamba', 'bambu', 'banal', 'banda', 'bando', 'banir', 'banjo', 'baque', 'barba', 'barca', 'barco', 'bardo', 'bares', 'barão', 'basco', 'bater', 'batom', 'bazar', 'beata', 'beato', 'beber', 'bebia', 'becos', 'belas', 'belos', 'benta', 'berço', 'besta', 'bicho', 'bicos', 'bingo', 'bioma', 'birra', 'bispo', 'bloco', 'blusa', 'boate', 'boato', 'bobas', 'bobos', 'bocal', 'bocas', 'bocão', 'bodas', 'bodes', 'boina', 'bolha', 'bolos', 'bolsa', 'bolso', 'bolão', 'bomba', 'bonde', 'bonés', 'bossa', 'botar', 'botão', 'brasa', 'brava', 'bravo', 'braço', 'brega', 'brejo', 'breve', 'brisa', 'brito', 'bruta', 'bruto', 'bruxa', 'bruxo', 'bucal', 'bucha', 'bucho', 'bufão', 'bulbo', 'bumba', 'bunda', 'buquê', 'burra', 'burro', 'busto', 'bônus', 'cabal', 'caber', 'cabos', 'cabra', 'cacau', 'cacho', 'cacos', 'cafés', 'caicó', 'caixa', 'calar', 'calda', 'caldo', 'calma', 'calmo', 'calor', 'calos', 'calva', 'calvo', 'camas', 'cambe', 'campo', 'canal', 'canil', 'canja', 'canoa', 'canos', 'capaz', 'capim', 'capuz', 'caqui', 'caras', 'carga', 'cargo', 'carma', 'carne', 'caros', 'carpa', 'carro', 'carta', 'casal', 'casar', 'casca', 'casco', 'casos', 'caspa', 'casta', 'catar', 'cauda', 'caule', 'cavar', 'caçar', 'cação', 'caída', 'ceder', 'cedro', 'cegos', 'celta', 'cenas', 'censo', 'cento', 'cerne', 'certa', 'certo', 'cervo', 'cesta', 'cesto', 'cetim', 'cetro', 'chalé', 'chapa', 'chata', 'chato', 'chave', 'chefe', 'cheia', 'cheio', 'choça', 'chuva', 'chãos', 'ciclo', 'cinco', 'cinta', 'cinto', 'cinza', 'circo', 'cisne', 'cisto', 'cisão', 'citar', 'civil', 'civis', 'ciúme', 'clara', 'claro', 'clave', 'clero', 'clica', 'clico', 'clima', 'clipe', 'clone', 'cloro', 'clube', 'cocos', 'coeso', 'cofre', 'coifa', 'coisa', 'colar', 'combo', 'comer', 'comum', 'conde', 'condo', 'cones', 'congo', 'copas', 'copel', 'copos', 'coral', 'corar', 'corda', 'corja', 'corno', 'corpo', 'corré', 'corsa', 'corvo', 'cosmo', 'costa', 'couro', 'couve', 'covas', 'coxas', 'coçar', 'crase', 'crato', 'credo', 'crepe', 'creta', 'criar', 'crime', 'crise', 'cruas', 'cruel', 'cubas', 'cubos', 'cueca', 'cujos', 'culta', 'culto', 'cupim', 'cupom', 'curar', 'cárie', 'célia', 'cílio', 'cível', 'cólon', 'cópia', 'dados', 'damas', 'danos', 'daqui', 'dardo', 'dedos', 'dedão', 'delas', 'delta', 'densa', 'denso', 'dente', 'depor', 'desde', 'dessa', 'desta', 'deter', 'deusa', 'dever', 'devir', 'diabo', 'dicas', 'dieta', 'diodo', 'dique', 'disso', 'ditar', 'ditos', 'divas', 'dizer', 'doada', 'docas', 'doces', 'dogma', 'doida', 'doido', 'domar', 'donos', 'dores', 'dorso', 'dosar', 'dotar', 'drama', 'dublê', 'ducha', 'duche', 'dueto', 'dunas', 'dupla', 'duplo', 'duque', 'durar', 'duros', 'débil', 'dócil', 'dólar', 'dúzia', 'ecoar', 'eixos', 'elena', 'elfos', 'elite', 'enfim', 'então', 'epóxi', 'errar', 'erros', 'ervas', 'esqui', 'essas', 'esses', 'estar', 'estas', 'estes', 'etapa', 'etnia', 'euros', 'exame', 'exata', 'exato', 'expor', 'extra', 'facas', 'facão', 'fados', 'faixa', 'falar', 'falir', 'falsa', 'falso', 'faraó', 'farda', 'fardo', 'farol', 'farpa', 'farra', 'farsa', 'fases', 'fatal', 'fator', 'fatos', 'fauna', 'favas', 'favor', 'fazer', 'febre', 'fedor', 'feias', 'feios', 'feira', 'feita', 'feixe', 'feliz', 'feras', 'ferir', 'feroz', 'festa', 'fetal', 'fetos', 'feudo', 'fiada', 'fiapo', 'fibra', 'ficar', 'figos', 'filha', 'filho', 'final', 'finas', 'finos', 'fisco', 'fixar', 'fixos', 'flora', 'fluir', 'fluxo', 'flúor', 'fobia', 'focal', 'focar', 'focos', 'fofas', 'fofos', 'fogos', 'fogão', 'foice', 'folha', 'folia', 'fones', 'fonte', 'forno', 'forte', 'fosca', 'fosco', 'fossa', 'fosso', 'fotos', 'fraca', 'fraco', 'frade', 'fraga', 'frase', 'frear', 'frevo', 'frias', 'frios', 'frota', 'fruta', 'fruto', 'fugas', 'fugaz', 'fugir', 'fumar', 'fungo', 'funil', 'furar', 'furor', 'furos', 'fusão', 'fuzuê', 'fuçar', 'fácil', 'féria', 'fêmea', 'fêmur', 'fênix', 'fórum', 'fúria', 'fútil', 'gafes', 'gaita', 'galho', 'galos', 'galão', 'galês', 'gambá', 'ganso', 'garra', 'garça', 'gases', 'gatas', 'gatos', 'geada', 'gelar', 'gemer', 'genes', 'genro', 'gente', 'geral', 'gerar', 'gerir', 'germe', 'gesso', 'gesto', 'gibis', 'ginga', 'girar', 'giros', 'globo', 'goela', 'golfe', 'golfo', 'golpe', 'gorda', 'gordo', 'gorro', 'gosma', 'gotas', 'gozar', 'grade', 'grado', 'grama', 'grana', 'grata', 'grato', 'graus', 'graxa', 'graça', 'greco', 'grega', 'grego', 'greve', 'gripe', 'grupo', 'gruta', 'grãos', 'guará', 'gueto', 'guiar', 'guião', 'guria', 'gusta', 'gávea', 'gêmea', 'gêmeo', 'gênio', 'gíria', 'haras', 'harpa', 'haste', 'haver', 'herói', 'hiato', 'hidro', 'hiena', 'hindu', 'hinos', 'hiper', 'homem', 'honra', 'horas', 'horda', 'horta', 'horto', 'hotel', 'https', 'humor', 'hábil', 'hélio', 'hífen', 'ibero', 'idade', 'ideal', 'ideia', 'idosa', 'idoso', 'igual', 'ilesa', 'ileso', 'impor', 'imune', 'inata', 'incas', 'infra', 'intra', 'intro', 'invés', 'irado', 'irmão', 'irmãs', 'iscas', 'islão', 'itens', 'japão', 'jarra', 'jarro', 'jatos', 'jaula', 'jegue', 'jeito', 'jejum', 'jogar', 'jogos', 'joias', 'jovem', 'judeu', 'jules', 'julho', 'junco', 'junho', 'jurar', 'juros', 'justa', 'justo', 'juíza', 'juízo', 'júlia', 'lados', 'lages', 'lagoa', 'lagos', 'laico', 'lajes', 'lapso', 'lares', 'larva', 'latam', 'latas', 'latim', 'latão', 'laudo', 'lavar', 'lazer', 'laços', 'leais', 'lebre', 'legal', 'leiga', 'leigo', 'leite', 'leito', 'lemes', 'lenda', 'lenha', 'lenta', 'lente', 'lento', 'lenço', 'leque', 'lerdo', 'lesão', 'letal', 'letra', 'levar', 'leões', 'libra', 'liceu', 'licor', 'lidar', 'lidos', 'ligar', 'lilás', 'limbo', 'limão', 'lince', 'linda', 'lindo', 'linha', 'linho', 'lisas', 'lisos', 'litro', 'lixar', 'lixos', 'lixão', 'lição', 'lobos', 'lobão', 'local', 'logar', 'loira', 'loiro', 'lojas', 'lomba', 'lombo', 'lonas', 'longa', 'longe', 'longo', 'lorde', 'lotar', 'louco', 'loura', 'lousa', 'louça', 'loção', 'lugar', 'lulas', 'lunar', 'lutar', 'luvas', 'luxos', 'lábia', 'lábio', 'lápis', 'líder', 'lídia', 'línea', 'lírio', 'lótus', 'lúmen', 'lúpus', 'macho', 'macia', 'macio', 'macro', 'magia', 'magna', 'magos', 'magra', 'magro', 'maior', 'major', 'malas', 'males', 'malta', 'malte', 'mamar', 'mambo', 'mamãe', 'mamão', 'manga', 'manhã', 'mania', 'manos', 'mansa', 'manso', 'manta', 'manto', 'mapas', 'mares', 'marra', 'marte', 'massa', 'matar', 'matos', 'maçãs', 'mecha', 'medir', 'medos', 'meias', 'meiga', 'meigo', 'meios', 'melão', 'memes', 'menor', 'menos', 'menta', 'mercê', 'meros', 'mesas', 'meses', 'mesma', 'mesmo', 'metal', 'meter', 'metro', 'mexer', 'micos', 'micro', 'milha', 'milho', 'mimar', 'minha', 'minis', 'minor', 'miojo', 'miolo', 'mirar', 'mirim', 'missa', 'mista', 'misto', 'mitos', 'miúda', 'miúdo', 'modas', 'modos', 'moeda', 'moela', 'mogno', 'moita', 'molas', 'monge', 'moral', 'morar', 'morna', 'morno', 'morta', 'mosca', 'motas', 'motel', 'motor', 'motos', 'moura', 'mover', 'moços', 'moção', 'moída', 'mudar', 'mudos', 'muita', 'muito', 'mulas', 'mundo', 'mural', 'muros', 'murro', 'musas', 'museu', 'musgo', 'máfia', 'mágoa', 'média', 'médio', 'mídia', 'míope', 'móbil', 'móvel', 'múmia', 'mútua', 'mútuo', 'nadar', 'naipe', 'nariz', 'nasal', 'natal', 'natas', 'naval', 'naves', 'navio', 'nação', 'negar', 'negro', 'neles', 'neném', 'nepal', 'nervo', 'nessa', 'nesse', 'nesta', 'netos', 'nevar', 'nicho', 'ninar', 'ninfa', 'ninho', 'ninja', 'nisso', 'nisto', 'nitro', 'nobel', 'nobre', 'noite', 'nomes', 'norma', 'norte', 'nossa', 'nosso', 'notar', 'novas', 'novos', 'nozes', 'noção', 'nudez', 'nulos', 'nunca', 'nuvem', 'névoa', 'nível', 'obeso', 'obras', 'obter', 'odiar', 'oeste', 'ofurô', 'olhar', 'olhos', 'olhão', 'ombro', 'ondas', 'ontem', 'opaca', 'opaco', 'opala', 'optar', 'opção', 'ordem', 'orgia', 'orixá', 'ossos', 'ostra', 'ousar', 'outra', 'outro', 'ouvir', 'oxalá', 'oásis', 'pacas', 'padre', 'pagam', 'pagar', 'pagos', 'pagão', 'palco', 'palha', 'palma', 'palmo', 'pampa', 'panda', 'panos', 'papel', 'papos', 'parar', 'parco', 'parda', 'pardo', 'parir', 'parma', 'parvo', 'patas', 'pausa', 'pavio', 'pavor', 'pavão', 'pazes', 'pecar', 'pedal', 'pedir', 'pedra', 'pegar', 'pegos', 'peixe', 'pelos', 'penal', 'penca', 'penta', 'pente', 'pequi', 'perda', 'perna', 'persa', 'perto', 'perua', 'pesar', 'pesco', 'pesos', 'peste', 'pesto', 'pezão', 'peões', 'piada', 'piano', 'picar', 'picos', 'pilar', 'pilha', 'pilão', 'pinho', 'pinos', 'pinta', 'pipas', 'pirar', 'pirei', 'pires', 'pirão', 'pisar', 'pisos', 'pista', 'pizza', 'placa', 'placê', 'plebe', 'plena', 'pleno', 'pluma', 'pneus', 'pobre', 'podar', 'poder', 'podre', 'poema', 'poeta', 'polar', 'polir', 'polos', 'polpa', 'polvo', 'pomar', 'pomba', 'pombo', 'pompa', 'ponta', 'ponte', 'ponto', 'porca', 'porco', 'poros', 'porre', 'porém', 'posar', 'posse', 'potes', 'pouca', 'pouco', 'povos', 'povão', 'poças', 'poços', 'poção', 'prado', 'praga', 'praia', 'prata', 'prato', 'praxe', 'prazo', 'praça', 'prece', 'presa', 'preta', 'preto', 'preço', 'prole', 'prosa', 'prumo', 'psico', 'pudim', 'pudor', 'pular', 'pulga', 'pulha', 'pulos', 'punho', 'punir', 'puras', 'puxar', 'puxão', 'pádua', 'páreo', 'pátio', 'pódio', 'pólen', 'pônei', 'quais', 'quase', 'quina', 'quiçá', 'quota', 'rabos', 'radar', 'raiar', 'raios', 'raiva', 'ralar', 'ramos', 'rampa', 'rapaz', 'raras', 'raros', 'rasas', 'rasos', 'rasto', 'ratos', 'razão', 'ração', 'reais', 'recém', 'redes', 'redor', 'refil', 'refém', 'regar', 'reger', 'reler', 'reles', 'reluz', 'relva', 'remar', 'remos', 'renal', 'rente', 'repor', 'retas', 'reter', 'retro', 'rever', 'revés', 'rezar', 'reína', 'reúso', 'ricas', 'ricos', 'rigor', 'rimar', 'risos', 'ritmo', 'ritos', 'rival', 'robôs', 'rocha', 'rodar', 'rojão', 'rolar', 'rolha', 'rolim', 'rolos', 'rombo', 'rosas', 'rosca', 'rosto', 'rotas', 'rotor', 'rouca', 'roupa', 'roxas', 'roçar', 'rubro', 'rudes', 'rugir', 'ruins', 'ruiva', 'ruivo', 'rumor', 'rumos', 'rural', 'russa', 'russo', 'ruína', 'rádio', 'régua', 'rímel', 'saber', 'sabiá', 'sabor', 'sabão', 'sacar', 'sachê', 'sacos', 'sacra', 'sacro', 'sadia', 'sadio', 'safra', 'sagaz', 'salas', 'salmo', 'salsa', 'salão', 'sampa', 'sanar', 'sanha', 'santa', 'santo', 'sapos', 'sarar', 'sarau', 'sarda', 'sarja', 'sarna', 'sarro', 'sauna', 'saída', 'seara', 'secar', 'secos', 'sedas', 'sedes', 'seios', 'seita', 'seiva', 'selar', 'selim', 'selos', 'selva', 'senda', 'senha', 'senso', 'senão', 'serpa', 'serva', 'servo', 'setas', 'setor', 'sexta', 'sexto', 'seção', 'sigla', 'sigma', 'signo', 'silos', 'sinal', 'sismo', 'skate', 'socar', 'socos', 'sogra', 'sogro', 'solar', 'solos', 'somar', 'sonar', 'sopas', 'sorte', 'souto', 'souza', 'suave', 'subir', 'sucos', 'sueca', 'sueco', 'sujar', 'sujos', 'sumir', 'sunga', 'super', 'supor', 'surda', 'surdo', 'surfe', 'sushi', 'sutil', 'sutis', 'sutiã', 'suíno', 'suíte', 'sábio', 'série', 'sério', 'símio', 'síria', 'sírio', 'sítio', 'sócia', 'sócio', 'sódio', 'sósia', 'sótão', 'tabus', 'tacos', 'talco', 'tanga', 'tango', 'tanto', 'tapar', 'tarja', 'tarso', 'taças', 'tchau', 'tecer', 'tecno', 'teias', 'telas', 'teles', 'telha', 'telão', 'temer', 'temor', 'tempo', 'tengo', 'tenor', 'tenra', 'tensa', 'tenso', 'termo', 'terno', 'terra', 'terça', 'terço', 'terém', 'teses', 'tesão', 'tetra', 'texto', 'tiago', 'tiara', 'tigre', 'times', 'tinta', 'tinto', 'tipos', 'tirar', 'tiros', 'titia', 'toada', 'tocar', 'tocha', 'todas', 'todos', 'toldo', 'tolos', 'tomar', 'tonta', 'tonto', 'topar', 'torga', 'torpe', 'torta', 'torto', 'tosar', 'tosca', 'tosco', 'total', 'totem', 'touca', 'touro', 'trair', 'trama', 'trapo', 'treco', 'trena', 'trens', 'trenó', 'treta', 'trevo', 'treze', 'tribo', 'tricô', 'trigo', 'trios', 'tripa', 'tripé', 'trono', 'tropa', 'truco', 'trufa', 'trupe', 'truta', 'tubos', 'tufão', 'tumba', 'turca', 'turco', 'turma', 'turno', 'turnê', 'tutor', 'tábua', 'tátil', 'táxis', 'tédio', 'tênis', 'tênue', 'tíbia', 'tórax', 'túlio', 'túnel', 'ultra', 'unhas', 'unida', 'união', 'untar', 'urano', 'urnas', 'ursos', 'urubu', 'usada', 'usina', 'usual', 'vacas', 'vagar', 'vagos', 'vagão', 'valas', 'valer', 'valor', 'valsa', 'vanda', 'vapor', 'varal', 'vasos', 'vasta', 'vasto', 'vazar', 'vazia', 'vazio', 'vazão', 'veado', 'veias', 'velha', 'velho', 'veloz', 'verba', 'verbo', 'verde', 'verme', 'vespa', 'vetar', 'vetor', 'vetos', 'vezes', 'viado', 'viana', 'vidas', 'vigas', 'vigor', 'vilas', 'vilão', 'vinda', 'vinho', 'vinil', 'vinte', 'viral', 'virar', 'viril', 'visar', 'visor', 'visão', 'vital', 'viver', 'vivos', 'vocal', 'vocês', 'vodca', 'vodka', 'vogal', 'voraz', 'vossa', 'vosso', 'votar', 'votos', 'vovós', 'vozes', 'vulgo', 'vulto', 'vácuo', 'vária', 'vênus', 'vício', 'vídeo', 'vírus', 'vôlei', 'xampu', 'zebra', 'zelar', 'zerar', 'zeros', 'zinco', 'zonas', 'zíper', 'ácido', 'ágape', 'ágeis', 'águia', 'álbum', 'ápice', 'árabe', 'árdua', 'árduo', 'áreas', 'árido', 'áries', 'átila', 'átomo', 'átrio', 'áudio', 'áurea', 'áureo', 'ávida', 'ávido', 'ávila', 'âmago', 'âmbar', 'ânimo', 'ânsia', 'ébano', 'épica', 'épico', 'época', 'ética', 'ético', 'êxito', 'êxodo', 'ícone', 'ídolo', 'ímpar', 'ímpio', 'índex', 'índia', 'índio', 'óbvio', 'óleos', 'ópera', 'órfão', 'órgão', 'óscar', 'óssea', 'ósseo', 'ótica', 'ótico', 'ótima', 'ótimo', 'óvnis', 'óvulo', 'óxido', 'ômega', 'úmida', 'úmido', 'única', 'único', 'úteis', 'útero', 'wokar', 'wokar', 'wokei')
from toxingar import slurs

class wordleClass():
    def __init__(self, wordSize: int, wordList: tuple, postUrl=None, getUrl=None, apiHeaders=None):
        """Return wordleClass instance for given wordsize and wordList"""
        self.wordsize = wordSize
        self.word = "linúx"             # linux
        self.wordList = wordList
        self.wordNoAccent = "linux"

        self.postUrl = postUrl
        self.getUrl = getUrl
        self.apiHeaders = apiHeaders
        self.winnersOutOfDate = True
        self.running = False

        # status of each letter of the guess. 10 = not in the word, 11 = in the word, but wrong position, 12 = in word, correct position
        self.status = [0] * wordSize 
        self.response = ""              # response string
        
        self.allowedGuesses = wordSize + 1
        self.guessesCount = 0       

        self.hallOfFame = {}

        self.close = ("🄰","🄱","🄲","🄳","🄴","🄵","🄶","🄷","🄸","🄹","🄺","🄻","🄼","🄽","🄾","🄿","🅀","🅁","🅂","🅃","🅄","🅅","🅆","🅇","🅈","🅉",)
        self.correct = ("🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹","🇺","🇻","🇼","🇽","🇾","🇿",)


    def update(self, override = False):
        """resets variables and chooses a word randomly from the given wordlist. ctx.send it"""
        # We shouldnt choose new words if there is already a word being wordled
        if self.running and not override:
            return "Quem desistir é woke"
        
        self.guessesCount = 0
        self.word = choice(self.wordList)
        self.wordNoAccent = unidecode(self.word)
        print("word", self.word)
        self.running = True             
        return "!wt _tentativa_, se for capaz!"
        from resources import words5, wordleClass
        wordle5 = wordleClass(5, words5)


    def win(self, username):
        """Sweet victory"""
        if not self.postUrl:
            if username not in self.hallOfFame:
                self.hallOfFame[username] = 0
            self.hallOfFame[username] += 1
            print(self.hallOfFame.items())
        else:
            # username, word, attempts, timestamp)
            p = post(self.postUrl, json = {"username": username, "word": self.wordNoAccent, "attempts": self.guessesCount, "timestamp": time()}, headers=self.apiHeaders)
            print(p.request.body)

        if username not in self.hallOfFame:
            self.hallOfFame[username] = 0
            self.hallOfFame[username] += 1
        self.winnersOutOfDate = True
        self.guessesCount = 0
        self.running = False


    def winners(self):
        if True:
            if self.getUrl:
                # out of date and api mode enabled, so we must get the updated winners list from the api
                g = get(self.getUrl, headers=self.apiHeaders)
                #DBGprint(f"g JSON  {g.json()}\n\tvalues: {g.json().values()}\n\thallofame values: {self.hallOfFame.values()}\n\tcode: {g.status_code}\n\ttext: {g.text}")
                if g.status_code == 200:
                    self.hallOfFame = dict(sorted(g.json().items(), key=lambda x:x[1], reverse=True))
                else: 
                    print("REQUEST ERROR")
            else:
                # api mode disabled, just sort the hallofFame with the recently added winner
                self.hallOfFame = sorted(self.hallOfFame.items(), key=lambda x:x[1], reverse=True)

            self.winnersOutOfDate = False
            
        return self.hallOfFame


    def attempt(self, guess, username):
        """Attempt to get the word right. ctx.send it"""
        if self.running == False:
            return "Inicie um novo wordle com !wordle tamanho-da-palavra"

        if self.guessesCount > self.allowedGuesses:
            return "Woke! Cabou-se.\nReinicie com !wordle tamanho-da-palavra"
        
        if len(guess) != self.wordsize:
            return "O tamanho da tentativa deve ser " + str(self.wordsize)
        
        guess = guess.lower()
        
        self.guessesCount += 1
        self.response = ""                      # restart response string which will be returned
        if guess == "aeiou":
            return "para"
        for i, letter in enumerate(guess):

            # if letter is in the word
            if letter in self.wordNoAccent:
                if letter == self.wordNoAccent[i]:
                    # DBprint(f"\tletter {letter} in word and pos")
                    self.status[i] = 12
                else:
                    # if in word but wrong position
                    
                    # DBprint(f"\tletter {letter} in word")
                    self.status[i] = 11
            else:
                # DBprint(f"\tletter {letter} NOT in word")
                self.status[i] = 10

        if sum(self.status) == 12 * self.wordsize:          # if user won
            self.response += f"\nLinux! *{username} ganha inesperadamente*"
            self.win(username)
            return self.response

        for i, statuscode in enumerate(self.status):
            if statuscode == 12:
                # append filled letter emoji. ord() returns the ascii. 97 = 'a'.
                self.response += self.correct[ord(guess[i]) - 97]
            elif statuscode == 11:
                self.response += self.close[ord(guess[i]) - 97]
            else:
                self.response += "▯"

        if sum(self.status) == 10 * self.wordsize:        # if missed every word
            self.response += "\nburro"

        if self.guessesCount == self.allowedGuesses:        # if missed the last chance
            self.response += "\nAndrebot wins\n" + self.word
            username = "Andrebot"
            self.win(username)

        print(self.response)
        return self.response
    
response = get(testUrl, headers=apiHeaders)

