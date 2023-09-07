from datetime import date

def Verificar_saldo(val):
    if  Pessoa1.contaIn.saldo + Pessoa1.contaP.saldo >= val:
        True
    else:
        False
        
class Conta:
    def __init__(self):
        Pessoa.__init__(self)
        self.tp_conta = None
        self.dt_abertura = date.today()
        self.saldo = 0  
        
    def sacar(self,val):
        if Verificar_saldo(val):
            print(f'O valor de {val}R$ foi sacado')
        else:
            print("Não é possivel sacar o valor")
            
    def depositar(self,val):
        self.saldo += val
        print(f'O valor de {val}R$ foi depositado')
    
    
class ContaP(Conta):
    def __init__(self):
        Conta.__init__(self)
        self.tp_conta = "Poupança"



class ContaIn(Conta):
    def __init__(self):
        Conta.__init__(self)
        self.tp_conta = "Investimento"


class Pessoa:
    def __init__(self):
        self.contaP = None
        self.contaIn = None
        self.name = self.__class__.__name__
        
    def Create_Conta(self):
        conta = ''
        
        while conta != '1' and conta != '2':
            conta = input(f"[SYSTEM]Qual conta deseja criar?\n[1] - POUPANÇA\n[2] - INVESTIMENTO\n")
        if conta == '1':
            self.contaP = ContaP()
            print("[SYSTEM]CONTA CRIADA\n")
            
        else:
            self.contaIn = ContaIn()
            print("[SYSTEM]CONTA CRIADA\n")
            
    
            
Pessoa1 = Pessoa()

Pessoa1.Create_Conta()
Pessoa1.Create_Conta()

Pessoa1.contaP.depositar(500)
Pessoa1.contaIn.depositar(400)


Pessoa1.contaP.sacar(901)
       


        
        

        
        
        
    
    