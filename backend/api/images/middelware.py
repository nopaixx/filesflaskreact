import json
import os
import sys
from werkzeug.utils import secure_filename
from sqlalchemy import desc
from datetime import datetime

from api.app import app
from api.images import Images


def get_all_images():
    query_images = Images.query.order_by(desc(Images.id)).all()
    images = [element.serialize() for element in query_images]
    return {'images': images}, 200


def get_image(named):
    image = Images.query.filter_by(name=named).first()
    if image:
        return {'image': image.serialize()}, 200
    else:
        return {'image': {
                        'path': app.config['NOT_FOUND_IMAGE'],
                        'name': 'NOT_FOUND'
                         }
               }, 404


def set_image(request):
    
    valid_request(request)

    file = request.files['file']
    name = request.form.get('name')

    filename = get_secure_name(file.filename, name)
    
    save_file(file, filename)

    path = generate_path(filename)
    
    image = Images.query.filter_by(name=name).first()

    if image:
        Images.update(image, path, name)
        STATUS = 'UPDATED'
    else:
        image = Images.create(path, name)
        STATUS = 'CREATED'

    return {'image': image.serialize(),
            'status': STATUS}, 201

# util function


def save_file(file, filename):
    """
    Recibe a binary file and name and save into static folder

    :file: binary File
    :filaname: destination name

    :return: return true if succesfull false otherwise

    TODO: improve system write ok etc... raise excpetion..
    """
    file.save(os.path.join(app.config['STATIC_FOLDER'], filename))
    return True


def generate_path(filename):
    """
    Given a input filename we return a path with the static server URL

    :filename: File name destination

    :return: return a full url

    """

    path = "{}/{}/{}".format(app.config['SERVER_NAME_URI'],
                             app.config['STATIC_PATH'],
                             filename)
    return path

def get_secure_name(filename, name):
    """
    With this function we are sure we not override other file
    and we sanitize the input

    :filename: original filename destination
    :name: this is the frontend taged name

    :return: sanitized name with timestamp

    """
    filename = filename.split('.')
    filename = '{}-{}-{}.{}'.format("".join(item for item in filename[:-1]), 
                                    name,
                                    datetime.utcnow().timestamp(),
                                    filename[-1])
    return secure_filename(filename)


def valid_request(request):
    """
    this function validate our request with mandatory fields

    """
    if app.config['VIRUS_SCAN']:
        if not virus_scan(request):
            raise RuntimeError('virus detected!')
        
    if not valid_name(request):
        raise RuntimeError('invalid name')

    if not valid_file(request):
        raise RuntimeError('invalid file')


def allowed_file(filename):
    """
    Allowed extension

    :return: True if allowed filename
    """

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def valid_file(request):
    """
    For the request we need a file we check if is valid
    """
    if 'file' not in request.files:
        return False

    file = request.files['file']

    if file.filename == '':
        return False

    if not allowed_file(file.filename):
        return False

    return True


def virus_scan(request):
    # TODO 3-party app to check for virus in binary file
    pass

def valid_name(request):
    # TODO add you validation for the name, for example
    # length>0 <80
    # escape caracters etc...

    return True


