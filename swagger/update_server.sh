set -x

cp default_controller.py \
   python-flask-server/swagger_server/controllers/

cp ../flask-server/system.py \
   python-flask-server/swagger_server/controllers/

cp ../flask-server/acme.py \
   python-flask-server/swagger_server/controllers/

set +x
