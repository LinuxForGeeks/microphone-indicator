#!/usr/bin/python3

import configparser
import os
import datetime

class Settings:
    def __init__(self):
        print ("DEBUG: Initializing the Settings module @", (str(datetime.datetime.now())))

        cparse = configparser.ConfigParser()
        cparse.read([os.path.expanduser('~/.micindicator')])

        try:
            self._shownotifications = cparse.get('DEFAULT', 'show-notifications')

        except configparser.NoOptionError:
            print ("DEBUG: No configration file using default settings")
            self._shownotifications = '1'
            self.save()

        except ValueError:
            print ("DEBUG: Problem while reading setting file, using the default settings")
            os.system("rm ~/.micindicator")
            self._shownotifications = '1'
            self.save()

    ## Functions to get and set settings
    @property
    def show_notifications(self):
        #print ("DEBUG: getting show notifications settings @", (str(datetime.datetime.now())))
        if self._shownotifications == '1':
            return True
        else:
            return False

    @show_notifications.setter
    def show_notifications(self, data):
        #print ("DEBUG: setting show notifications settings @", (str(datetime.datetime.now())))
        if data == True:
            self._shownotifications = '1'
        else:
            self._shownotifications = '0'

    ## Function to save the settings
    def save(self):
        print ("DEBUG: saving settings file @", (str(datetime.datetime.now())))
        config = open(os.path.expanduser('~/.micindicator'), 'w')
        Text='''# Mic. Indicator Settings File
[DEFAULT]
# Should notifications be enabled
show-notifications = %s
''' % (self._shownotifications)
        config.write(Text)
        config.close()
