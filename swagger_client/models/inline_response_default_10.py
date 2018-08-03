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

from swagger_client.models.apiruns_task import ApirunsTask  # noqa: F401,E501


class InlineResponseDefault10(object):
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
        'acquisition': 'str',
        'dataset_id': 'int',
        'duration': 'float',
        'id': 'int',
        'number': 'str',
        'session': 'str',
        'subject': 'str',
        'task': 'ApirunsTask'
    }

    attribute_map = {
        'acquisition': 'acquisition',
        'dataset_id': 'dataset_id',
        'duration': 'duration',
        'id': 'id',
        'number': 'number',
        'session': 'session',
        'subject': 'subject',
        'task': 'task'
    }

    def __init__(self, acquisition=None, dataset_id=None, duration=None, id=None, number=None, session=None, subject=None, task=None):  # noqa: E501
        """InlineResponseDefault10 - a model defined in Swagger"""  # noqa: E501

        self._acquisition = None
        self._dataset_id = None
        self._duration = None
        self._id = None
        self._number = None
        self._session = None
        self._subject = None
        self._task = None
        self.discriminator = None

        if acquisition is not None:
            self.acquisition = acquisition
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if duration is not None:
            self.duration = duration
        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if session is not None:
            self.session = session
        if subject is not None:
            self.subject = subject
        if task is not None:
            self.task = task

    @property
    def acquisition(self):
        """Gets the acquisition of this InlineResponseDefault10.  # noqa: E501

        Acquisition  # noqa: E501

        :return: The acquisition of this InlineResponseDefault10.  # noqa: E501
        :rtype: str
        """
        return self._acquisition

    @acquisition.setter
    def acquisition(self, acquisition):
        """Sets the acquisition of this InlineResponseDefault10.

        Acquisition  # noqa: E501

        :param acquisition: The acquisition of this InlineResponseDefault10.  # noqa: E501
        :type: str
        """

        self._acquisition = acquisition

    @property
    def dataset_id(self):
        """Gets the dataset_id of this InlineResponseDefault10.  # noqa: E501

        Dataset run belongs to.  # noqa: E501

        :return: The dataset_id of this InlineResponseDefault10.  # noqa: E501
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this InlineResponseDefault10.

        Dataset run belongs to.  # noqa: E501

        :param dataset_id: The dataset_id of this InlineResponseDefault10.  # noqa: E501
        :type: int
        """

        self._dataset_id = dataset_id

    @property
    def duration(self):
        """Gets the duration of this InlineResponseDefault10.  # noqa: E501

        Total run duration in seconds.  # noqa: E501

        :return: The duration of this InlineResponseDefault10.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponseDefault10.

        Total run duration in seconds.  # noqa: E501

        :param duration: The duration of this InlineResponseDefault10.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def id(self):
        """Gets the id of this InlineResponseDefault10.  # noqa: E501


        :return: The id of this InlineResponseDefault10.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponseDefault10.


        :param id: The id of this InlineResponseDefault10.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def number(self):
        """Gets the number of this InlineResponseDefault10.  # noqa: E501

        Run id  # noqa: E501

        :return: The number of this InlineResponseDefault10.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponseDefault10.

        Run id  # noqa: E501

        :param number: The number of this InlineResponseDefault10.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def session(self):
        """Gets the session of this InlineResponseDefault10.  # noqa: E501

        Session number  # noqa: E501

        :return: The session of this InlineResponseDefault10.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this InlineResponseDefault10.

        Session number  # noqa: E501

        :param session: The session of this InlineResponseDefault10.  # noqa: E501
        :type: str
        """

        self._session = session

    @property
    def subject(self):
        """Gets the subject of this InlineResponseDefault10.  # noqa: E501

        Subject id  # noqa: E501

        :return: The subject of this InlineResponseDefault10.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this InlineResponseDefault10.

        Subject id  # noqa: E501

        :param subject: The subject of this InlineResponseDefault10.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def task(self):
        """Gets the task of this InlineResponseDefault10.  # noqa: E501


        :return: The task of this InlineResponseDefault10.  # noqa: E501
        :rtype: ApirunsTask
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this InlineResponseDefault10.


        :param task: The task of this InlineResponseDefault10.  # noqa: E501
        :type: ApirunsTask
        """

        self._task = task

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
        if not isinstance(other, InlineResponseDefault10):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
