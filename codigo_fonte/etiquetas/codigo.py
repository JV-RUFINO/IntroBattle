from enum import Enum, auto

class Perso(Enum):
    Paladino = auto()
    Caçadora = auto()
    Suporte  = auto()
    Ladino   = auto()
    Maga     = auto()


class Stat(Enum):
    VELOCIDADE  = auto()
    ATAQUE      = auto()
    DEFESA      = auto()
    CARGA       = auto()
    VIDA        = auto()

class Magi(Enum):
    Fogo        = auto()
    Fumaça      = auto()
    Agua        = auto()
    Vento       = auto()

class Condicao(Enum):
    Buffado     = auto()
    Nerfado     = auto()
    Estavel     = auto()

class Estado(Enum):
    Idle        = auto()
    Escolhivel  = auto()
    Selecionada = auto()
    Down        = auto()

class Combate(Enum):
    Atacar      = auto()
    Magia       = auto()
    Falar       = auto()
    Pular       = auto()
