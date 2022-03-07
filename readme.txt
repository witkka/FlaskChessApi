=========================================================================
Flask api, version '1.0.0', March, 2022.
This is README.txt,  user guide.
Author: Katarzyna Witkowska, https://github.com/witkka
=========================================================================

This package contains flask api and test data.

To install the package:
> pip install -e .

To chose app:
> $env:FLASK_APP = "flaskr"

To change environmental variables to development:
> $env:FLASK_ENV = "development"

To change environmental variables to production:
> $env:FLASK_ENV = "production"

To run application:
> flask run

To run tests:
> pytest tests/

-------------------------------------------------------------------------

API
To find list of valid moves:
'/api/v1/{chess-figure}/{current-field}'

Example of query with correct input data:
query: '/api/v1/rook/h2'
message:    {
               "availableMoves":[
                  "H3"
               ],
               "error": null,
               "figure":"rook",
               "currentField":"H2"
            }

query: '/api/v1/rook/h23'
message:    {
               "availableMoves":[],
               "error": "Field does not exist.",
               "figure":"rook",
               "currentField":"H23"
            }

To check if move to dest_field is possible for given figure from current_field:
'/api/v1/{chess-figure}/{current-field}/{dest-field}'
Example of query with correct input data:
query: '/api/v1/rook/h2/h3'
message:    {
       "move":"valid",
       "figure":"rook",
       "error": null,
       "currentField":"H2",
       "destField":"H3"
    }

query: '/api/v1/rook/h2/h23'
message:    {
       "move":"invalid",
       "figure":"rook",
       "error": null,
       "currentField":"H2",
       "destField":"H23"
    }

 If figure name is incorrect, api returns response_code 409.
 If field name is incorrect, api returns response_code 404.
 If all data is correct and there is no server error, api returns status_code 200.



