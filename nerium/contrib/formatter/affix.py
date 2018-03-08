import datetime

from flask import request
from nerium import ResultFormatter


class AffixFormatter(ResultFormatter):
    """ Wrap default object array with error and metadata details
    """
    def format_results(self):
        formatted = {}
        formatted['error'] = False
        formatted['response'] = self.result
        formatted['metadata'] = {}
        formatted['metadata']['executed'] = datetime.datetime.now().isoformat()
        formatted['metadata']['params'] = request.args.to_dict()
        return formatted
