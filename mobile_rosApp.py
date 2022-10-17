#!/usr/bin/env python

import rospy, os
from std_msgs.msg import String, Bool
from kuka_tasks import KUKA_TASKS
import tools


class MOB_APP_ROS_CMDS:
    def __init__(self, var):
        self.var = var
        self.kuka_tasks = KUKA_TASKS(self.var)
        # self.p2 = False
        # self.p3 = False
        # self.p4 = False
        # self.p5 = False
        # self.p6 = False
        # self.rtn = False
        # self.calib = False
        self.Compliance = False
        self.saveInit = False
        self.debug_msg = ''

        rospy.Subscriber("btn_press1", Bool, self.btn_press1_callback)
        rospy.Subscriber("btn_press2", Bool, self.btn_press2_callback)
        rospy.Subscriber("btn_press3", Bool, self.btn_press3_callback)
        rospy.Subscriber("btn_press4", Bool, self.btn_press4_callback)
        rospy.Subscriber("btn_press5", Bool, self.btn_press5_callback)
        rospy.Subscriber("btn_press6", Bool, self.btn_press6_callback)
        rospy.Subscriber("btn_press_return", Bool, self.btn_press_return_callback)
        rospy.Subscriber("btn_press_calib", Bool, self.btn_press_calib_callback)
        rospy.Subscriber("btn_press_freeMode", Bool, self.btn_press_freeMode_callback)
        rospy.Subscriber('btn_press_gait', Bool, self.btn_press_gait_callback)
        rospy.Subscriber('btn_press_arc', Bool, self.btn_press_arc_callback)
        rospy.Subscriber('btn_press_saveInit', Bool, self.btn_press_saveInit_callback)
        
        self.debugPub = rospy.Publisher('mob_app_debug_msg', String, queue_size=10)

        # rospy.init_node('ros_mobApp_node', anonymous=False)
        self.rate = rospy.Rate(100)

    def btn_press1_callback(self, data):
        self.var.move2Point = 1
        if self.var.gaitMode:
            self.debug_msg = 'Walking Left (P1)'
        elif not self.var.gaitMode and self.var.moveMode == 'arc':
            self.debug_msg = 'Moving arc to Left (P1)'
        else:
            self.debug_msg = 'Moving ptp to Left (P1)'
        self.publish_debug_msg()

    def btn_press2_callback(self, data):
        self.var.move2Point = 2
        if self.var.gaitMode:
            self.debug_msg = 'Walking Straight (P2)'
        elif not self.var.gaitMode and self.var.moveMode == 'arc':
            self.debug_msg = 'Moving arc Straight (P2)'
        else:
            self.debug_msg = 'Moving ptp Straight (P2)'
        self.publish_debug_msg()
        

    def btn_press3_callback(self, data):
        self.var.move2Point = 3
        if self.var.gaitMode:
            self.debug_msg = 'Walking Right (P3)'
        elif not self.var.gaitMode and self.var.moveMode == 'arc':
            self.debug_msg = 'Moving arc to Right (P3)'
        else:
            self.debug_msg = 'Moving ptp to Right (P3)'
        self.publish_debug_msg()

    def btn_press4_callback(self, data):
        self.var.move2Point = 4
        if self.var.gaitMode:
            self.debug_msg = 'Walking Left (P4)'
        elif not self.var.gaitMode and self.var.moveMode == 'arc':
            self.debug_msg = 'Moving arc to Left (P4)'
        else:
            self.debug_msg = 'Moving ptp to Left (P4)'
        self.publish_debug_msg()

    def btn_press5_callback(self, data):
        self.var.move2Point = 5
        if self.var.gaitMode:
            self.debug_msg = 'Walking Straight (P5)'
        elif not self.var.gaitMode and self.var.moveMode == 'arc':
            self.debug_msg = 'Moving arc Straight (P5)'
        else:
            self.debug_msg = 'Moving ptp Straight (P5)'
        self.publish_debug_msg()

    def btn_press6_callback(self, data):
        self.var.move2Point = 6
        if self.var.gaitMode:
            self.debug_msg = 'Walking Right (P6)'
        elif not self.var.gaitMode and self.var.moveMode == 'arc':
            self.debug_msg = 'Moving arc to Right (P6)'
        else:
            self.debug_msg = 'Moving ptp to Right (P6)'
        self.publish_debug_msg()

    def btn_press_return_callback(self, data):
        self.var.move2Point = 0
        if self.var.cur_leg == 'left':
            pos = f'{self.var.leftLeg_init_pos.x} {self.var.leftLeg_init_pos.y} {self.var.leftLeg_init_pos.z} {self.var.leftLeg_init_pos.a} {self.var.leftLeg_init_pos.b} {self.var.leftLeg_init_pos.c}'
            self.kuka_tasks.move_2_XYZABC(pos, 'ptp')
            self.debug_msg = 'moving to initial position of Left Leg'
            print(self.debug_msg)
            self.publish_debug_msg()
        if self.var.cur_leg == 'right':
            pos = f'{self.var.rightLeg_init_pos.x} {self.var.rightLeg_init_pos.y} {self.var.rightLeg_init_pos.z} {self.var.rightLeg_init_pos.a} {self.var.rightLeg_init_pos.b} {self.var.rightLeg_init_pos.c}'
            self.kuka_tasks.move_2_XYZABC(pos, 'ptp')
            self.debug_msg = 'moving to initial position of Right Leg'
            print(self.debug_msg)
            self.publish_debug_msg()
        
    
    def btn_press_calib_callback(self, data):
        if data.data  and  not self.var.setPointOrientation:
            self.var.setPointOrientation = True
            self.debug_msg = 'Calibration Mode is ON!'
            self.publish_debug_msg()
        elif data.data  and  self.var.setPointOrientation:
            self.var.setPointOrientation = False
            self.debug_msg = 'Calibration Mode is OFF!'
            self.publish_debug_msg()
        
        

    def btn_press_freeMode_callback(self, data):
        if data.data and not self.Compliance:
            self.Compliance = True
            comp = [self.var.xy_compliant, self.var.xy_compliant, self.var.z_compliant, 
                    self.var.abc_compliant, self.var.abc_compliant, self.var.abc_compliant]
            self.kuka_tasks.setCompliance(comp)
            self.debug_msg = 'Free Mode is ON!'
            self.publish_debug_msg()
        elif data.data and self.Compliance:
            self.Compliance = False
            self.kuka_tasks.resetCompliance()
            self.debug_msg = 'Free Mode is OFF!'
            self.publish_debug_msg()

    def btn_press_gait_callback(self, data):
        if data.data and self.var.gaitMode:
            self.var.gaitMode = False
            self.debug_msg = 'Gait Mode is ON!'
            self.publish_debug_msg()
        elif data.data and not self.var.gaitMode:
            self.var.gaitMode = True
            self.debug_msg = 'Gait Mode is OFF!'
            self.publish_debug_msg()

    def btn_press_arc_callback(self, data):
        if data.data and not self.var.moveMode == 'arc':
            self.var.moveMode = 'arc'
            print('moveMode: ARC')
            self.debug_msg = 'ARC Mode is ON!'
            self.publish_debug_msg()
        elif data.data and self.var.moveMode == 'arc':
            self.var.moveMode = 'ptp'
            print('moveMode: PTP')
            self.debug_msg = 'ARC Mode is OFF!'
            self.publish_debug_msg()

    def btn_press_saveInit_callback(self, data):
        cur_xyzabc = self.kuka_tasks.getXYZABC()
        print(cur_xyzabc)
        if self.var.cur_leg == 'left': 
            key_ = 'left'
            values_ = {'init_pos': cur_xyzabc}
            tools.save_data(key_, values_)
            self.var.leftLeg_init_pos.x = cur_xyzabc[0]
            self.var.leftLeg_init_pos.y = cur_xyzabc[1]
            self.var.leftLeg_init_pos.z = cur_xyzabc[2]
            self.var.leftLeg_init_pos.a = cur_xyzabc[3]
            self.var.leftLeg_init_pos.b = cur_xyzabc[4]
            self.var.leftLeg_init_pos.c = cur_xyzabc[5]
            print("~ New Initial Point is recorded for Left Leg! ~")
            self.debug_msg = 'SAVED LEFT LEG INIT POSITION'
            self.publish_debug_msg()
        if self.var.cur_leg == 'right':
            key_ = 'right'
            values_ = {'init_pos': cur_xyzabc}
            tools.save_data(key_, values_)
            self.var.rightLeg_init_pos.x = cur_xyzabc[0]
            self.var.rightLeg_init_pos.y = cur_xyzabc[1]
            self.var.rightLeg_init_pos.z = cur_xyzabc[2]
            self.var.rightLeg_init_pos.a = cur_xyzabc[3]
            self.var.rightLeg_init_pos.b = cur_xyzabc[4]
            self.var.rightLeg_init_pos.c = cur_xyzabc[5]
            print("~ New Initial Point is recorded for Right Leg! ~")
            self.debug_msg = 'SAVED RIGHT LEG INIT POSITION'
            self.publish_debug_msg()

    
    def publish_debug_msg(self):
        # if not rospy.is_shutdown():
        self.debugPub.publish(self.debug_msg)