import unittest
import os
import json
import string 
import random
from .constants.TestPayload import *
from .constants.TestEnvironment import *


from app import app

CURRENT_DIRECTORY = os.path.dirname(__file__)




class GraphCompareTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_invalid_input_provided(self):

        payload = dict(graphs="", dataset="RELIABLE")

        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type = 'multipart/form-data',
            headers=headers,
            data=payload
        )

        self.assertEqual(400, response.status_code)
        self.assertEqual('error' in STRING_OUTPUT_INVALID_INPUT, 'error' in response.json)

    def test_invalid_dataset_provided(self):

        letters = string.ascii_lowercase
        dataset_name = ''.join(random.choice(letters) for i in range(10))
        payload = dict(graphs=STRING_INPUT, dataset=dataset_name)

        print(dataset_name)
        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type = 'multipart/form-data',
            headers=headers,
            data=payload
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(STRING_OUTPUT_ALL, response.json)
    
    def test_successful_graph_compare_alldataset(self):


        payload = dict(graphs=STRING_INPUT, dataset="ALL")

        
        headers={}

        response = self.app.post(
            STRING_URL,
            content_type = 'multipart/form-data',
            headers=headers,
            data=payload
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(STRING_OUTPUT_ALL, response.json)

    def test_successful_graph_compare_reliabledataset(self):

        payload = dict(graphs=STRING_INPUT, dataset="RELIABLE")

        
        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type = 'multipart/form-data',
            headers=headers,
            data=payload
        )
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(STRING_OUTPUT_RELIABLE, response.json)
