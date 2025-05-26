#Há um campeonato de tiro. Cada participante realiza 3 rodadas de tiros.
#Em cada rodada um competidor pode fazer de 0 a 1000 pontos. 
#A média dos pontos das duas melhores rodadas de um competidor é incluída em um ranque. 
#A função deve determinar os pontos no ranque de um competidor dados os pontos das três rodadas.

def pontos_no_ranque(pts_rodada1: int, pts_rodada2: int, pts_rodada3: int) -> float:
    '''Determina os pontos e um competidor no ranque a partir de *pts_rodada1*, *pts_rodada2* e *pts_rodada1*.
    Todas as entradas devem ser valores x, 0 <= x <= 1000.
    Exemplos:
    >>> pontos_no_ranque(1000, 500, 100)
    750.0
    >>> pontos_no_ranque(1000,0,2)
    501.0
    >>> pontos_no_ranque(0,1000,3)
    501.5
    >>> pontos_no_ranque(123, 250,250)
    250.0
    >>> pontos_no_ranque(100,100,100)
    100.0
    '''

    assert 0 <= pts_rodada1 <= 1000, 'A quantidade de pontos por rodada limita-se ao intervalo fechado de 0 a 1000.'
    assert 0 <= pts_rodada2 <= 1000, 'A quantidade de pontos por rodada limita-se ao intervalo fechado de 0 a 1000.'
    assert 0 <= pts_rodada1 <= 1000, 'A quantidade de pontos por rodada limita-se ao intervalo fechado de 0 a 1000.'

    if pts_rodada1 >= pts_rodada2 or pts_rodada1 >= pts_rodada3:
        if pts_rodada2 >= pts_rodada3:
            pontos = (pts_rodada1 + pts_rodada2)/2

        else:
            pontos = (pts_rodada1 + pts_rodada3)/2

    else:
        pontos = (pts_rodada2 + pts_rodada3)/2

    return pontos


#A gravidade e os pontos de uma infração de excesso de velocidade são determinados
#de acordo com a porcentagem do limite de velocidade excedido.
#Se o limite de velocidade for excedido em até 20%, a infração é média (3 pontos), entre 20% e
#50% a infração é grave (5 pontos), e acima de 50% a infração é gravíssima (7 pontos).
#A velocidade medida por um radar passa por um ajuste.
#Se a velocidade medida for até 105 Km/h, a velocidade considerada é a velocidade medida menos 5 km/h.
#Se a velocidade medida for maior que 105 Km/h, a velocidade considerada será 5% a menos que a velocidade medida.
      
def velocidade_considerada(velocidade_medida: int) -> int:
    '''Determina a velocidade que deve ser considerada por um radar a partir da *velocidade_medida*.
    Caso *velocidade_medida* seja exatamente 105km/h, retornar-se-á 105 - 5 = 100.
    Caso *velocidade_medida* seja menor do que 5km/h, retornar-se-á 0.
    Casas decimais serão arredondadas.
    Exemplos:
    >>> velocidade_considerada(105)
    100
    >>> velocidade_considerada(100)
    95
    >>> velocidade_considerada(4)
    0
    >>> velocidade_considerada(200)
    190
    >>> velocidade_considerada(193)
    183
    '''
    
    if velocidade_medida > 105:
        vel_considerada = velocidade_medida*0.95

    elif velocidade_medida  < 5:
        vel_considerada = 0 

    else:
        vel_considerada = velocidade_medida - 5

    return round(vel_considerada)


def pontos_na_carteira(velocidade_medida: int, limite_velocidade: int) -> int:
    '''Determina quantos ponto serão atribídos a carteira de um motorista a partir da *velocidade_medida*
    e do *limite_de_velocidade*.
    *velocidade_medida* será tratada pela função velocidade_considerada e após isso será referenciada como velocidade.
    Caso *velocidade* seja extamente igual a 20% ou 50% do *limite_velocidade*, a multa de maior gravidade
    será aplicada.
    Exemplos:
    >>> pontos_na_carteira(41, 30)
    5
    >>> pontos_na_carteira(95, 60)
    7
    >>> pontos_na_carteira(40, 60)
    0
    >>> pontos_na_carteira(103, 90)
    3
    >>> pontos_na_carteira(130, 90)
    5
    >>> pontos_na_carteira(500, 30)
    7
    '''

    velocidade = velocidade_considerada(velocidade_medida)

    if velocidade < limite_velocidade:
        pontos = 0

    elif velocidade < limite_velocidade*1.2:
        pontos = 3

    elif velocidade < limite_velocidade*1.5:
        pontos = 5

    else:
        pontos = 7

    return pontos






















    
