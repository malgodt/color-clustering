# Color Clustering using K-Means Endpoint

This is a simple Python microservice for color clustering using the K-Means algorithm. It is built using the Flask framework and is designed to be run using Docker.

The endpoint accepts a list of colors in hexadecimal format along with a dictionary of predefined categories and a threshold value. It then groups the provided colors into respective categories based on the minimum Euclidean distance and returns the clustered colors as a JSON response.

## Requirements

-   Python 3.6+
-   Flask
-   K-Means Implementation
-   Docker

## Endpoint

**URL**: `/cluster`

**Method**: `POST`

**Input Request (JSON)**:

```json
{
    "colors": ["#fafafa", "#d11d05", "#663399", "#dedede", "#D3C0D3"],
    "categories": {
        "white": "#ffffff",
        "purple": "#7670B3",
        "neutral": "#BFBFBF",
        "red": "#AA2B31"
    },
    "threshold": 0.9
}
```

**Output Response (JSON)**:

```json
{
    "neutral": ["#dedede", "#D3C0D3"],
    "purple": ["#663399"],
    "red": ["#d11d05"],
    "white": ["#fafafa"]
}
```

## Setup and Deployment

1. Clone or download this repository.
2. Build the Docker image by running:

```sh
docker build -t color-clustering .
```

3. Run the Docker container:

```sh
docker run -p 8080:8080 color-clustering
```

4. Send a POST request to `http://localhost:8080/cluster` with the JSON payload as described above.

## Example Usage

You can use this microservice to cluster colors for various purposes, such as grouping similar colors in a design application or categorizing colors for data visualization.

For more details concerning the implementation, please refer to the source code provided.
