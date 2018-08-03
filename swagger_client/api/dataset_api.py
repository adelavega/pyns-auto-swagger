# coding: utf-8

"""
    neuroscout

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DatasetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_datasets_dataset_id_get(self, dataset_id, **kwargs):  # noqa: E501
        """Get dataset by id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_datasets_dataset_id_get(dataset_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dataset_id: (required)
        :return: InlineResponseDefault6
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_datasets_dataset_id_get_with_http_info(dataset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_datasets_dataset_id_get_with_http_info(dataset_id, **kwargs)  # noqa: E501
            return data

    def api_datasets_dataset_id_get_with_http_info(self, dataset_id, **kwargs):  # noqa: E501
        """Get dataset by id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_datasets_dataset_id_get_with_http_info(dataset_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dataset_id: (required)
        :return: InlineResponseDefault6
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_datasets_dataset_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if ('dataset_id' not in params or
                params['dataset_id'] is None):
            raise ValueError("Missing the required parameter `dataset_id` when calling `api_datasets_dataset_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['dataset_id'] = params['dataset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/datasets/{dataset_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault6',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_datasets_get(self, **kwargs):  # noqa: E501
        """Returns list of datasets.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_datasets_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[InlineResponseDefault5]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_datasets_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_datasets_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_datasets_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns list of datasets.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_datasets_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[InlineResponseDefault5]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_datasets_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponseDefault5]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
