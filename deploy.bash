# stops, removes and builds an image for VeRNAl
# runs the container on port 5002

sudo docker container stop vernal
sudo docker container rm vernal 

sudo docker build -t vernal .
sudo docker run -p 5002:5002 -d -t --restart on-failure --network=PipelineNetwork  --name vernal vernal 
