import pickle
import os
from flask import jsonify, abort, Blueprint
import sys
import os
from core.tools import graph_compare 



routes = Blueprint('routes', __name__)
CURRENT_DIRECTORY = os.path.dirname(__file__)

@routes.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@routes.route('/test', methods=['GET'])
def vernal():
    print("Executing VERNAL similarity functions")
    moduleLibraryPath = os.path.join(CURRENT_DIRECTORY, "../core/tools/GraphData/3dMotifAtlas_ALL_one_of_each_graph.cPickle")
    tempResponsePath = os.path.join(CURRENT_DIRECTORY, "../core/tools/GraphData/response.json") #BP2 output
    
    return jsonify(graph_compare.k_most_similar_bp2(moduleLibraryPath, tempResponsePath))


