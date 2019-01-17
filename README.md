[![Build Status](https://travis-ci.com/Rhytah/iReporter.svg?branch=API)](https://travis-ci.com/Rhytah/iReporter) [![Coverage Status](https://coveralls.io/repos/github/Rhytah/iReporter/badge.svg?branch=API)](https://coveralls.io/github/Rhytah/iReporter?branch=API) [![Maintainability](https://api.codeclimate.com/v1/badges/e28b889db9f04910afe6/maintainability)](https://codeclimate.com/github/Rhytah/iReporter/maintainability)

# iReporter

**Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter.
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention**

## Tools

* Text editor where we write our project files. (VScode)
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library
* Postman -Application to test and consume endpoints
* PEP8 - Style guide

**Getting Started**
clone the github repo to your computer:

* $git clone `https://github.com/Rhytah/iReporter.git`

* Extract the zip file to another file

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

## Author
* [Rhytah] `https://github.com/Rhytah`
