import unittest
import os
import json
import string
import random
from .constants.TestPayload import *
from .constants.TestEnvironment import *


from app import app

CURRENT_DIRECTORY = os.path.dirname(__file__)

with open(os.path.join(CURRENT_DIRECTORY, "inputdata/SAMPLE_VERNAL_INPUT.json")) as f:
    VERNAL_INPUT = json.load(f)
f.close()


class GraphCompareTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_invalid_input_provided(self):
        '''
        Check if Vernal fails gracefully with no input
        '''
        payload = dict(graphs="", dataset="RELIABLE")

        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type='multipart/form-data',
            headers=headers,
            data=payload
        )

        with open(os.path.join(CURRENT_DIRECTORY, "responses/RESPONSE_ERROR_INVALID_GRAPH_INPUT.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(400, response.status_code)
        self.assertEqual('error' in expected_response,
                         'error' in response.json)

    def test_invalid_input_provided_object(self):
        '''
        Check if Vernal fails gracefully with invalid json input
        '''
        payload = dict(graphs={"nothinghere": "nothing"}, dataset="RELIABLE")

        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type='multipart/form-data',
            headers=headers,
            data=payload
        )

        with open(os.path.join(CURRENT_DIRECTORY, "responses/RESPONSE_ERROR_INVALID_GRAPH_INPUT.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(400, response.status_code)
        self.assertEqual('error' in expected_response,
                         'error' in response.json)

    def test_invalid_dataset_provided(self):  # fail
        '''
        Check if Vernal defaults to a usable dataset if an invalid dataset is provided
        '''
        with open(os.path.join(CURRENT_DIRECTORY, "inputdata/SAMPLE_VERNAL_INPUT.json")) as f:
            VERNAL_INPUT = json.load(f)
        f.close()

        letters = string.ascii_lowercase
        dataset_name = ''.join(random.choice(letters) for i in range(10))

        payload = dict(graphs=str(VERNAL_INPUT), dataset=dataset_name)

        print(dataset_name)
        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type='multipart/form-data',
            headers=headers,
            data=payload
        )

        with open(os.path.join(CURRENT_DIRECTORY, "responses/RESPONSE_STRING_ALL_DATASET.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, response.json)

    def test_successful_graph_compare_alldataset(self):  # fail
        '''
        Verify Vernal output given a valid input and the ALL dataset
        '''

        with open(os.path.join(CURRENT_DIRECTORY, "inputdata/SAMPLE_VERNAL_INPUT.json")) as f:
            VERNAL_INPUT = json.load(f)
        f.close()

        payload = dict(graphs=str(VERNAL_INPUT), dataset="ALL")

        print(payload)
        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type='multipart/form-data',
            headers=headers,
            data=payload
        )

        with open(os.path.join(CURRENT_DIRECTORY, "responses/RESPONSE_STRING_ALL_DATASET.json")) as f:
            expected_response = json.load(f)
        f.close()

        print(response.json)

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, response.json)

    def test_successful_graph_compare_reliabledataset(self):  # fail
        '''
        Verify Vernal output given a valid input and the RELIABLE dataset
        '''

        with open(os.path.join(CURRENT_DIRECTORY, "inputdata/SAMPLE_VERNAL_INPUT.json")) as f:
            VERNAL_INPUT = json.load(f)
        f.close()

        payload = dict(graphs=str(VERNAL_INPUT), dataset="RELIABLE")

        headers = {}

        response = self.app.post(
            STRING_URL,
            content_type='multipart/form-data',
            headers=headers,
            data=payload
        )

        with open(os.path.join(CURRENT_DIRECTORY, "responses/RESPONSE_STRING_RELIABLE_DATASET.json")) as f:
            expected_response = json.load(f)
        f.close()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, response.json)
