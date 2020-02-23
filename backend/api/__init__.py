import os

from flask import Flask, send_from_directory
from flask_restful import Resource, Api


from api.app import app
from api.app import api

# our rest endpoints
from api.images.endpoint import ImageIndex
from api.images.endpoint import ImageItem

api.add_resource(ImageIndex, '/images')
api.add_resource(ImageItem, '/images/<named_image>')

# server our satic files
@app.route('/static/<filename>')
def files(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)


if __name__ == '__main__':
    # added our resource path or the rest model
    app.run()
