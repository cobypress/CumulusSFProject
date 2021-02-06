# Salesforce Test Data Creation with CumulusCI & Snowfakery

what you will need - an up to date version of Python and CumulusCI

If you are using Mac and are looking to do quite a lot of work with Python, I would 100% reccomend using HomeBrew, I end up using it atleast once a week to install a package.

First off I would complete this trail on Trailhead as it gives you a pretty banging understanding of CumulusCI and will walk you through the test of setting it up

https://trailhead.salesforce.com/en/content/learn/trails/build-applications-with-cumulusci

## How to upload?

If you end up getting to a point where you have everything installed and want to get some test data in your org, then run the following commands in terminal - 

To connect your org - cci org connect
To run the flow - cci flow run run_everything --org {Your org name}

if you want to run a specific task in CumulusSFProject/cumulusci.yml then you can do cci task run {task name} --org {org name}

## Read All About It

Trailhead - https://trailhead.salesforce.com/en/content/learn/trails/build-applications-with-cumulusci

Snowfakery GitHub - https://github.com/SFDO-Tooling/Snowfakery

Snowfakery GitHub Documentation - https://github.com/SFDO-Tooling/Snowfakery/blob/master/docs/index.md

CumulusCI GutHub - https://github.com/SFDO-Tooling/CumulusCI

CumulusCI Documentation - https://cumulusci.readthedocs.io/en/latest/

SnowFakery Documentation - https://snowfakery.readthedocs.io/en/stable/

CumulusCI Partner Training - https://partners.salesforce.com/s/education/general/CumulusCI

HomeBrew - https://brew.sh/
