#!/usr/bin/env python3
import os
import rospkg
import rospy
from geometry_msgs.msg import *
from python_qt_binding import *
from python_qt_binding.QtCore import *
from python_qt_binding.QtWidgets import *
from std_srvs.srv import *
from turtlesim.msg import Pose
#from pynput import keyboard          -- If keyboard inputs are needed then add the pynput module .
#from pynput.keyboard import Key, Listener


from move_turtle_1 import MoveTurtle

class TurtleGuiPlugin:
    def __init__(self):
        #Initializing a node for getting the position of our turtle   
        rospy.init_node('moveturtle', anonymous=True)
        self._widget = QWidget()
        #Subcribing this node to the topic pose
        rospy.Subscriber('/turtle1/pose',Pose,self.pose_callback)
        # Getting the path of our Ui File and loading it in
        ui_file = os.path.join(rospkg.RosPack().get_path('turtle_gui'), 'src', 'turtle_gui_plugin.ui')
        loadUi(ui_file, self._widget)
        self._widget.setObjectName('TurtleGuiPluginUi')
        self._widget.up.setAutoRepeat(True)
        self._widget.up.setAutoRepeatInterval(40)
        self._widget.up.pressed.connect(self.up_move)
        self._widget.down.setAutoRepeat(True)
        self._widget.down.setAutoRepeatInterval(40)
        self._widget.down.pressed.connect(self.down_move)
        self._widget.down.setAutoRepeat(True)
        self._widget.down.setAutoRepeatInterval(40)

        self._widget.left.pressed.connect(self.left_move)
        self._widget.down.setAutoRepeat(True)
        self._widget.down.setAutoRepeatInterval(40)
        self._widget.right.pressed.connect(self.right_move)

        self.moveturtle= MoveTurtle()
        self._widget.show()

    def pose_callback(self,pose):
        self.a=pose.x
        self.b=pose.y
        self._widget.xdisplay.display(self.a)
        self._widget.ydisplay.display(self.b)
        
    def up_move(self):
        try:
            self.moveturtle.Up()
        except rospy.ServiceException as e:
            print("Move Up failed: %s" % e)

    def down_move(self):
        try:
            self.moveturtle.Down()
        except rospy.ServiceException as e:
            print("Move Down failed: %s" % e)

    def left_move(self):
        try:
            self.moveturtle.Left()
        except rospy.ServiceException as e:
            print("Move Left failed: %s" % e)

    def right_move(self):
        try:
            self.moveturtle.Right()
        except rospy.ServiceException as e:
            print("Move Right failed: %s" % e)

 
if __name__=="__main__":
    app = QApplication(sys.argv)
    x = TurtleGuiPlugin()
    sys.exit(app.exec_())
