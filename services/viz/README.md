## To visualiza the copter/rover in rviz

### Instal

clone the rep in your local catkin workspace
```bash
cd <catkin_ws>/src
git clone https://github.com/jeguzzi/dfw-models
```

## Run

1. start the service, e.g. when running
```bash
docker-compose -f wifi/docker-compose.yml up -d
```

2. launch rviz
```bash
roslaunch erle_models rviz.launch
```
