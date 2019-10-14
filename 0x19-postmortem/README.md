# Postmortem

This text documents an outage migrating a website to Wordpress.

[!(https://qph.fs.quoracdn.net/main-qimg-346aef273af21139ac0ac938662b2035-c)]

## Issue summary

The website of one of our clients was on migration was down from 12:00 a.m. to 1:15 a.m. (GMT - 5) on a Cyberday sales, avoiding users from visiting their web page and losing sells as a result. After investigation, it turns out that the issue was about misconfiguration on some Wordpress migration files and Nginx caused by a misconfigured puppet manifiest. 

## Timeline

| Time | Fact count|
|-----| --------|
|12: 05 a.m. |The owner of hagosillas.com called to report that their website is down|
|12: 35 a.m. | One of the DevOps team member on shift that night started to investigate the incident|
|12: 55 a.m. | The typo in the wordpress configuration file was found and solved|
|01: 15 a.m. |  The  misconfiguration option of Nginx was found and solved|
|01: 00 a.m. | The root cause was found and solved|

## Root causes 
Given the 500 status code as a response for any petition to the server, strace command was used in order to track down the issue. It turns out that the website crash was caused by a typo on the Wordpress configuration file, but after that the server still didn't serve any content, because the typo refered to a file that wasn't crucial, so the server can continue working even with that issue. Checking all the needed configuration, a Nginx misconfigured option about how many processes can handle was found and it was overriding on this outage. This last issue was caused by a puppet manifest runned in the wrong server, found in the home directory of the server. The next day, and after the investigation, it was determined that one of the DevOps team member was trying to configure this server and testing options in a Docker container at the same time and mixes puppet manifests of both of them. 

## Corrective and preventive measures

### Corrective measures:
Given the typo on the website configuration, the web developer team has been asked to document general issues at the end of the day in order to having into account for debugging tasks.

The idea of doing one task at the time was reinforced to the DevOps team members, to avoiding misconfiguration issues. Also, the need of well documented puppet manifests was discussed and assumed as a standard.

### Preventive measures:

Meetings between developers and DevOps teams has been scheduled in order to work on communication skills and  sharing of common processes and knowledge for both teams. 
