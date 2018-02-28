import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from . import acme
from . import system


def get_tops():
    """
    get_tops
    Get list of top level groups.

    :rtype: List[str]
    """
    return ['config', 'status', 'command']


def get_config_groups():
    """
    get_config_groups
    Get list of config group names.

    :rtype: List[str]
    """
    return ['system', 'acme']


def get_config_group_by_name(groupName):
    """
    get_config_group_by_name
    Get list of section names in a config group.
    :param groupName: 
    :type groupName: str

    :rtype: List[str]
    """
    if groupName == 'system':
        return system.get_config_sections()
    elif groupName == 'acme':
        return acme.get_config_sections()
    else:
        return []


def get_config_section_by_name(groupName, sectionName):
    """
    get_config_section_by_name
    Get list of name:value settings in a config section.
    :param groupName: 
    :type groupName: str
    :param sectionName: 
    :type sectionName: str

    :rtype: List[InlineResponse200]
    """
    if groupName == 'system':
        return system.get_config_section(sectionName)
    elif groupName == 'acme':
        return acme.get_config_section(sectionName)
    else:
        return []


def get_status_groups():
    """
    get_status_groups
    Get list of status group names.

    :rtype: List[str]
    """
    return ['system', 'acme']


def get_status_group_by_name(groupName):
    """
    get_status_group_by_name
    Get list of section names in a status group.
    :param groupName: 
    :type groupName: str

    :rtype: List[str]
    """
    if groupName == 'system':
        return system.get_status_sections()
    elif groupName == 'acme':
        return acme.get_status_sections()
    else:
        return []


def get_status_section_by_name(groupName, sectionName):
    """
    get_status_section_by_name
    Get list of name:value settings in a status section.
    :param groupName: 
    :type groupName: str
    :param sectionName: 
    :type sectionName: str

    :rtype: List[InlineResponse200]
    """
    if groupName == 'system':
        return system.get_status_section(sectionName)
    elif groupName == 'acme':
        return acme.get_status_section(sectionName)
    else:
        return []
