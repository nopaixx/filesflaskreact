import sys
import os

from flask_restful import Resource
from flask import request
from werkzeug.utils import secure_filename


from api.app import app
from api.images import Images
from api.images.middelware import get_all_images
from api.images.middelware import get_image
from api.images.middelware import set_image


class ImageIndex(Resource):

    def get(self):
        """
        Rest endpoint
        GET /images 

        :return: List of images in system
        """

        return get_all_images()

    
    def post(self):
        """
        POST /images
        recibe binary image

        :return: Return status and path
        """
        try:
            return set_image(request)
        except Exception as e:
            print(e, file=sys.stderr)
            return str(e), 404
        
        try:
            if 'file' not in request.files:
                print("No file", file=sys.stderr)

            file = request.files['file']

            if file.filename == '':
                print("print no name", file=sys.stderr)
            data = request.stream.read()
            dirname, filename = os.path.split(os.path.abspath(__file__))
            print(dirname, filename, file=sys.stderr)
            filename = secure_filename(file.filename)
            final = os.path.join(app.config['STATIC_FOLDER'], filename)
            print(final, file=sys.stderr)
#            file.save(os.path.join(app.config['STATIC_FOLDER'], filename))
        except Exception as e:
            print(e, file=sys.stderr)
        return set_image(request) 


class ImageItem(Resource):


    def get(self, named_image):
        """
        Rest endpoint

        GET /images/named_image

        :return: Return a image path and name
        """

        return get_image(named_image)

