import numpy as np
from typing import Dict, List
from sklearn.cluster import KMeans
from utils import hex_to_rgb, rgb_to_hex, cosine_similarity

def cluster_colors(colors: List[str], categories: Dict[str, str], threshold: float) -> Dict[str, List[str]]:
    color_data = np.array([hex_to_rgb(color) for color in colors])
    category_data = np.array([hex_to_rgb(color) for color in categories.values()])

    kmeans = KMeans(n_clusters=len(categories), init=category_data, n_init=1)
    kmeans.fit(color_data)
    
    clustered_colors = {category: [] for category in categories.keys()}
    
    for color, label in zip(colors, kmeans.labels_):
        category_name = list(categories.keys())[label]
        category_color = categories[category_name]
        similarity = cosine_similarity(hex_to_rgb(color), hex_to_rgb(category_color))
        
        if similarity >= threshold:
            clustered_colors[category_name].append(color)
    
    return clustered_colors