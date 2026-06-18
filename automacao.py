import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "teste@hotmail.com"
senha = "senhadoemail"


pyautogui.PAUSE = 0.2
#PASSO 1
#tecla windows
#pesquisar edge
#colocar o link do sistema
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
pyautogui.sleep(1.5)
pyautogui.write(link)
pyautogui.press("enter")

#PASSO 2
#clicar no campo de email
#digitar o email
#colocar a senha
#entrar no sistema
pyautogui.sleep(2)
pyautogui.click(x=526, y=369)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.sleep(2)

#PASSO 3
#pegar as informações dos produtos
#cadastrar em suas devidas categorias até acabar a lista do csv

#usando pandas pra ler o csv com os dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#PASSO 4
#repetir

for linha in tabela.index:
    pyautogui.click(x=510, y=254)
    #codigo
    #para localizar algum dado específico em uma tabela, é necessário usar esse mesmo formato nomedatabela.loc[variavel, "nomedacoluna"]
    codigo = tabela.loc[linha, "codigo"]   
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)   
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)  
    