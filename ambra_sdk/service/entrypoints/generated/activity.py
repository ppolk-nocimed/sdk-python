""" Activity.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import FilterNotFound
from ambra_sdk.exceptions.service import InvalidCondition
from ambra_sdk.exceptions.service import InvalidField
from ambra_sdk.exceptions.service import InvalidSortField
from ambra_sdk.exceptions.service import InvalidSortOrder
from ambra_sdk.exceptions.service import MissingFields
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import NotPermitted
from ambra_sdk.exceptions.service import Running
from ambra_sdk.service.query import QueryO
from ambra_sdk.service.query import QueryOF
from ambra_sdk.service.query import QueryOPSF

class Activity:
    """Activity."""

    def __init__(self, api):
        self._api = api

    
    def list(
        self,
        account_id,
        strict_account_filter=None,
    ):
        """List.
        :param account_id: Limit to activities in this account and the personal activities
        :param strict_account_filter: Flag to apply the account_id to personal activites as well (optional)
        """
        request_data = {
           'strict_account_filter': strict_account_filter,
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping['FILTER_NOT_FOUND'] = FilterNotFound('The filter can not be found. The error_subtype will hold the filter UUID')
        errors_mapping['INVALID_CONDITION'] = InvalidCondition('The condition is not support. The error_subtype will hold the filter expression this applies to')
        errors_mapping['INVALID_FIELD'] = InvalidField('The field is not valid for this object. The error_subtype will hold the filter expression this applies to')
        errors_mapping['INVALID_SORT_FIELD'] = InvalidSortField('The field is not valid for this object. The error_subtype will hold the field name this applies to')
        errors_mapping['INVALID_SORT_ORDER'] = InvalidSortOrder('The sort order for the field is invalid. The error_subtype will hold the field name this applies to')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        query_data = {
            'api': self._api,
            'url': '/activity/list',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        query_data['paginated_field'] = 'activities'
        return QueryOPSF(**query_data)
    
    def list_count(
        self,
        account_id,
    ):
        """List count.
        :param account_id: Limit to activities in this account and the personal activities
        """
        request_data = {
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping['FILTER_NOT_FOUND'] = FilterNotFound('The filter can not be found. The error_subtype will hold the filter UUID')
        errors_mapping['INVALID_CONDITION'] = InvalidCondition('The condition is not support. The error_subtype will hold the filter expression this applies to')
        errors_mapping['INVALID_FIELD'] = InvalidField('The field is not valid for this object. The error_subtype will hold the filter expression this applies to')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['RUNNING'] = Running('This call is currently runnning for the user')
        query_data = {
            'api': self._api,
            'url': '/activity/list/count',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryOF(**query_data)
    
    def get(
        self,
        uuid,
    ):
        """Get.
        :param uuid: The activity uuid
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The activity was not found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to access this activity')
        query_data = {
            'api': self._api,
            'url': '/activity/get',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def delete(
        self,
        uuid,
    ):
        """Delete.
        :param uuid: The activity uuid
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The activity was not found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to delete this activity')
        query_data = {
            'api': self._api,
            'url': '/activity/delete',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    