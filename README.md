An application that predicts the category of a youtube video using it's decription as an input

- To deploy a containerized application for a machine learning model
- to run this app on your local machine:
	- clone this repository
	- navigate to this folder in terminal
	- $ docker build -t yt01 . #build a docker image to run this app
	- $ docker run -d -p 5000:5000 yt01 #run the above built image on port 5000
