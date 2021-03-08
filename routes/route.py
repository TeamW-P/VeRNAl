import pickle
import os
from flask import jsonify, abort, Blueprint
import sys
import os
import json
from core.tools import graph_compare 



routes = Blueprint('routes', __name__)
CURRENT_DIRECTORY = os.path.dirname(__file__)

@routes.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@routes.route('/CompareSequence/<dataset>', methods=['POST'])
def vernal(dataset):

    bp_output = "" 
    try: 
        bp_output = eval(request.form.get("graphs"))
    except Exception as e:
        abort(400, "Vernal failed to process graph input: " + str(e))
    print("Executing VERNAL similarity functions with the ", dataset.upper(), " dataset")
    moduleLibraryPath = os.path.join(CURRENT_DIRECTORY, "../core/tools/GraphData/")
    #tempResponsePath = os.path.join(CURRENT_DIRECTORY, "../core/tools/GraphData/response.json") #BP2 output
    return jsonify(graph_compare.k_most_similar_bp2(moduleLibraryPath, bp_output, dataset=dataset))


