# python 3.5.X
# AQL request management


class AqlRequest:

    value = ''
    column = ''
    collection = ''
    AQL_request = ''

    def __init__(self, collection, choice):
        print('(AqlRequest)(__init__) AqlRequest object was created')
        self.collection = collection
        self.roudabout(choice)

    @property
    def _collection(self):
        return self.collection

    @property
    def _column(self):
        return self.column

    @property
    def _value(self):
        return self.value

    def more_than(self):
        print('(AqlRequest)(more_than) Witch column ?')
        self.column = input()
        print('(AqlRequest)(more_than) Witch value ?')
        self.value = input()
        # print('(AqlRequest)(more_than) Witch collection ?')
        # self.collection = collection
        self.AQL_request = 'FOR doc IN ' + self.collection + ' FILTER doc.' + self.column + ' > ' + \
                           self.value + ' RETURN doc'

    def less_than(self):
        print('(AqlRequest)(less_than) Witch column ?')
        self.column = input()
        print('(AqlRequest)(less_than) Witch value ?')
        self.value = input()
        # print('(AqlRequest)(more_than) Witch collection ?')
        # self.collection = collection
        self.AQL_request = 'FOR doc IN ' + self.collection + ' FILTER doc.' + self.column + ' > ' + \
                           self.value + ' RETURN doc'

    def equal_to(self):
        print('(AqlRequest)(equal_to) Witch column ?')
        self.column = input()
        print('(AqlRequest)(equal_to) Witch value ?')
        self.value = input()
        # print('(AqlRequest)(more_than) Witch collection ?')
        # self.collection = collection
        self.AQL_request = 'FOR doc IN ' + self.collection + ' FILTER doc.' + self.column + ' == ' + \
                           self.value + ' RETURN doc'

    def different_from(self):
        print('(AqlRequest)(different_from) Witch column ?')
        self.column = input()
        print('(AqlRequest)(different_from) Witch value ?')
        self.value = input()
        # print('(AqlRequest)(more_than) Witch collection ?')
        # self.collection = collection
        self.AQL_request = 'FOR doc IN ' + self.collection + ' FILTER doc.' + self.column + ' != ' + \
                           self.value + ' RETURN doc'

    def roudabout(self, choice):
        options = {
            'more_than': self.more_than,
            'less_than': self.less_than,
            'equal_to': self.equal_to,
            'different_from': self.different_from
        }
        # print('(AqlRequest)(roudabout) options created')
        # Made a choice with the "choice" argue
        options[choice]()
        del options
        # print('(AqlRequest)(roudabout) options deleted')

    def __str__(self):
        return 'AqlRequest'
