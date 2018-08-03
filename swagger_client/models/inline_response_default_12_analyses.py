# coding: utf-8

"""
    neuroscout

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponseDefault12Analyses(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'hash_id': 'str',
        'modified_at': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'description': 'description',
        'hash_id': 'hash_id',
        'modified_at': 'modified_at',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, description=None, hash_id=None, modified_at=None, name=None, status=None):  # noqa: E501
        """InlineResponseDefault12Analyses - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._hash_id = None
        self._modified_at = None
        self._name = None
        self._status = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if hash_id is not None:
            self.hash_id = hash_id
        if modified_at is not None:
            self.modified_at = modified_at
        self.name = name
        if status is not None:
            self.status = status

    @property
    def description(self):
        """Gets the description of this InlineResponseDefault12Analyses.  # noqa: E501


        :return: The description of this InlineResponseDefault12Analyses.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponseDefault12Analyses.


        :param description: The description of this InlineResponseDefault12Analyses.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hash_id(self):
        """Gets the hash_id of this InlineResponseDefault12Analyses.  # noqa: E501

        Hashed analysis id.  # noqa: E501

        :return: The hash_id of this InlineResponseDefault12Analyses.  # noqa: E501
        :rtype: str
        """
        return self._hash_id

    @hash_id.setter
    def hash_id(self, hash_id):
        """Sets the hash_id of this InlineResponseDefault12Analyses.

        Hashed analysis id.  # noqa: E501

        :param hash_id: The hash_id of this InlineResponseDefault12Analyses.  # noqa: E501
        :type: str
        """

        self._hash_id = hash_id

    @property
    def modified_at(self):
        """Gets the modified_at of this InlineResponseDefault12Analyses.  # noqa: E501


        :return: The modified_at of this InlineResponseDefault12Analyses.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this InlineResponseDefault12Analyses.


        :param modified_at: The modified_at of this InlineResponseDefault12Analyses.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def name(self):
        """Gets the name of this InlineResponseDefault12Analyses.  # noqa: E501

        Analysis name.  # noqa: E501

        :return: The name of this InlineResponseDefault12Analyses.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponseDefault12Analyses.

        Analysis name.  # noqa: E501

        :param name: The name of this InlineResponseDefault12Analyses.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this InlineResponseDefault12Analyses.  # noqa: E501

        PASSED, FAILED, PENDING, or DRAFT.  # noqa: E501

        :return: The status of this InlineResponseDefault12Analyses.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponseDefault12Analyses.

        PASSED, FAILED, PENDING, or DRAFT.  # noqa: E501

        :param status: The status of this InlineResponseDefault12Analyses.  # noqa: E501
        :type: str
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponseDefault12Analyses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
