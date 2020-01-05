Home project to monitor energy usage and production
==============================================

This project leverages AWS greengrass from a raspberry PI to poll data from my smart meter and solar inverter.

The smart meter polled using a serial cable on the P1 port, this meter is logging according to the dutch DMSR 4.2 spec.
The solar inverter is polled over modbus TCP using the SunSpec standard. The inverter at my home is from PowerOne / ABB.

What's Here
-----------

This project includes:

* README.md - this file
* buildspec.yml - this file is used by AWS CodeBuild to package this
  application for deployment to AWS Lambda
* energy_main.py - This is the main lambda polling data every x seconds on pushing data on a MQTT topic.
* template.yml - this file contains the AWS Serverless Application Model (AWS SAM) used
  by AWS CloudFormation to deploy this application to AWS
* tests/ - this directory contains unit tests for this application
* template-configuration.json - this file contains the project ARN with placeholders used for tagging resources with the project ID
* dsmr4_reader.py - the reader logic for the smart DSMR4 meter
* sunspec_modbus_tcp_reader - the reader logic for the inverter over modbus TCP
* /sunspec - containg sunspec python package and models (not available in PyPi hence packaged here) - https://github.com/sunspec/pysunspec / https://github.com/sunspec/models

TODO
------------------
WIP
