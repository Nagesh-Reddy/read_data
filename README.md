# This is an Flask backend app for reading, flattening and editing static json data and display using HTML and CSS
To run the application follow below steps
1) Install Python
2) Create a virtual env - Python -m venv <virtual_Name>
3) Install Flask - pip install flask
4) Activate virtual_env -
   Win - .\<virtual_Name>\Scripts\activate
   Linux - ./<virtual_Name>/bin/activate
5) Run unit_test.py from terminal/console to check all test cases working fine or not
6) Alternatively you can directly run normalized_data.py and then check below URLs from browser
  - http://127.0.0.1:5000/api/all?page=3
  - http://127.0.0.1:5000/api/song?title=3AM
  - Also, you can chenge the rating from last column under /api/all records page, it is an pagination tabular format displays 10 records at a time
