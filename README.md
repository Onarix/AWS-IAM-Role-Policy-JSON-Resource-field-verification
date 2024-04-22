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


## Built with

The method checking whole JSON file and validating resource field was built as an simple web app. 

[![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) - Backend <br> 
[![My Skills](https://skillicons.dev/icons?i=js)](https://skillicons.dev) - Frontend

## How to run?

### Webapp
To run webapp, create virtual environment and install modules from 'requirements.txt':
```
$ pip install -r requirements.txt
```

### Unit tests
Use this command to run unit tests:
```
$ pytest ./test_setup.py ./tests/tests.py
```


<!-- MARKDOWN LINKS & IMAGES -->
