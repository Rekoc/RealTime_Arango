# python 3.5.X
# Made for ArangoDB 3.1.X - Developer version & python-arango driver 3.X

from arango import ArangoClient, ArangoError
from Gui.AqlRequest import AqlRequest
from Gui.Terminal import Terminal


class DataManagement():

    # Client containe server abd database information
    client = ArangoClient()
    # Database will be create from the client 'client'
    database = client
    # Collection will be add/move/delete from database 'db'
    data = database

    # Database information
    database_name = 'database1'
    database_host = '127.0.0.1'
    database_port = 8529
    database_status = True
    user_name = 'root'
    user_password = ''
    ###########################

    def __init__(self):
        # print('(DataManagement)(__init__) DataManagement object created')
        pass

    def _database_name(self, new_value):
        # print('database_name will be :', new_value)
        self.database_name = new_value

    @property
    def _database_name(self):
        return self.database_name

    def _database_host(self, new_value):
        # print ('database_host will be :', new_value)
        self.database_host = new_value

    @property
    def _database_host(self):
        return self.database_host

    def _database_port(self, new_value):
        # print('database_port will be :', new_value)
        self.database_port = new_value

    @property
    def _database_port(self):
        return self.database_port

    def _user_name(self, new_value):
        # print('user_name will be :', new_value)
        self.user_name = new_value

    @property
    def _user_name(self):
        return self.user_name

    def _user_password(self, new_value):
        # print('user_password will be :', new_value)
        self.user_password = new_value

    @property
    def _user_password(self):
        return self.user_password

    @property
    def _database_status(self):
        return self.database_status

    def create_database(self):
        # Create IHM
        window = Terminal(False)
        ###########
        # Need to be in manual
        '''self.database_name = window.enter_value_automatic('database1')
        self.database_host = window.enter_value_automatic('127.0.0.1')
        self.database_port = window.enter_value_automatic(8529)
        self.user_name = window.enter_value_automatic('root')
        self.user_password = window.enter_value_automatic('')'''
        ###########

        # Initialize the client for ArangoDB
        self.client = ArangoClient(
            protocol='http',
            host=self.database_host,
            port=self.database_port,
            username=self.user_name,
            password=self.user_password,
            enable_logging=True
        )
        # Create a new database named "databaseName"
        print('(DataManagement)(create_database) self.database_name = ', self.database_name)
        try:
            self.database = self.client.create_database(self.database_name)
        except ConnectionError as exc:
            print('(DataManagement)(create_database)', repr(exc))
            self.database_status = False
        except ArangoError as exc:
            print('(DataManagement)(create_database)', repr(exc))
            self.database = self.client.database(self.database_name)
            # print('(DataManagement)(create_database)', self.database.properties())
        
        if self.user_name == False:
            # print('(DataManagement)(create_database) Your database was created with these information :')
            # print("(DataManagement)(create_database) protocol = 'http' ")
            # print("(DataManagement)(create_database) host = ", self.database_host)
            # print("(DataManagement)(create_database) port = ", self.database_port)
            return self.database
        else:
            try:
                self.client.create_user(self.user_name, self.user_password)
                self.client.grant_user_access(self.user_name, self.database_name)
            except ArangoError as exc:
                print('(DataManagement)(create_database)', repr(exc))
            # print('(DataManagement)(create_database) Your database was created with these information :')
            # print("(DataManagement)(create_database) protocol = 'http' ")
            # print("(DataManagement)(create_database) host = ", self.database_host)
            # print("(DataManagement)(create_database) port = ", self.database_port )
            # print("(DataManagement)(create_database) user = ", self.user_name)
            # print("(DataManagement)(create_database) password = ", self.user_password)
            return self.database

    def add_collection(self, collection_name):
        try:
            self.data = self.database.create_collection(collection_name)
            # print('(DataManagement)(add_collection)', self.data.all())
        except ArangoError as exc:
            self.data = self.database.collection(collection_name)
            # print('(DataManagement)(add_collection)', self.data.all())
            print('(DataManagement)(add_collection)', repr(exc))

    def add_data(self, **kwargs):
        if len(kwargs) != 0:
            # self.add_collection()
            try:
                result = self.data.insert(kwargs, return_new=True)
                # print('(DataManagement)(add_data)', result['_id'],
                # result['_key'], result['_rev'])
                return result
            except ArangoError as exc:
                print('(DataManagement)(add_data) _key already exist', repr(exc))
                return kwargs

        else:
            print('(DataManagement)(add_data) No data !')
            return kwargs

    def read_data(self, key):
        try:
            return self.database.get_document(key)
        except ArangoError as exc:
            print('(DataManagement)(read_data) ', repr(exc))

    '''def find_key(self):
        key = self.data.find(53)
        return key'''

    def use_query(self, collection, function_name):
        # print('(DataManagement)(create_query) BEGIN')
        aql = AqlRequest(collection, function_name)
        self.add_collection(aql.collection)
        # print('(DataManagement)(create_query) Collection OK')
        # Retrieve the execution plan without running the query
        self.database.aql.explain(aql.AQL_request)
        # Validate the query without executing it
        if self.database.aql.validate(aql.AQL_request):
            # Execute the query
            cursor = self.database.aql.execute(
                aql.AQL_request
            )
            # Iterate through the result cursor
            print([line['_key'] for line in cursor])
        else:
            print('(DataManagement)(use_query) AQL error ! Check your AQL request.')
        del aql

    def use_specific_query(self, collection, query):
        self.add_collection(collection)
        self.database.aql.explain(query)
        if self.database.aql.validate(query):
            # Execute the query
            cursor = self.database.aql.execute(
                query
            )
            print([line['_key'] for line in cursor])
        else:
            print('(DataManagement)(use_specific_query) AQL error ! Check your AQL request.')

    def create_user(self):
        if self.user_name == False:
            return 0
            # print('(DataManagement)(create_database) User name missing !')
            # print('(DataManagement)(
            # create_database) User creation cancelled')
        else:
            self.client.create_user(self.user_name, self.user_password)
            self.client.grant_user_access(self.user_name, self.database_name)
            # print('(DataManagement)(create_database) Your user was created with these information :')
            # print("(DataManagement)(create_database) user = ", self.user_name)
            # print("(DataManagement)(create_database) password = ", self.user_password)
            return 1

    def __str__(self):
        return 'Data Management'
    
    #def deleteDatabase()
