# Image2Text and Translator
## How to use

**Installing the clients library**
```
pip install --upgrade google-cloud-translate google-cloud-vision
```

**Setting up authentication**

You can run the following commands using the Cloud SDK on your local machine, or within Cloud Shell.
1. Create the service account. Replace [NAME] with your desired service account name.
```
gcloud iam service-accounts create [NAME]
```
2. Grant permissions to the service account. Replace [PROJECT_ID] with your project ID.
```
gcloud projects add-iam-policy-binding [PROJECT_ID] --member "serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role "roles/owner"
```
3. Generate the key file. Replace [FILE_NAME] with a name for the key file.
```
gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com
```
4. Provide authentication credentials to your application code by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS. Replace [PATH] with the file path of the JSON file that contains your service account key, and [FILE_NAME] with the filename.

   **Windows**
   - With PowerShell:
     ```
     $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]\[FILE_NAME].json"
     ```
   - With command prompt:
     ```
     set GOOGLE_APPLICATION_CREDENTIALS=[PATH]\[FILE_NAME].json
     ```
   
   **Linux or MacOS**
     ```
     export GOOGLE_APPLICATION_CREDENTIALS="[PATH]/[FILE_NAME].json"
     ```   

**Running**

`python main.py`
