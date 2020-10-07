## Project Problem Statement

To complete this module, you'll write a script that interacts with a running web service.  The web service is part of
your company's website and is in charge of storing and displaying the customer reviews of the company.

The reviews are stored in text files in the local disk. Your script should open those files, process the information
to turn it into the format expected by the web service, then send it to the web service to get stored.

For this lab, the service is running on the same machine, and you can actually look at how all of it is implemented,
if you want.  But you don't need to change the service implementation to complete the exercise.

Remember that you can take your time to prepare the code that you’ll write. You can start the lab later on, once you
have a good idea of what you'll do and how you'll do it.

Also, feel free to check out the resources that we pointed to as many times as you need.

### Introduction

You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of
customer reviews. Your manager asks you to take those reviews (saved as .txt files) and display them on your company's
website. To do this, you'll need to write a script to convert those .txt files and process them into Python
dictionaries, then upload the data onto your company's website (currently using Django).

### What you'll do

* Use the Python OS module to process a directory of text files

* Manage information stored in Python dictionaries

* Use the Python requests module to upload content to a running Web service

* Understand basic operations for Python requests like GET and POST methods
