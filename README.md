[![Build Status](https://travis-ci.org/Rhytah/iReporter.svg?branch=API-Version2)](https://travis-ci.org/Rhytah/iReporter) [![Coverage Status](https://coveralls.io/repos/github/Rhytah/iReporter/badge.svg?branch=API-Version2)](https://coveralls.io/github/Rhytah/iReporter?branch=API-Version2) [![Maintainability](https://api.codeclimate.com/v1/badges/e28b889db9f04910afe6/maintainability)](https://codeclimate.com/github/Rhytah/iReporter/maintainability)

# iReporter

**Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter.
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention**

## Features(UI).
* user signup.
* user login.
* users can create red-flag record.
* Users can create an intervention record.
* Users can view all red-flag and intervention records.
* Users can delete a red-flag or intervention record.
* Admin has the privilege of changing status of a record.
* Admin can view all records from different users.
 

## Getting Started
clone the github repo to your computer:
* $git clone https://github.com/Rhytah/iReporter.git
* Extract the zip file to another file
* Open using text editor
* Run it using web browser 

### Prerequisites

* Text editor where we write our project files. (VScode)
* Web browser (Mozilla, Chrome) to preview project files

## Technologies Used
* HTML.
* CSS.
* JAVASCRIPT.

### Usage
* launch <a href="https://rhytah.github.io/iReporter/UI/index.htm">Index</a>  to access Sign Up/ Sign In options
* On successful login, you will be redirected to webpage that contains information relevant to your logged in account(either user or Admin).
* <a href="https://rhytah.github.io/iReporter/UI/forum.htm">User interface</a> ;
        ** click `create red-flag` tab to display input fields.
        ** click `create intervention record` tab to display input fields.
        ** click `My records` tab to display past records.
        ** click `Logout` tab to leave page.
        ** top right corner contains brief user profile information.
* <a href="https://rhytah.github.io/iReporter/UI/admin.htm">Admin interface</a> ;
       ** click on status to display options to change status of a record


## Known Bugs
The App does not have a database and doesn't save data entered in it.

## GH-Pages.
my site is published at https://rhytah.github.io/iReporter/UI/index.htm

```
# API 

```

## Tools

* Text editor where we write our project files. (VScode)
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library
* Postman -Application to test and consume endpoints
* PEP8 - Style guide



# Create virtual environment and activate it

```
$pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate

```
 **Install all the necessary tools by**
 ```
 $pip insatll -r requirements.txt
 ```
## Start app server in console/terminal/commandprompt

```
$python app.py
```
## Test app in terminal

```
$pytest
```
## Versioning
```
This is version one"v1" of the API
```
## End Points(Required Features)
|           End Point                                     |            Functionality                       |
|   ---------------------------------------------------   | ---------------------------------------------  |
|     POST   api/v1/auth/login/                           |             Login to application               |
|     POST   api/v1/auth/signup/                          |             Register an account                |
|     POST   api/v1/red-flags/                            |             Create a red-flag                  |
|     GET    api/v1/red-flags/                            |             Fetch all red-flags                |
|     GET    api/v1/red-flags/<int:redflag_Id>            |             Fetch a red-flag                   |
|     PATCH  api/v1/red-flags/<int:redflag_Id>            |             Edit red-flag location             |
|     PATCH  api/v1/red-flags/<int:redflag_Id>            |             Edit red-flag comment              |
