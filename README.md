# Serverless Functions Lab

## Lab Rules
For this serverless functions assignment, I chose HbA1c levels as my chosen medical indicator.
HbA1c normal level : <5.7%
HbA1c Pre-diabetic level 5.7%-6.4%
HbA1c Diabetic level: >6.5%
with <5.7% correlating to "normal", 5.7-6.4% correlating to "elevated", and >6.5% correlating to "high"




Citation:
Diabetes diagnosis. Diabetes Diagnosis & Tests | ADA. (n.d.). https://diabetes.org/about-diabetes/diagnosis


## Cloud Environments Used
The cloud environments used for this assignment were GCP's Cloud Run and OCI's Application. More information on the individual cloud running and screenshots can be found in their relevant folders (i.e., GCP cloud run will be found in the gcp folder, and OCI will be found in the oci folder). Having used all three different cloud environments for this assignment, I can confidently say that my preferred environment is GCP. This is for a variety of reasons. While using Microsoft's Azure function app, I thought that would be my preference since it seemed to work quickly, deploy relatively fast, and even append changes super quickly; however, I was sorely mistaken. When using Azure, as a novice myself who was trying my best to navigate and fix errors, Azure would repeatedly time out and no longer load the code, the logs, or the function. To work quickly because there was limited time, I had deleted and redeployed multiple times, which then led to me reaching my deployment limit in Azure (100% my fault, but definitely unexpected). And even when attempting to fix the errors and parse through where it was going wrong, Azure did not give a clear picture of what was going wrong; it gave just a basic error. In addition to a lack of clarity in terms of troubleshooting code, the HTTP trigger function created for the application would no longer exist once I left the "code+test" window, which I did not like at all. When compared to GCP, I appreciated that GCP gave a clear picture of what was going wrong within the code through the logs, which were conveniently found on the left side of the source code under "logs". As well as being able to find and navigate around GCP more easily, the HTTP trigger function would not disappear when leaving the source window. At first, the user interface of GCP seemed a little more strenuous due to the small source code window, and the lag time between editing the code and then redeploying, but after using all 3 cloud environemnts I 100%% prefer the GCP cloud run. As for OCI, while i do have a preference for GCP, it feels a bit unfair, more so because I was navigating around OCI mainly through the combined efforts of YouTube, Google, ChatGPT, and OCI's tutorial guides. I like the clean user interface that is seen in OCI, and that there are tutorial guides to help you with setting things up. However, OCI's cloud run equivalent seemed to be the "application" selection that lived within the developer services. Funnily, there was more to do for OCI to initially set up the application, but also less to do at the same time. In comparison to GCP, I preferred the OCI terminal to the GCP terminal. The GCP terminal just felt a little too jarring, jumping from white to a cobalt blue. Overall, GCP is the winner for this assignment, not only in terms of deployment but also in terms of my heart.



