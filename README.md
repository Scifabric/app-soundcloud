PyBossa demo application SoundCloud
===================================

This application shows how you can do sound pattern recognition using
[SoundCloud API](http://developers.soundcloud.com/). 

![alt screenshot](http://i.imgur.com/ZkNSfnE.png)

The application has three files:

*  createTasks.py: for creating the application in PyBossa, and fill it with some tasks.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: a simple tutorial for the volunteers.

Testing the application
=======================

You need to install the pybossa-client and the soundcloud client (use a virtualenv):

```bash
    $ pip install pybossa-client
    $ pip install soundcloud
```
Then, you can follow the next steps:

*  Create an account in PyBossa
*  Copy under your account profile your API-KEY
*  Run python createTasks.py -u http://crowdcrafting.org -k API-KEY
*  Open with your browser the Applications section and choose the SoundCloud app. This will open the presenter for this demo application.

Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This application uses the [pybossa-client](https://pypi.python.org/pypi/pybossa-client) in order to simplify the development of the application and its usage. Check the [documentation](http://pythonhosted.org/pybossa-client/).


LICENSE
=======

Please, see the COPYING file.


Acknowledgments
===============
The thumbnail has been created using a [photo](http://www.flickr.com/photos/32985084@N00/2708708829) from Daniel Lombraña González (license CC BY-SA 2.0). 


