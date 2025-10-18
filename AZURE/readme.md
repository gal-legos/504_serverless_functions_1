## Azure Function App
### creation steps
To create the function app in azure I was able to deploy it by searching for the "sunction app" in the search bar and then clicking on the the icon with a lightning bolt. From there I hit create and the steps to set up a function were similar to setting up a virtual machine in the sense that both require a name, a region selection, and the choice of OS. For the function app I chose linux over windows and selected python. From there I went on to adjust the networking, monitoring, and deployment to creat this function application. Once deployed it moved pretty wuick and after clicking on the resource we then clicked create function. Once in the function it opened up a code source where it could be edited. From there I created my code. A cool thing about Azure was the ability to test run the code without needing a terminal or an output script in your choice of code editor. Another interesting tidbit was that azure gave 3 urls instead of 1 based off of what was needed. Unfortunately for me, the code did not work one time and my overuse of azure led to me being temporarily banned from deploying a new function. Below you will see screenshots of my attempt at azure and a terminal code i used to troubleshoot.


#### trouble shoot code
curl with url


###### had to break the link to post




## Screenshots
![did_not_work](serverless_function_screenshots/fml.png)


![colab_output](serverless_function_screenshots/original_zure_colab_output.png)