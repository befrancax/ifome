import PySimpleGUI as sg




# criar as janelas e layouts
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)




def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar pedido', layout=layout, finalize=True)
# criar janelas iniciais
janela1,janela2 = janela_login(), None
#criar loop de leitura dos eventos
while True:
    window,event,values = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # próxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values ['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza Catupiry c/ Frango')
        elif values['pizza1'] == True :
            sg.popup('Foi solicitado uma Pizza Pepperoni')
        elif values['pizza2'] == True :
            sg.popup('Foi solicitado uma Pizza Frango c/ Catupiry')

#lógica do que acontece ao clicar nos botões