from tkinter import *
from Calc import CalcZeroF


#função para chamar a classe com parametros para seus atributos
def chamaClasse():
    #atualiza variáveis que serão parametros para atributos da classe
    fun = fEntry.get()
    aI = aEntry.get()
    bI = bEntry.get()
    pr = pEntry.get()
    metd = metodo.get()
    #chama metodo para atualizar atributos da classe e verificar metodo de calculo escolhido
    CalcZeroF.Controle(self = CalcZeroF, f=fun, a=aI, b=bI,p=pr,metodo=metd)

window = Tk() #instanciando a classe Tk para criar uma janela

fLabel = Label( window,
                text ='função') #cria label e indica o que nele deve estar escrito
fLabel.pack() #insere label na janela

fEntry = Entry(
    window,
    font=("Arial", 15), #cria prompt de entrada
)
fEntry.pack()

aLabel = Label( 
        window,
        text ='início do intervalo')
aLabel.pack()
aEntry = Entry(
    window,
    font=("Arial", 15)
)
aEntry.pack()
bLabel = Label( window,
                text ='final do intervalo')
bLabel.pack()
bEntry = Entry(
    window,
    font=("Arial", 15)
)
bEntry.pack()
pLabel = Label( window,
                text ='precisão')
pLabel.pack()
pEntry = Entry(
    window,
    font=("Arial", 15)
)
pEntry.pack()
metodo = StringVar()

#cria botões de seleção para escolher método de cálculo
for i in range(len(CalcZeroF.nomes)):
    opc = Radiobutton(  window,
                        text=CalcZeroF.nomes[i],
                        variable=metodo,
                        value=CalcZeroF.nomes[i],
                        command=chamaClasse,
                        indicatoron=0,
                        bg="gray")
    opc.pack()

window.mainloop() #faz janela aparecer
