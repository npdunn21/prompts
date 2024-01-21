# prompts
Repo for journal prompt email notification app

Project contains:
- Functionality to prompt OpenAI to generate journal prompts
- Functionality to send a daily email notification with 3 prompts
- Dockerfile for deploying app in cloud

To deploy and run:
1. Build docker image (`docker build -t prompts`)
2. Tag docker image (`docker tag [image tag] [region]-docker.pkg.dev/[artifactory repository path]/[image name]:[version]`)
3. Push docker image to artifact repository (`docker push us-east4-docker.pkg.dev/[artifactory repository path]/[image name]:[version]`)
4. Run the image in a GKE deployment (`kubectl create deployment [cluster name] --image=[region]-docker.pkg.dev/[artifactory repository path]/[image name]:[version]`)

Improvements:
1. There's no tracking right now for if there are duplicate prompts
2. There's probably a better way of deploying this sort of app in the cloud - deploying it to a GKE cluster is probably overkill, probably could use a cron job or something like that