import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'


pyautogui.press('win')
pyautogui.write('chrom')
pyautogui.press('enter')
pyautogui.hotkey("win","up")

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=701, y=374)
pyautogui.write('felipe123@gmail.com')
pyautogui.press('tab')
pyautogui.write('123vvervrvvr89')
pyautogui.press('enter')
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index :
    #codigo
    codigo = str(tabela.loc[linha,'codigo'])
    pyautogui.click(x=838, y=253)
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    marca = str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    #tipo
    tipo =  str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    #categoria
    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    #preço
    preco = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    #custo
    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    #obs    
    obs = str(tabela.loc[linha,'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(6000) 
