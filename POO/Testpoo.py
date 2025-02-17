class carro:
    def __init__(self, modelo, cor, ano_fabricacao, capacidade_tanque):  
        self.modelo = modelo 
        self.cor = cor
        self.ano_fabricacao = ano_fabricacao
        self.capacidade_tanque = capacidade_tanque
        self.velocidade = 0
        self.acelerar = 0
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print('o carro já está ligado') 
        else:
            print('carro ligou!')
            self.ligado = True

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1.2*tempo
            self.tanque -= (tempo/60)*15
            print('Carro em movimento ... 🚙💨💨')

    def freiar(self):
        if self.ligado and self.velocidade != 0:
            self.velocidade -= 0.8*tempo
            print('Carro parando ... 🚙⏩')
            if self.velocidade < 0:
                self.velocidade = 0
                print('O carro parou ... 🚙⬇️')
        else:
            ('O carro já está parado ... 🚙❌')
        
meu_carro = carro(modelo='sedan', cor='vermelha', ano_fabricacao='2012', capacidade_tanque='30.500')
print(meu_carro)







