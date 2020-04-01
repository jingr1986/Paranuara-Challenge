# Instructions

### Steps to install
* Run ```git clone https://github.com/jingr1986/Paranuara-Challenge.git```
* Run ```cd Paranuara-Challenge```
* Run ```source setup.sh```
* Run ```python manage.py makemigrations```
* Run ```python manage.py migrate```
* Run ```python manage.py pre_load``` to load the provided resource files
* Run ```python manage.py runserver``` to run the server on 8000 port, consider changing if the port is already occupied

### Resources
Provided resource files are kept in ```app/resources/``` folder,
In case you want to modify the resource data, consider replacing the files ```app/resource/people.json``` or ```app/resource/companies.json```
After that, run ```python manage.py pre_load```
This should reload the data again.
> Note: file names are strict and thus should be kept the same.

### Endpoints
BASE_URL = ```http://localhost:8000```
> Note: Base URL would be different in case one changes the port intentionally
- Endpoint 1
    - **Endpoint**: Given a company index return all of its employees
    - **URL**: ```<BASE_URL>/company/company_id>/employees/```
    - URL Args:
        - company_id: Refers to index + 1 from companies.json resource file
- Endpoint 2
    - **Endpoint**: Return all the mutual alive brown eyes friends from given 2 individuals
    - **URL**: ```<BASE_URL>/mutual/<pk1>/<pk2>/```
    - URL Args:
        - pk1: first person's id
        - pk2: second person's id 
- Endpoint 3
    - **Endpoint**: Provide details about individual's favourite food
    - **URL**: ```<BASE_URL>/people/<pk1>/favourite_foods/```
    - URL Args:
        - pk1: person's id
- Endpoint 4
    - **Endpoint**: Allow a company to add new employee if it does not have one
    - **URL**: ```<BASE_URL>/company/<company_id>/add_employee/```
    - URL Args:
        - company_id: Refers to index + 1 from companies.json resource file


### Test cases
Run ```python manage.py test``` to run test cases
