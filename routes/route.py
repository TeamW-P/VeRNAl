import pickle
import os
from flask import jsonify, abort, Blueprint, request
import sys
import os
import json
import ast
from core.tools import graph_compare 



routes = Blueprint('routes', __name__)
CURRENT_DIRECTORY = os.path.dirname(__file__)

@routes.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@routes.route('/compare-sequence/', methods=['POST'])
def vernal():

    try:
        # data is received enclosed in single quotes which json.load() does not like
        # we can instead use ast.literal_eval which is safer than eval - malicious concerns are not a problem here since data given here
        # is received only by internal pipelining and not by an external party
        representative_graphs = ast.literal_eval(request.form.get("graphs"))
        
        datasetName = request.form.get("dataset", type=str)
        if (datasetName.upper() == 'RELIABLE'):
            datasetName = 'RELIABLE'
        else:
            if (datasetName.upper() != 'ALL'):
                print("Invalid dataset provided, default to ALL dataset")
            datasetName = 'ALL'

        print("Executing VERNAL similarity functions with the ", datasetName.upper(), " dataset")
        moduleLibraryPath = os.path.join(CURRENT_DIRECTORY, "../core/tools/GraphData/")
        res = graph_compare.k_most_similar_bp2(moduleLibraryPath, representative_graphs, datasetName)
        return res
    except Exception as e:
        abort(400, "Vernal failed to process graph input: " + str(e))



