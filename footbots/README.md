# A demostration of the multi agent synchronization mechanism developed for DroneFlyWay


## Installation

```bash
> git clone https://github.com/jeguzzi/dfw-server.git
> docker-compose -f footbots/docker-compose.yml pull
```

## Configuration

### Select the set of robots

Edit the command of service ```footbot_bridge``` in ```footbots/docker-compose.yml```
to select the set of footbots to use.

### Modify the robots' colors

Edit ```footbots/worlds/footbots/config.yaml``` to modify the footbots' colors.

```yaml
command: rosrun footbot_tools footbot_control.py _robots:=[32,51,53,55,60,66]
```

### Modify the robots' path

Edit ```footbots/planner.launch``` to modify the (initial) footbots' paths.

```xml
<rosparam param="paths">
   footbot_32: L2S108,L2S66,...
   footbot_51: L2S108,L2S66,...
   footbot_53: L2S108,L2S66,...
   footbot_55: L2S105,L2S69,...
   footbot_60: L2S105,L2S69,...
   footbot_66: L2S105,L2S69,...
</rosparam>
```

A path is encoded in a string as a list of cell to reach sequentially. It may optionally end by ```...```, which is interpreted as a instruction to loop over the sequence
```yaml
<Cell_id>,<Cell_id>,<Cell_id>[...]
```

Cells should belong to the [navigation layer](http://192.168.201.4/worlds/Footbots/map/layers/L2).


## Running

We assume that the demo runs on the demo machine with IP 192.168.201.4.

### Setup

1. Switch on the selected footbots (by default 32, 51, 53, 55, 60 and 66).

2. Launch roscore
```bash
> roscore
```   

3. On the optitrack machine:

   - start motive,
   - open the project `DFW_footbots`,
   - [optional] recalibrate the tracker,
   - start streaming,
   - launch `rosdemo`

4. Launch the docker containers using either
```bash
> docker-compose -f footbots/docker-compose.yml up -d
```
or the [docker-compose GUI](http://192.168.201.4:5000)

4. Place the footbots inside the navigable area.

5. [Visualize the system](http://192.168.201.4:http://localhost:5000/worlds/Footbots/live?drone=footbot_66). You can highlight a robot's path, by appending the robot's id to the url.
```
http://192.168.201.4/worlds/Footbots/live?drone=<footbot_id>
```
You can also [visualize all tracked rigid bodies](http://192.168.201.4/worlds/Footbots/localization)


## Stopping

1. Stop the docker containers, using either
```bash
> docker-compose -f footbots/docker-compose.yml down
```
or the [docker-compose GUI](http://192.168.201.4:5000)
2. Switch off the footbots
