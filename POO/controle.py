class ControleRemoto:
    def __init__(self, cor, altura, largura,expessura,quantidade_botoes,):
        self.cor = str(cor) 
        self.altura = float(altura)
        self.largura = float(largura)
        self.expessura = float(expessura)
        self.quantidade_botoes = int(quantidade_botoes)
        self.tv = False

    def LigarTv(self):
       if self.tv == False:
           self.tv == True
           
    def AumetarVolume(self):
        
    def DesligarTV(self):
         pass
    

controle1 = ControleRemoto(cor='preto',
                        altura='15.5',
                        largura='0.5',
                        expessura=5,
                        quantidade_botoes=10)

print(controle1.cor,controle1.altura,controle1.largura,controle1.expessura,controle1.quantidade_botoes)
















