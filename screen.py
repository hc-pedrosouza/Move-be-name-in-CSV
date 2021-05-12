import PySimpleGUI as gui


def frame():
    user_input = {}

    layout = [
        [gui.Text("'.CSV ' CONTENDO LISTA DE ARQUIVOS A SEREM MOVIDOS")],
        [gui.Input(size=(65,1)), gui.FileBrowse('Procurar', file_types=(('CSV', '.csv'),('Todos Arquivos', '.*')), )],
        [gui.Text('')],
        [gui.Text('PASTA COM ARQUIVOS PARA MOVER')],
        [gui.Input(size=(65,1)), gui.FolderBrowse('Procurar')],
        [gui.OK(),gui.Cancel()]
    ]

    window = gui.Window("MOVER ARQUIVOS A PARTIR DO CSV", layout, size=(560, 200), resizable=True, icon=False)
    event, user_input = window.read()

    if len(user_input[0]) <= 2:
        raise("Nenhuma opção selecionada")
    
    elif event == 'OK':
        user_input.pop("Procurar")
        user_input.pop("Procurar0")
        user_input = user_input

    else:
        raise("Nenhuma opção selecionada")

    return user_input