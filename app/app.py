from flask import Flask, request, jsonify, render_template
from typing import List, Dict
from pydantic import ValidationError
from color_clustering import cluster_colors
from pydantic import BaseModel, Field
from typing import List, Dict

class ColorRequestModel(BaseModel):
    colors: List[str] = Field(..., min_items=1)
    categories: Dict[str, str] = Field(...)
    threshold: float = Field(..., ge=0, le=1)

app = Flask(__name__)

@app.route('/cluster', methods=['POST'])
def cluster_endpoint():
    try:
        data = ColorRequestModel(**request.get_json())
    
        colors = data.colors
        categories = data.categories
        threshold = data.threshold

        # Ensure there are more colors than categories
        if len(colors) < len(categories):
            return jsonify({
                'status': 'error',
                'message': 'Not enough colors to cluster. There must be more colors than categories.'
            }), 400 

        clustered_colors = cluster_colors(colors, categories, threshold)
    
        return jsonify(clustered_colors)

    except ValidationError as e:
        return jsonify({
            'status': 'error',
            'message': 'Invalid data provided.',
            'details': e.errors()
        }), 400

@app.route('/', methods=['GET'])
def display_html():
    return render_template('preview.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)