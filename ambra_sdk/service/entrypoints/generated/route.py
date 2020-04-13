""" Route.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import AccountNotFound
from ambra_sdk.exceptions.service import FilterNotFound
from ambra_sdk.exceptions.service import InvalidAction
from ambra_sdk.exceptions.service import InvalidCondition
from ambra_sdk.exceptions.service import InvalidField
from ambra_sdk.exceptions.service import InvalidFlag
from ambra_sdk.exceptions.service import InvalidJson
from ambra_sdk.exceptions.service import InvalidLinkage
from ambra_sdk.exceptions.service import InvalidManualRoles
from ambra_sdk.exceptions.service import InvalidOption
from ambra_sdk.exceptions.service import InvalidOtherNamespaces
from ambra_sdk.exceptions.service import InvalidSchedule
from ambra_sdk.exceptions.service import InvalidSortField
from ambra_sdk.exceptions.service import InvalidSortOrder
from ambra_sdk.exceptions.service import MissingFields
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import NotPermitted
from ambra_sdk.service.query import QueryO
from ambra_sdk.service.query import QueryOPSF

class Route:
    """Route."""

    def __init__(self, api):
        self._api = api

    
    def list(
        self,
        account_id,
    ):
        """List.
        :param account_id: uuid of the account
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
        errors_mapping['NOT_FOUND'] = NotFound('The account can not be found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to view this list')
        query_data = {
            'api': self._api,
            'url': '/route/list',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        query_data['paginated_field'] = 'routes'
        return QueryOPSF(**query_data)
    
    def add(
        self,
        actions,
        conditions,
        name,
        on_harvest,
        on_share,
        account_id=None,
        delay=None,
        delay_till_schedule=None,
        group_id=None,
        location_id=None,
        manual_roles=None,
        namespace_id=None,
        no_re_run=None,
        on_manual_route=None,
        on_thin=None,
        on_upload=None,
        options=None,
        other_namespaces=None,
        schedule=None,
        suspended=None,
    ):
        """Add.
        :param actions: Route actions in JSON format
        :param conditions: Route conditions in JSON format
        :param name: Name of the route
        :param on_harvest: Apply the rule to studies harvested into the namespace
        :param on_share: Apply the rule to studies shared into the namespace
        :param account_id: account_id
        :param delay: Number of minutes to delay running this rule for after it is triggered (optional)
        :param delay_till_schedule: Delay running this rule after it is triggered until the next scheduled time - flag (optional)
        :param group_id: group_id
        :param location_id: location_id
        :param manual_roles: A comma separated list of the uuid of roles that can run the rule manually (optional)
        :param namespace_id: namespace_id
        :param no_re_run: Do not run this rule on a re-notification from storage - flag (optional)
        :param on_manual_route: Apply this rule for a manually routed study - flag (optional)
        :param on_thin: Apply this rule to thin studies when they are created - flag (optional)
        :param on_upload: Apply the rule to studies uploaded into the namespace - flag (optional)
        :param options: Route options in JSON format (optional)
        :param other_namespaces: A comma separated list of the uuid of other namespaces to apply this rule to (optional)
        :param schedule: Route schedule in JSON format (optional)
        :param suspended: This rule is suspended and not applied - flag (optional)

        Notes:
        (account_id OR group_id OR location_id OR namespace_id) - uuid of the account, group or location or namespace the route is linked with
        """
        request_data = {
           'namespace_id': namespace_id,
           'on_manual_route': on_manual_route,
           'group_id': group_id,
           'manual_roles': manual_roles,
           'on_upload': on_upload,
           'on_harvest': on_harvest,
           'delay_till_schedule': delay_till_schedule,
           'actions': actions,
           'suspended': suspended,
           'name': name,
           'options': options,
           'conditions': conditions,
           'delay': delay,
           'schedule': schedule,
           'other_namespaces': other_namespaces,
           'on_share': on_share,
           'location_id': location_id,
           'account_id': account_id,
           'no_re_run': no_re_run,
           'on_thin': on_thin,
        }
	
        errors_mapping = {}
        errors_mapping['ACCOUNT_NOT_FOUND'] = AccountNotFound('The account was not found')
        errors_mapping['INVALID_ACTION'] = InvalidAction('An action is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_CONDITION'] = InvalidCondition('A condition is invalid. The error_subtype holds the condition')
        errors_mapping['INVALID_FLAG'] = InvalidFlag('An invalid flag was passed. The error_subtype holds the name of the invalid flag')
        errors_mapping['INVALID_JSON'] = InvalidJson('The field is not in valid JSON format. The error_subtype holds the name of the field')
        errors_mapping['INVALID_LINKAGE'] = InvalidLinkage('The linkage is invalid')
        errors_mapping['INVALID_MANUAL_ROLES'] = InvalidManualRoles('The manual_roles is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_OPTION'] = InvalidOption('An option is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_OTHER_NAMESPACES'] = InvalidOtherNamespaces('The other_namespaces is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_SCHEDULE'] = InvalidSchedule('The schedule is invalid. The error_subtype holds the error detail')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to add a route to that account')
        query_data = {
            'api': self._api,
            'url': '/route/add',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def set(
        self,
        uuid,
        actions=None,
        conditions=None,
        delay=None,
        delay_till_schedule=None,
        manual_roles=None,
        name=None,
        no_re_run=None,
        on_harvest=None,
        on_manual_route=None,
        on_share=None,
        on_thin=None,
        on_upload=None,
        options=None,
        other_namespaces=None,
        schedule=None,
        suspended=None,
    ):
        """Set.
        :param uuid: The route uuid
        :param actions: Route actions in JSON format (optional)
        :param conditions: Route conditions in JSON format (optional)
        :param delay: Number of minutes to delay running this rule for after it is triggered (optional)
        :param delay_till_schedule: Delay running this rule after it is triggered until the next scheduled time - flag (optional)
        :param manual_roles: A comma separated list of the uuid of roles that can run the rule manually (optional)
        :param name: Name of the route (optional)
        :param no_re_run: Do not run this rule on a re-notification from storage - flag (optional)
        :param on_harvest: Apply the rule to studies harvested into the namespace (optional)
        :param on_manual_route: Apply this rule for a manually routed study- flag (optional)
        :param on_share: Apply the rule to studies shared into the namespace (optional)
        :param on_thin: Apply this rule to thin studies when they are created - flag (optional)
        :param on_upload: Apply the rule to studies uploaded into the namespace - flag (optional)
        :param options: Route options in JSON format (optional)
        :param other_namespaces: A comma separated list of the uuid of other namespaces to apply this rule to (optional)
        :param schedule: Route schedule in JSON format (optional)
        :param suspended: This rule is suspended and not applied - flag (optional)
        """
        request_data = {
           'on_manual_route': on_manual_route,
           'delay': delay,
           'uuid': uuid,
           'schedule': schedule,
           'on_upload': on_upload,
           'name': name,
           'conditions': conditions,
           'options': options,
           'on_harvest': on_harvest,
           'on_share': on_share,
           'delay_till_schedule': delay_till_schedule,
           'other_namespaces': other_namespaces,
           'actions': actions,
           'no_re_run': no_re_run,
           'suspended': suspended,
           'on_thin': on_thin,
           'manual_roles': manual_roles,
        }
	
        errors_mapping = {}
        errors_mapping['INVALID_ACTION'] = InvalidAction('An action is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_CONDITION'] = InvalidCondition('A condition is invalid. The error_subtype holds the condition')
        errors_mapping['INVALID_FLAG'] = InvalidFlag('An invalid flag was passed. The error_subtype holds the name of the invalid flag')
        errors_mapping['INVALID_JSON'] = InvalidJson('The field is not in valid JSON format. The error_subtype holds the name of the field')
        errors_mapping['INVALID_MANUAL_ROLES'] = InvalidManualRoles('The manual_roles is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_OPTION'] = InvalidOption('An option is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_OTHER_NAMESPACES'] = InvalidOtherNamespaces('The other_namespaces is invalid. The error_subtype holds the error detail')
        errors_mapping['INVALID_SCHEDULE'] = InvalidSchedule('The schedule is invalid. The error_subtype holds the error detail')
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The route can not be found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to edit the route')
        query_data = {
            'api': self._api,
            'url': '/route/set',
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
        :param uuid: The route uuid
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The route can not be found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to view the route')
        query_data = {
            'api': self._api,
            'url': '/route/get',
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
        :param uuid: The route uuid
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The route can not be found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to delete the route')
        query_data = {
            'api': self._api,
            'url': '/route/delete',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def physician_alias_match(
        self,
        account_id,
        lv,
    ):
        """Physician alias match.
        :param account_id: The account to test in
        :param lv: The tag text to match against the PHYSICIAN_ALIAS rule.
        """
        request_data = {
           'lv': lv,
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping['MISSING_FIELDS'] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping['NOT_FOUND'] = NotFound('The account can not be found')
        errors_mapping['NOT_PERMITTED'] = NotPermitted('You are not permitted to do this')
        query_data = {
            'api': self._api,
            'url': '/route/physician/alias/match',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    