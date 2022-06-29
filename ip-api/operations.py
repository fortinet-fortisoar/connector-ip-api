""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import get_logger, ConnectorError
import json
import requests

logger = get_logger('ip-api')


class IPAPI(object):

    def __init__(self, config):
        self.url = config.get('server').strip()
        if not self.url.startswith('http://'):
            self.url = 'http://' + self.url
        if self.url[-1] == '/':
            self.url = self.url[:-1]
        self.headers = {'accept': 'application/json'}

    def make_rest_call(self, endpoint, method='POST', data=None, headers=None):
        url = self.url + endpoint
        logger.info('Final url to make rest call is: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        if data:
            logger.info('Converting the data: {0} into an equivalent JSON object.'.format(data))
            data = json.dumps(data)
            logger.info('After converting into a JSON object: {0}'.format(data))
        try:
            logger.info('Making a request with {0} method, {1} data and {2} as headers.'.format(method, data, self.headers))
            response = requests.request(method, url, data=data, headers=self.headers)
            if response.status_code in [200]:
                try:
                    logger.info('Converting the response into JSON format after returning with status code: {0}'.format(
                        response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response.content})
        except Exception as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))

    def execute_batch_api(self, params):
        endpoint = '/batch'
        return self.make_rest_call(endpoint=endpoint, data=params.get('list_of_ip_addr'))


def _run_operation(config, params):
    operation = params['operation']
    ipapi_obj = IPAPI(config)
    command = getattr(IPAPI, operation)
    response = command(ipapi_obj, params)
    return response


def _check_health(config):
    try:
        endpoint = 'http://edns.ip-api.com/json'
        response = requests.request('GET', endpoint)
        if response.status_code != 200:
            logger.exception('Configuration Error, Check URL.')
            raise ConnectorError('Configuration Error, Check URL.')
    except Exception as e:
        logger.exception('Health Check Error:{0}'.format(e))
        raise ConnectorError('Health Check Error:{0}'.format(e))
