# aws-lambda-splinter-headless-chrome

A sample AWS Lambda Deployment package (for Python 3.7) to get started with Web automation using Splinter (which internally uses Selenium Remote Driver) and Headless Chrome.

<b>Libraries used:</b>
1. splinter v0.11.0 (https://splinter.readthedocs.io/en/latest/)
2. selenium v3.141.0 (https://pypi.org/project/selenium/)
3. headless-chrome v1.0.0-55 (https://github.com/adieuadieu/serverless-chrome/releases/tag/v1.0.0-55) 
4. chromedriver v2.43 (https://chromedriver.storage.googleapis.com/index.html?path=2.43/)

<b>--------------------</b><br>
If you decide to upgrade any/all of the above libraries to a newer version, please be advised that it may result in compatibility issues. 

As a result of this, you may possibly face the below errors in the Lambda function (in case you don't see any errors and the Lambda function times out, try setting the Lambda Timeout config to at least a minute):

<i>[ERROR] WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally</i>

<i>(unknown error: DevToolsActivePort file doesn't exist)</i>

<i>(The process started from chrome location /var/task/headless-chromium is no longer running, so ChromeDriver is assuming that Chrome has crashed.)</i>
  
<i>[ERROR] SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 76</i>

<i>[ERROR] WebDriverException: Message: chrome not reachable</i>
<br><b>--------------------</b>
