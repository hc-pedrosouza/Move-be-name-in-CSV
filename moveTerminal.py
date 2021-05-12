import csv
from os import chdir, listdir, mkdir
import itertools
from platform import system
import shutil


def choose_dir_sepator():
    try:
        os_name = system()

        if ('Windows' in os_name):
            os_separator = '\\'
        elif ('Darwin' in os_name) or ('Linux' in os_name):
            os_separator = '/'
        else:
            os_separator = '\\'
    except:
        os_by_user = input(
            "Qual sistema operacional você está utilizando?\nWindows   Linux   Mac\n")
        os_by_user = os_by_user.lower()

        if ('window' in os_by_user):
            os_separator = '\\'
        elif ('mac' in os_by_user) or ('linux' in os_by_user):
            os_separator = '/'
        else:
            os_separator = '\\'
    return os_separator


def get_list_files():
    files_local = input(
        "Informe o caminho da pasta estão localizados os arquivos: ")
    chdir(files_local)
    file_list = listdir()
    return (file_list, files_local)


def get_csv(os_separator):

    try:
        csv_fullpath = input(
            "Informe o caminho do CSV contendo os itens que deseja mover.\n     Ex: C:\\Users\\hcped\\Downloads\\ListaChaveNFCe.csv\nCaminho do CSV: ")
        temp_csv_name = csv_fullpath.rsplit(os_separator, 1)
        csv_name = str(temp_csv_name[1])
        csv_local = str(temp_csv_name[0])
        chdir(csv_local)
    except:
        raise("\nCaminho do arquivo CSV informado incorretamente")

    return(csv_local, csv_name)


def file_extension_remove(file_list):
    file_list_without_ext = []
    for file in file_list:
        if '.' in file:
            file_without_ext = file.rsplit('.', 1)
            file_list_without_ext.append(file_without_ext[0])
        else:
            file_list_without_ext.append(file)
    return file_list_without_ext


def mkdir_to_move(files_local):
    try:
        chdir(files_local)
        mkdir('Moved')
    except:
        print("Não foi possivel criar pasta para mover os arquivos")


def read_csv(csv_local,csv_name):
    chdir(csv_local)
    csv_itens = list(itertools.chain.from_iterable(csv.reader(open(csv_name))))
    return csv_itens


def get_files_to_move(csv_itens, files_list):
    files_to_move = []
    for item in csv_itens:
        for file in files_list:
            if item in file:
                files_to_move.append(file)
    return files_to_move


def move_files(files_local, files_to_move, os_separator):
    for file in files_to_move:
        full_path_file = files_local + os_separator + file
        full_path_file_moved = files_local + os_separator + "Moved"
        shutil.move(full_path_file, full_path_file_moved)


os_separator = choose_dir_sepator()
files_list, files_local = get_list_files()
csv_name = get_csv(os_separator)
file_list_without_ext = file_extension_remove(files_list)
mkdir_to_move(files_local)
csv_itens = read_csv(csv_name[0], csv_name[1])
files_to_move = get_files_to_move(csv_itens, files_list)
move_files(files_local, files_to_move, os_separator)
