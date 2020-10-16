# demo github actions

![Testing](https://github.com/danielino/demo-github-actions/workflows/Testing/badge.svg)



## deploy on gcp

- create service account

    ```
    gcloud iam service-accounts create ghactions --description="github actions service account" --display-name="sa-github-actions"
    gcloud iam service-accounts keys create ~/key-sa-gcp-demo-actions.json --iam-account ghactions@worm-poc.iam.gserviceaccount.com
    ```