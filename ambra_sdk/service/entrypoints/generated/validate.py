""" Validate.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import FilterNotFound
from ambra_sdk.exceptions.service import InUse
from ambra_sdk.exceptions.service import InvalidCondition
from ambra_sdk.exceptions.service import InvalidField
from ambra_sdk.exceptions.service import InvalidSortField
from ambra_sdk.exceptions.service import InvalidSortOrder
from ambra_sdk.exceptions.service import MissingFields
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import NotPermitted
from ambra_sdk.service.query import QueryO
from ambra_sdk.service.query import QueryOPSF

class Validate:
    """Validate."""

    def __init__(self, api):
        self._api = api

    
    def list(
        self,
        account_id,
    ):
        """List.
        :param account_id: The account id
        """
        request_data = {
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping['FILTER_NOT_FOUND'] = FilterNotFound('The filter can not be found. The error_subtype will hold the filter UUID')
        errors_mapping['INVALID_CONDITION'] = InvalidCondition('The condition is not support. The error_subtype will hold the filter expression this applies to')
        errors_mapping['INVALID_FIELD'] = InvalidField('The field is not valid for this object. The error_subtype will hold the filter expression this applies to')
        errors_mapping['INVALID_SORT_FIELD'] = InvalidSortField('The field is not valid for this object. The error_subtype will hold the field name this applies to')
        errors_mapping['INVALID_SORT_ORDER'] = InvalidSortOrder('The sort order for the field is invalid. The error_subtype will hold the field name this applies to')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to view the validation rule')
        query_data = {
            'api': self._api,
            'url': '/validate/list',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        query_data['paginated_field'] = 'validates'
        return QueryOPSF(**query_data)
    
    def add(
        self,
        account_id,
        conditions,
        name,
    ):
        """Add.
        :param account_id: The account id
        :param conditions: The validation conditions
        :param name: The validation rule name
        """
        request_data = {
           'name': name,
           'conditions': conditions,
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping['INVALID_CONDITION'] = InvalidCondition('A condition is invalid. The error_subtype holds more detail')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The object was not found. The error_subtype holds the type of the object')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to add validation rules')
        query_data = {
            'api': self._api,
            'url': '/validate/add',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def set(
        self,
        conditions,
        name,
        uuid,
    ):
        """Set.
        :param conditions: The validation conditions
        :param name: The validation rule name
        :param uuid: The validation id
        """
        request_data = {
           'uuid': uuid,
           'name': name,
           'conditions': conditions,
        }
	
        errors_mapping = {}
        errors_mapping['INVALID_CONDITION'] = InvalidCondition('A condition is invalid. The error_subtype holds more detail')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The validation rule was not found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to add validation rules')
        query_data = {
            'api': self._api,
            'url': '/validate/set',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def get(
        self,
        uuid,
    ):
        """Get.
        :param uuid: Id of the validate
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The validate was not found.')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to view the validation rule')
        query_data = {
            'api': self._api,
            'url': '/validate/get',
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
        :param uuid: Id of the validation rule
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping['IN_USE'] = InUse('The validation rule is used in a routing rule')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The validation rule  was not found.')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to delete the validation rule')
        query_data = {
            'api': self._api,
            'url': '/validate/delete',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    