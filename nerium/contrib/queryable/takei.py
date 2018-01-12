import os

import records
from dotenv import find_dotenv, load_dotenv

# Provision environment as needed
if find_dotenv():
    load_dotenv(find_dotenv())
else:
    load_dotenv('/dotenv/.env')


class TakeiQueryable():

    def results(self, query, **kwargs):
        backend_code = self.parse(query)
        backend = records.Database(self.backend_lookup(backend_code))
        results = backend.query(query, **kwargs)
        return results.as_dict()

    def get_table_list(self, query_file):
        backend_code = self.parse(query_file)
        backend = records.Database(self.backend_lookup(backend_code))
        return backend.get_table_names()

    def parse(self, file_path):
        parts = file_path.split('/')
        end = parts[-1]
        file_parts = end.split('.')
        return ''.join(file_parts[1:])

    def backend_lookup(self, backend_code):
        backend = os.getenv('{}_BACKEND'.format(backend_code.upper()),
                            "NO BACKEND")
        return backend
