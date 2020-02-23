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


# GET /images --> lista de images
# POST /images --> sube la image
# GET /image/name --> devuelve una image

class ImageIndex(Resource):

    def get(self):
        """
        Rest endpoint
        GET /images 

        :return: List of images in system
        """
        try:
            return get_all_images()
        except Exception as e:
            print(e, file=sys.stderr)
            return str(e), 404


    
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
        

class ImageItem(Resource):


    def get(self, named_image):
        """
        Rest endpoint

        GET /images/named_image

        :return: Return a image path and name
        """
        try:
            return get_image(named_image)
        except Exception as e:
            print(e, file=sys.stderr)
            return str(e), 404

