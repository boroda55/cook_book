class Line:
    def __init__(self, name_file=''):
        self.name_file = name_file
        self.count_lines = 0
        self.file_dict = {}

    # Чтение файлов которые были предоставлены
    def write_file(self):
        file_list = []
        with open(self.name_file, 'r', encoding='utf-8') as f:
            for i in f.read().splitlines():
                file_list.append(i)
        self.count_lines = len(file_list)
        self.file_dict = {'name_file' : self.name_file, 'count_lines' : self.count_lines}
    # Функция сортировки, сделал отдельно, что бы не запутаться
    def __comparison(self, file_dict1={}, file_dict2={}, file_dict3={}):
        files_dict = [file_dict1, file_dict2, file_dict3]
        sorted_files_dict = sorted(files_dict, key=lambda x: x['count_lines'])
        return sorted_files_dict
    # Функция создания нового файла и добавление текста для решения задания №3
    def new_file(self, file_dict1={}, file_dict2={}, file_dict3={}):
        with open('task3.txt', 'w', encoding='utf-8') as f:
            sorted_files_dict = self.__comparison(file_dict1, file_dict2, file_dict3)
            for sorted_file_dict in sorted_files_dict:
                f.write(sorted_file_dict['name_file']+'\n')
                f.write(str(sorted_file_dict['count_lines'])+'\n')
                i = 1
                while i <= sorted_file_dict['count_lines']:
                    f.write(f'Строка номер {i} файла номер {sorted_file_dict['name_file'][:-4]}\n')
                    i += 1

# Создание объектов 3 файлов и чтение их
txt1 = Line('1.txt')
txt1.write_file()

txt2 = Line('2.txt')
txt2.write_file()

txt3 = Line('3.txt')
txt3.write_file()

# Решение Задания 3
#task_3 = Line()
#task_3.new_file(txt1.file_dict, txt2.file_dict, txt3.file_dict)

### Сортировка от П понял, но задание просто не так понял немного
def merge_files(file_names):
    sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[1])

    with open('result.txt', 'w', encoding='utf-8') as result_file:
        for file_name, line_count in sorted_file_data:
            file_content = open(file_name, encoding='utf-8').read()
            result_file.write(f'Имя файла: {file_name}\n')
            result_file.write(f'Количество строк: {line_count}\n')
            result_file.write(file_content + '\n\n')

merge_files(['1.txt', '2.txt', '3.txt'])