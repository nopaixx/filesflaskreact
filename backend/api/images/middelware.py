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
    try:
        image = Images.query.filter_by(name=named).first()
        if image:
            return {'image': image.serialize()}
        else:
            return 'NOT_FOUND', 404
    except Exception as e:
        print(str(e), file=sys.stderr)



def set_image(request):
    
    valid_request(request)

    file = request.files['file']
    name = request.form.get('name')

    filename = get_secure_name(file.filename, name)
    
    # first() is equivalent to limit and only once with this name
    # first we save the image if something faile we don't update the date base
    file.save(os.path.join(app.config['STATIC_FOLDER'], filename))

    path = "{}/{}/{}".format(app.config['SERVER_NAME_URI'], 
                             app.config['STATIC_PATH'],
                             filename)

    image = Images.query.filter_by(name=name).first()

    if image:
        Images.update(image, path, name)
        STATUS = 'UPDATED'
    else:
        image = Images.create(path, name)
        STATUS = 'CREATED'

    return {'image': image.serialize(),
            'status': STATUS}, 201


def get_secure_name(filename, name):
    filename = filename.split('.')
    filename = '{}-{}-{}.{}'.format("".join(item for item in filename[:-1]), 
                                    name,
                                    datetime.utcnow().timestamp(),
                                    filename[-1])
    return secure_filename(filename)


def valid_request(request):
    
    if app.config['VIRUS_SCAN']:
        if not virus_scan(request):
            raise RuntimeError('virus detected!')
        
    if not valid_name(request):
        raise RuntimeError('invalid name')

    if not valid_file(request):
        raise RuntimeError('invalid file')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def virus_scan(request):
    # TODO 3-party app to check for virus in binary file
    pass

def valid_name(request):
    # TODO add you validation for the name, for example
    # length>0 <80 
    # escape caracters etc...

    return True

def valid_file(request):

    if 'file' not in request.files:
        return False

    file = request.files['file']

    if file.filename == '':
        return False

    if not allowed_file(file.filename):
        return False

    return True
