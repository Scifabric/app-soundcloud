PyBossa demo project SoundCloud
===================================

This project shows how you can do sound pattern recognition. You can use sound
clips from SoundCloud using the [SoundCloud API](http://developers.soundcloud.com/)
or, alternatively, use some sound clips hosted somewhere else (like on Dropbox).

![alt screenshot](http://i.imgur.com/ZkNSfnE.png)

The project has five main files:

* **project.json**: a JSON file that describes the project.
* **long_description.md**: a Markdown file with a long description of the
  project.
* **get_sounds.py**: to query SoundCloud and write a file with the sound links.
* **template.html**: the task presenter where the user/volunteer will do the sound
  pattern recognition.
* **tutorial.html**: a simple tutorial that explains how to do the sound pattern
  recognition.


Testing the project
===================

You need to install the pybossa-pbs and the SoundCloud client libraries. Use of
a virtual environment is recommended:

```bash
    $ virtualenv env
    $ source env/bin/activate
```

```bash
    $ pip install -r requirements.txt
```

If you are going to use the SoundCloud API to get the sound clips, you will need
a SoundCloud Client ID, so if you don't have one, you need to create it.
Go to [https://developers.soundcloud.com](https://developers.soundcloud.com) and follow the instructions.
Once you have the Client ID, copy the file **config.py.tmpl** to **config.py**
and fill in the contents with your Client ID token. Then, you can follow the next steps.


## Creating an account in a PyBossa server
Now that you've all the requirements installed in your system, you need
a PyBossa account:

*  Create an account in your PyBossa server (use [Crowdcrafting](http://crowdcrafting.org) if you want).
*  Copy your API-KEY (you can find it in your profile page).

## Configure pybossa-pbs command line

PyBossa-pbs command line tool can be configured with a config file in order to
avoid typing the API-KEY and the server every time you want to take an action
on your project. For this reason, we recommend you to actually create the
config file. For creating the file, follow the next steps:

```bash
    $ cd ~
    $ editorofyourchoice .pybossa.cfg
```

That will create a file. Now paste the following:

```ini
[default]
server: http://yourpybossaserver.com
apikey: yourapikey
``` 

Save the file, and you are done! From now on, pybossa-pbs will always use the
default section to run your commands.

## Create the project

Now that we've everything in place, creating the project is as simple as
running this command:

```bash
    $ pbs create_project
```

## Adding some tasks

Now we can add some tasks. The project comes with two samples that you can use:

 * soundcloud_tasks.csv: a CSV file with some tasks
 * get_sounds.py: a script that will contact SoundCloud to create a JSON file with
   the information to show the SoundCloud clips.

### Using a CSV file for adding tasks

This is very simple too, thanks to pbs:

```bash
    $ pbs add_tasks --tasks-file soundcloud_tasks.csv
```
You'll get a progress bar with the tasks being uploaded. Now your project has
some tasks in the server to be processed by the volunteers.

### Using a JSON file for adding tasks

Instead of giving you a JSON file, we wanted to show you how you can use a web
service like SoundCloud to query it and get the sound clips.
For this reason, we've created the script **get_sounds.py**.

When you run this script, it will contact SoundCloud, get up to 10 songs from your
account in the web services, get its links, and write a file in JSON format
named: **soundcloud_tasks.json**. We'll use this file to add some extra tasks to
our project:

```bash
    $ python get_sounds.py
    $ pbs add_tasks --tasks-file soundcloud_tasks.json
```

Again, as before, you will see a progress bar as the tasks are being added to
your project. You can modify get_sounds.py to adapt it for your needs ;-)

**NOTE**: This template project allows you to use other sources different from
SoundCloud to get the sound clips. For example, you can use mp3 files hosted on
Dropbox or any other service. In case you want to use them, just make sure that
your .csv or .json files with the tasks include an attribute called "audio_url"
instead of the "embed" that you will find for SoundCloud audio clips, and make
sure you include the link to the raw mp3 audio file (other formats supported by
the HTML5 <audio> tag are also supported).

## Finally, add the task presenter, tutorial and long description

Now that we've some data to process, let's add to our project the required
templates to show a better description of our project, to present the tasks to
our users, and a small tutorial for the volunteers:

```bash
    $ pbs update_project
```

Done! Now you can do sound pattern recognition problems in the PyBossa server.

**NOTE**: we provide templates also for Bootstrap v2 in case your PyBossa
server is using Bootstrap 2 instead of Bootstrap 3. See the rest of the files.


Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This project uses the [pybossa-pbs](https://pypi.python.org/pypi/pybossa-pbs) library in order to simplify the development of the project and its usage. Check the [documentation](https://github.com/PyBossa/pbs).


LICENSE
=======

Please, see the COPYING file.


Acknowledgments
===============
The thumbnail has been created using a [photo](http://www.flickr.com/photos/32985084@N00/2708708829) from Daniel Lombraña González (license CC BY-SA 2.0). 


