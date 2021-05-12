import csv
import itertools
import shutil
from PySimpleGUI import OneLineProgressMeter as progress
from screen import frame
from os import chdir, listdir, mkdir
from platform import system
from datetime import datetime


class MoveCSV:
    def __init__ (self, user_input):
        self.csv = str(user_input[0])
        self.files_path = str(user_input[1])
        self.csv_itens = None
        self.file_list = None
        self.file_listex = None
        self.user_os = None
        self.os_separator = None
        self.moved_dir = None

    def os_name(self):
        os_name = system()
        self.os_separator = '/'
#        if ('Windows' in os_name):
 #           self.os_separator = '\\'
  #      elif ('Darwin' in os_name) or ('Linux' in os_name):
   #         self.os_separator = '/'
    #    else:
     #       self.os_separator = '\\'

        
    def get_list_files(self):
        chdir(self.files_path)
        self.file_list = listdir()

    def file_extension_remove(self):
        file_listex = []
        for file in self.file_list:
            if '.' in file:
                file_without_ext = file.rsplit('.', 1)
                file_listex.append(file_without_ext[0])
            else:
                file_listex.append(file)
        self.file_listex = file_listex

    def mkdir_moved(self):
        try:
            chdir(self.files_path)
            now = datetime.now()
            dir_name = str('MOVIDO-' + now.strftime("%H%M%S"))
            mkdir(dir_name)
            self.moved_dir = dir_name
        except:
            print("Não foi possivel criar pasta para mover os arquivos")
    
    def read_csv(self):
        print("files path: ",self.csv,"\nos separatou: ",self.os_separator)
        csv_path, csv_name = self.csv.rsplit(self.os_separator, 1)
        chdir(csv_path)
        csv_itens = list(itertools.chain.from_iterable(csv.reader(open(csv_name))))
        self.csv_itens = csv_itens
    
    def move_files(self):
        files_to_move = []
        current_file = 0
        chdir(self.files_path)
        for item in self.csv_itens:
            for file in self.file_list:
                if item in file:
                    files_to_move.append(file)

        for file in files_to_move:
            current_file += 1
            if current_file < len(files_to_move):
                progress('Momento Arquivos', current_file, len(self.file_list), 'single')

            full_path_file = self.files_path + self.os_separator + file
            full_path_file_moved = self.files_path + self.os_separator + self.moved_dir + self.os_separator + file
            shutil.move(full_path_file, full_path_file_moved)

    


user_input = frame()
app = MoveCSV(user_input)
app.os_name()
app.get_list_files()
app.file_extension_remove()
app.mkdir_moved()
app.read_csv()
app.move_files()

