import json
from jproperties import Properties

class Loader():
    def __init__(self):
        self.rdf_dict = {}
        self.filter = []
        self.target_list = []
        self.configs = Properties()
        self.fields = []
    
    def load_config(self):
        # self.configs = Properties()
        with open('lucene/application.properties', 'rb') as config_file:
            self.configs.load(config_file)
        return self.configs

    def load_rdf(self):
        file = open(self.configs['RDF_JSON'].data)
        rdf_dict = json.load(file)
        return rdf_dict

    def load_filters(self):
        filter = self.configs['filters'].data
        filter = json.loads(filter)
        return filter

    def load_target_list(self):
        target_list = self.configs['target_list'].data
        target_list = json.loads(target_list)
        return target_list

    def load_fields(self):
        self.fields = self.configs['fields'].data
        self.fields = json.loads(self.fields)
        return self.fields