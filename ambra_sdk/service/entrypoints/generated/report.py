""" Report.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import MissingFields
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import ReportFailed
from ambra_sdk.service.query import QueryO

class Report:
    """Report."""

    def __init__(self, api):
        self._api = api

    
    def status(
        self,
        report_id,
    ):
        """Status.
        :param report_id: The report id
        """
        request_data = {
           'report_id': report_id,
        }
	
        errors_mapping = {}
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The report can not be found')
        errors_mapping['REPORT_FAILED'] = ReportFailed('The report failed')
        query_data = {
            'api': self._api,
            'url': '/report/status',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def zip(
        self,
        report_id,
    ):
        """Zip.
        :param report_id: The report id
        """
        request_data = {
           'report_id': report_id,
        }
	
        errors_mapping = {}
        errors_mapping['NOT_FOUND'] = NotFound('Not found')
        query_data = {
            'api': self._api,
            'url': '/report/zip',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    