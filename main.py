#!/usr/bin/env python
# ========================================  
#      * Author: nipun.dhananjaya@gmail.com  
#      * Created: xx.08.2022  
# ======================================== 
import PySimpleGUIQt as sg
from multiprocessing import Process
import threading
import numpy as np
import time as time
import json


import server_V30032017 as iiwa_server
from client_lib import kuka_iiwa_ros_client
from kuka_tasks import KUKA_TASKS

from tools import VARIABLES, KEYS, rehab_gui_layout, saved_data_update, data_file
from gui_event_handler import event_handler
from mobile_rosApp import MOB_APP_ROS_CMDS




kuka = kuka_iiwa_ros_client()

var = VARIABLES()
key = KEYS()
kuka_tasks = KUKA_TASKS(var)
isGUI_close = False
mobApp_cmd = MOB_APP_ROS_CMDS(var)

# ================================================== LOADING and UPDATING SAVED DATA ========================================
saved_data_update(var)

# ===================== GUI LAYOUT ===============================================================================================================================
sg.theme("DarkAmber")
layout = rehab_gui_layout(sg, var, key)
window = sg.Window('TEST GUI1', layout)

# ==================================================================================================================================================================================
# ==================================================================================================================================================================================


def XYZABC_DISPLAY():
    if not kuka.ToolPosition[0][0] == None: window.FindElement(key.disp.nowX).Update(f'{kuka.ToolPosition[0][0]:.2f}')
    if not kuka.ToolPosition[0][1] == None: window.FindElement(key.disp.nowY).Update(f'{kuka.ToolPosition[0][1]:.2f}') 
    if not kuka.ToolPosition[0][2] == None: window.FindElement(key.disp.nowZ).Update(f'{kuka.ToolPosition[0][2]:.2f}')
    if not kuka.ToolPosition[0][3] == None: window.FindElement(key.disp.nowA).Update(f'{kuka.ToolPosition[0][3]:.2f}')
    if not kuka.ToolPosition[0][4] == None: window.FindElement(key.disp.nowB).Update(f'{kuka.ToolPosition[0][4]:.2f}')
    if not kuka.ToolPosition[0][5] == None: window.FindElement(key.disp.nowC).Update(f'{kuka.ToolPosition[0][5]:.2f}')

def JOINT_POSITION_DISPLAY():
    if not kuka.JointPosition[0][0] == None: window.FindElement(key.disp.nowJ1).Update(f'{kuka.JointPosition[0][0]:.2f}')
    if not kuka.JointPosition[0][1] == None: window.FindElement(key.disp.nowJ2).Update(f'{kuka.JointPosition[0][1]:.2f}') 
    if not kuka.JointPosition[0][2] == None: window.FindElement(key.disp.nowJ3).Update(f'{kuka.JointPosition[0][2]:.2f}')
    if not kuka.JointPosition[0][3] == None: window.FindElement(key.disp.nowJ4).Update(f'{kuka.JointPosition[0][3]:.2f}')
    if not kuka.JointPosition[0][4] == None: window.FindElement(key.disp.nowJ5).Update(f'{kuka.JointPosition[0][4]:.2f}')
    if not kuka.JointPosition[0][5] == None: window.FindElement(key.disp.nowJ6).Update(f'{kuka.JointPosition[0][5]:.2f}')
    if not kuka.JointPosition[0][6] == None: window.FindElement(key.disp.nowJ7).Update(f'{kuka.JointPosition[0][6]:.2f}')

def run_gui():
    
    while True:
        event, values = window.read()
        window.FindElement("_output_").Update("")
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        elif not kuka.isready:
            print('Please connect kuka via running server_V30032017.py')
        else:
            event_handler(window, event, values, key, var)
            
    var.close = True

    window.close()

def tasks():
    time.sleep(1)

    while not var.close:
        
        XYZABC_DISPLAY()
        JOINT_POSITION_DISPLAY()
        
        if var.move2Point == 0:
            var.isInitialSwing = True
            var.point_tracker = 'init'
            
        
        elif var.move2Point == 1:
            if var.setPointOrientation:
                kuka_tasks.set_point_orientations(1)
            else:
                kuka_tasks.move2_P(1)
            # kuka_tasks.set_point_orientations(1)
        elif var.move2Point == 2:
            if var.setPointOrientation:
                kuka_tasks.set_point_orientations(2)
            else:
                kuka_tasks.move2_P(2)
        elif var.move2Point == 3:
            if var.setPointOrientation:
                kuka_tasks.set_point_orientations(3)
            else:
                kuka_tasks.move2_P(3)
        elif var.move2Point == 4:
            if var.setPointOrientation:
                kuka_tasks.set_point_orientations(4)
            else:
                kuka_tasks.move2_P(4)
        elif var.move2Point == 5:
            if var.setPointOrientation:
                kuka_tasks.set_point_orientations(5)
            else:
                kuka_tasks.move2_P(5)
        elif var.move2Point == 6:
            if var.setPointOrientation:
                kuka_tasks.set_point_orientations(6)
            else:
                kuka_tasks.move2_P(6)

        # print(kuka.isFinished[0])
        

        time.sleep(0.1)
    


# ================================  ~MAIN~   =============================================================================
def main(args=None):
    print("Starting..")
    print(kuka.ToolPosition[0][0])

    thread_run_task = threading.Thread(target=tasks)

    try:
        thread_run_task.start()
        run_gui()

    except:
        print('Err')

if __name__ == '__main__':
    main()
