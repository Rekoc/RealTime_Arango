#python 3.5.X
#Made for ArangoDB 3.1.X - Developer version & python-arango driver 3.X

class DataFormating:

    imput_data = ''
    output_data = {}

    def __init__(self, data):
        print ('(DataFormating)(__init__) Dataformating object created')
        self._imput_data(self, data)

    def _imput_data(self, new_value):
        print ('DataFormating)(_data_imput) new value will be : ', new_value)
        self.imput_data = new_value

    @property
    def _imput_data(self):
        return print ('imput_data = ', imput_data)

    @property
    def _output_data(self):
        return print ('output_data = ', output_data)

    def data_analyse(self):
        self._imput_data()

    def __str__(self):
        return 'Data_Formating'
