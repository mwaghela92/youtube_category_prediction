#currently developed locally and exported pickle file to be used in the app
#will be updated if docker is used for development
$ docker build -t model_dev .
$ docker run -v /Users/zeemee/Documents/python_projects/youtube/youtube_data:/data model_dev:latest