<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Onarix/AWS-IAM-Role-Policy-JSON-Resource-field-verification">
    <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AWS-IAM-Role-Policy-JSON-Resource-field-verification</h3>

  <p align="center">
    Assessment project for Remitly Poland company job recruitment stage
    <br />
    <a href="https://github.com/Onarix/AWS-IAM-Role-Policy-JSON-Resource-field-verification"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Onarix/AWS-IAM-Role-Policy-JSON-Resource-field-verification">View Demo</a>
    ·
    <a href="https://github.com/Onarix/AWS-IAM-Role-Policy-JSON-Resource-field-verification/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Onarix/AWS-IAM-Role-Policy-JSON-Resource-field-verification/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>


## Overview

The <b>*AWS-IAM-Role-Policy-JSON-Resource-field-verification project*</b> is a utility for validating the entire Role Policy JSON File from Amazon AWS and most certainly - checking the resources statuses in document statements.

Method 'resource_verify()' returns logical <b>FALSE</b>, if the resource value contains a single asterisk (*) and <b>TRUE</b> if otherwise.

```python
def resource_verify(self) -> list:
    status = []
    for statement in self.policy.content["PolicyDocument"]["Statement"]:
        if statement["Resource"] == "*":
            status.append(False)
        else:
            status.append(True)
    return status
```

## Built with

The method checking whole JSON file and validating resource field was built as a simple web app. 

[![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) - Backend Flask service, containing dedicated class for Role Policy JSON file, validating it and checking the 'resources' status <br> 
[![My Skills](https://skillicons.dev/icons?i=js)](https://skillicons.dev) - Simple Frontend service, that helps to visualize the process of Role Policy data validation.

## How to run?

### Prerequisites
First of all, you have to clone the project to use the app:
```
$ git clone https://github.com/Onarix/AWS-IAM-Role-Policy-JSON-Resource-field-verification.git
```
You need Python installed in your computer to run the project.
To prepare webapp, install modules from 'requirements.txt':
```
$ pip install -r requirements.txt
```

### Webapp
To use webapp, run the <b>'API.py'</b> script file:
```
$ python API.py
```
After the Flask server start, you can access the webapp, by running the <b>'index.html'</b> file in your web browser.


### Unit tests
Use this command from project main catalog to run unit tests:
```
$ pytest ./test_setup.py ./tests/tests.py
```
