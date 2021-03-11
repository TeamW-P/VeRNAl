import pickle
import os
from flask import jsonify, abort, Blueprint, request
import sys
import os
import json
from core.tools import graph_compare 



routes = Blueprint('routes', __name__)
CURRENT_DIRECTORY = os.path.dirname(__file__)

@routes.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@routes.route('/CompareSequence/', methods=['POST'])
def vernal():

    try: 
        bp_output = request.form.get("graphs")
        bp2ProcessedData = json.loads(bp_output)
        
        datasetName = request.form.get("dataset", type=str)
        print("Executing VERNAL similarity functions with the ", datasetName.upper(), " dataset")
        moduleLibraryPath = os.path.join(CURRENT_DIRECTORY, "../core/tools/GraphData/")
        res = str(graph_compare.k_most_similar_bp2(moduleLibraryPath, bp2ProcessedData, datasetName))
    except Exception as e:
        abort(400, "Vernal failed to process graph input: " + str(e))



