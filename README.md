# Simple-REST-Project
Simple REST Project in Django. Contains basic User Authentization and Order system of Products.

### To pull from DockerHub run this command:
docker pull equiv/deepsee_project:latest

### Run the image.
docker run --name deepsee_project -d -p 8000:8000 equiv/deepsee_project:latest

### To create an order and list all of them go to:
http://127.0.0.1:8000/api/order/

### To inspect and edit order click "url":"hyperlink" or go to:
http://127.0.0.1:8000/api/order/id/ where id is order's id

### To create a product and list all of them go to:
http://127.0.0.1:8000/api/product/

### To inspect and edit product click "url":"hyperlink" or go to:
http://127.0.0.1:8000/api/product /id/ where id is product's id

### To perform simple unit test enter these commands in /usr/src/app #  Docker directory:
cd deepsee_project/
python manage.py test api.product.tests
