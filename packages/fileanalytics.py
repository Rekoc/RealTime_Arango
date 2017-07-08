#python 3.5.X


class FileAnalytics:

    path_file = ''
    liste = []
    splitter = ';'

    def __init__(self, path):
        # print('(DataFormating)(__init__) Dataformating object created')
        self.path_file = path

    def get_dic_from_two_lists(self, keys, values):
        return {keys[i]: values[i] for i in range(len(keys)-1)}

    def treat_line(self, line):
        # print('(DataFormating)(treat_line) BEGIN')
        line_treated = line.split(self.splitter)
        for i in range(line.count(self.splitter) + 1):
            self.liste.append(line_treated[i])
        # print('(DataFormating)(treat_line) liste = ', self.liste)
        return line_treated

    def read_file(self):
        # print('(DataFormating)(read_file) BEGIN')
        with open(self.path_file, 'r') as file:
            line = 'empty'
            while line:
                line = file.readline()
                # print('(DataFormating)(read_file) line = ', line)
                self.treat_line(line)
        return self.liste

    def __str__(self):
        return 'File_Analytics'
