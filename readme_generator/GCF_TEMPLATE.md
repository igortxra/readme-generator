# $SERVICE
$SHORT_DESCRIPTION

## What it does
$WHAT_IT_DOES

## Structure
```
# Can be a little different*
.
├── $FUNCTION_NAME          # Serverless Function folder (What is inside is deployed)
|  └── main.py              # Serverless Function file
|  └── main_test.py         # Tests are located here
|  └── requirements.txt     # Serverless functions dependecies 
|  └── pkg/                 # local dependecies, internal modules
├── requirements-dev.txt    # Development/test dependencies
├── ...
```


## How to run (locally)
```bash
pip install -r requirementes-dev.txt
pip install -r $FUNCTION_NAME/requirements.txt
cd $FUNCTION_NAME
functions-framework --target=$FUNCTION_NAME --debug
```


## How to test (locally)
```bash
coverage run -m pytest -v   # Run tests tracking coverage
coverage report             # See report in terminal 
coverage html               # Create a report in html
```


## Environment variables
- **VAR** - Explanation


## Triggering
Method: `$HTTP_METHOD`

### Expected parameters:
#### Header
- **key** - Explanation

#### Query String
- **key** - Explanation

#### JSON
```json
// Put a json here
```

### Successfull response
```json
// Put a json here
```
