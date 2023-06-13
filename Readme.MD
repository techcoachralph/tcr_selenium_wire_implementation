## Selenium-Wire Implementation using AWS Device Farm
### By Tech Coach Ralph

This is the repository from my very first livestream where I was attempting to troubleshoot implementing Selenium-Wire with the RemoteDriver.

Based on the documentation from Selenium-Wire, there is very limited implementation and support for having it work with the RemoteDriver. 
It works great locally but figuring out how to have it work on a Selenium Grid environment, CI/CD Pipeline via Jenkins/Teamcity, or with the AWS Device Farm is a bit complicated.

What is Selenium Wire?
Selenium Wire extends Selenium’s Python bindings to give you access to the underlying requests made by the browser. You author your code in the same way as you do with Selenium, but you get extra APIs for inspecting requests and responses and making changes to them on the fly.

https://pypi.org/project/selenium-wire/

Here is a link to the livestream where I attempted to configure Selenium-Wire with the AWS Device Farm.

https://www.youtube.com/watch?v=zzyxMoWOYXU

Since them, through hours of investigation and trying different configurations through Docker and AWS EC2 Instances, I have gotten a much better understanding of Selenium-Wire.

After cloning this project, you will need to create a config.json file and store your AWS project ARN when generating the grid URL.

```commandline
{
  "aws_project_arn": "arn provided by AWS Device Farm goes here"
}
```

In upcoming Livestreams, we will be going through the configuring Selenium-Wire to work with a local Docker container with Selenium Grid, selenium-wire on AWS EC2 instance, and integrating it with the AWS Device Farm. 

After those shows, I will push the code to a separate branch to review and follow along.

If you have any questions, feel free to contact me.

Check out the YouTube Channel for more content:
https://youtube.com/@TechnicalCoachingWithRalph