#!/usr/bin/env python

import rospy
import os
import signal
import subprocess


def ControlLauncher(object):

    def __init__(self):
        rospy.init_node('control_launcher', anonymous=True)
        self.control_nodes = []
        rospy.on_shutdown(self.shutdown)
        drones = rospy.get_param('drones')
        controller_ns = rospy.get_param('ns')
        for drone in drones:
            ns = drone['ns']
            cmd = ('roslaunch mav_control main_utm.launch ns:="{controller_ns}/{ns}"'.
                   format(**locals()))
            self.control_nodes.append(subprocess.Popen(cmd, preexec_fn=os.setsid))

    def shutdown(self):
        for p in self.control_nodes:
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)


if __name__ == '__main__':
    ControlLauncher()
