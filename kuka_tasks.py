#!/usr/bin/env python
# ========================================  
#      * Author: nipun.dhananjaya@gmail.com  
#      * Created: xx.08.2022  
# ========================================  
import server_V30032017 as iiwa_server
from client_lib import kuka_iiwa_ros_client
import numpy as np
import os
import time
import json
from trajectory_points import P1, P2, P3, P4, P5, P6
from tools import  save_data, saved_data_update


kuka = kuka_iiwa_ros_client()

z_err = 1332





class KUKA_TASKS():
    def __init__(self, var):
        self.var = var
    
    def setTool(self, tool):
        kuka.send_command('setTool '+ tool)
        print('>> setTool '+ tool)

    def setVel(self, vel):
        kuka.send_command(f'setJointVelocity {vel}')
        print(f'>> setJointVelocity {vel}')

    def setAcc(self, acc):
        kuka.send_command(f'setJointAcceleration {acc}')
        print(f'>> setJointAcceleration {acc}')

    def setJrk(self, jrk):
        kuka.send_command(f'setJointJerk {jrk}')
        print(f'>> setJointJerk {jrk}')

    def setCartVel(self, cartVel):
        kuka.send_command(f'setCartVelocity {cartVel}')
        print('>> setCartVelocity {cartVel}')

    def setImp(self, imp):
        kuka.send_command(f'setCartImpCtrl {imp}')
        print(f'>> setCartImpCtrl {imp}')

    def setAngs(self, angs):
        kuka.send_command(f'setPosition {angs}')
        print(f'>> setPosition {angs}')


    def move_2_XYZABC(self, pos, mode='ptp'):
        pos = pos.split(' ')
        z = pos.pop(2)
        pos.insert(2, '{}'.format(-z_err + float(z)))
        pos = '{} {} {} {} {} {}'.format(pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])
        kuka.send_command('setPositionXYZABC {} {}'.format(pos, mode))
        print('>> setPositionXYZABC {} {}'.format(pos, mode))

    def getXYZABC(self):
        return kuka.ToolPosition[0][:]

    def moveCirc(self, Pmid, Pend, blend):
        Pmid = Pmid.split(' ')
        Zmid = Pmid.pop(2)
        Pend = Pend.split(' ')
        Zend = Pend.pop(2)
        Pmid.insert(2, '{}'.format(-z_err + float(Zmid)))
        Pend.insert(2, '{}'.format(-z_err + float(Zend)))
        Pmid = '{} {} {} {} {} {}'.format(Pmid[0], Pmid[1], Pmid[2], Pmid[3], Pmid[4], Pmid[5])
        Pend = '{} {} {} {} {} {}'.format(Pend[0], Pend[1], Pend[2], Pend[3], Pend[4], Pend[5])
        kuka.send_command('MoveCirc {} {} {}'.format(Pmid, Pend, blend))
        print('>> MoveCirc {} {} {}'.format(Pmid, Pend, blend))

    def setCompliance(self, comp = [2,2,10,5,5,5]):
        val = f'{comp[0]} {comp[1]} {comp[2]} {comp[3]} {comp[4]} {comp[5]}'
        kuka.send_command('setCompliance {}'.format(val))
        print('>> setCompliance {}'.format(val))

    def resetCompliance(self):
        kuka.send_command('resetCompliance')
        print('>> resetCompliance')

    def init_swing(self, point, reverse = False):
        if not reverse:
            print('================ INIT SWING ===================')
            self.moveCirc(point.init_sw_midLow, point.init_sw_mid, self.var.blendingOri)
            self.moveCirc(point.init_sw_midUp, point.sw_end, self.var.blendingOri)
        else:
            print('================ INIT SWING REVERSE ===================')
            self.moveCirc(point.init_sw_midUp, point.init_sw_mid, self.var.blendingOri)
            self.moveCirc(point.init_sw_midLow, point.init_point, self.var.blendingOri)
    
    def full_swing(self, point):
        print('================ FULL SWING ===================')
        self.moveCirc(point.sw_midLow, point.sw_mid, self.var.blendingOri)
        self.moveCirc(point.sw_midUp, point.sw_end, self.var.blendingOri)
    
    def half_stance_1(self, point):
        print('================ 1st HALF STANCE ===================')
        self.moveCirc(point.st_midUp, point.st_mid, self.var.blendingOri)

    def half_stance_2(self, point):
        print('================ 2nd HALF STANCE SWING ===================')
        self.moveCirc(point.st_midLow, point.st_end, self.var.blendingOri)

    def move2_P(self, P ):
        if P == 1:
            p = P1(self.var)
        elif P == 2:
            p = P2(self.var)
        elif P == 3:
            p = P3(self.var)
        elif P == 4:
            p = P4(self.var)
        elif P == 5:
            p = P5(self.var)
        else :
            p = P6(self.var)

        # NOT GAIT MODE
        if not self.var.gaitMode:
            # ptp and lin
            if self.var.moveMode == 'ptp' or self.var.moveMode == 'lin':
                self.move_2_XYZABC(p.sw_end, self.var.moveMode)
                self.var.move2Point = 0
            # arc (swing)
            elif self.var.moveMode == 'arc':
                # swing forward
                self.init_swing(p)
                # swing backward
                time.sleep(1)
                self.init_swing(p, reverse=True)
                self.var.move2Point = 0

        # GAIT MODE
        elif kuka.isFinished[0]:
            print('init swing done')
            # init gait cycle
            if self.var.isInitialSwing:
                if self.var.point_tracker == 'init'  and not self.var.move2Point == 0:
                    self.init_swing(p)
                    time.sleep(0.4)
                    if not kuka.hasError[0]:
                        self.var.point_tracker = 'p1'
                if self.var.point_tracker == 'p1'  and not self.var.move2Point == 0:
                    self.half_stance_1(p)
                    time.sleep(0.4)
                    if not kuka.hasError[0]:
                        self.var.point_tracker = 'init'
                self.var.isInitialSwing = False

            # full gait cycle
            else:
                # 2nd half stance
                if self.var.point_tracker == 'init' and not self.var.move2Point == 0:
                    self.half_stance_2(p)
                    time.sleep(0.5)
                    if not kuka.hasError[0]:
                        self.var.point_tracker = 'st_end'
                    else:
                        print('Err: moving 2nd half stance ')

                # full swing
                if self.var.point_tracker == 'st_end' and not self.var.move2Point == 0:
                    self.full_swing(p)
                    time.sleep(0.5)
                    if not kuka.hasError[0]:
                        self.var.point_tracker = 'p1'
                    else:
                        print('Err: moving full swing')

                # 1st half stance
                if self.var.point_tracker == 'p1' and not self.var.move2Point == 0:
                    self.half_stance_1(p)
                    time.sleep(0.5)
                    if not kuka.hasError[0]:
                        self.var.point_tracker = 'init'
                    else:
                        print('Err: moving 1st half stance')
                
    def set_point_orientations(self, P):
        if P == 1:
            p = P1(self.var)      
        elif P == 2:
            p = P2(self.var) 
        elif P == 3:
            p = P3(self.var)
        elif P == 4:
            p = P4(self.var)
        elif P == 5:
            p = P5(self.var)
        else :
            p = P6(self.var)
        
        P_ori = {}

        if kuka.isFinished[0]:
            

            kuka.send_command(f'setCartImpCtrl {self.var.xy_imp} {self.var.xy_imp} {self.var.z_imp} {5} {5} {5} {self.var.damp}')      
            # init swing midLow
            self.var.move2Point = 0
            self.move_2_XYZABC(p.init_sw_midLow)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: init_swing_mid_low    1/11', end='')
                time.sleep(0.4)
            P_ori['init_sw_midLow'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # init swing mid
            self.var.move2Point = 0
            self.move_2_XYZABC(p.init_sw_mid)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: init_swing_mid    2/11', end='')
                time.sleep(0.4)
            P_ori['init_sw_mid'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # init swing midUp
            self.var.move2Point = 0
            self.move_2_XYZABC(p.init_sw_midUp)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: init_swing_mid_up     3/11', end='')
                time.sleep(0.4)
            P_ori['init_sw_midUp'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # swing End
            self.var.move2Point = 0
            self.move_2_XYZABC(p.sw_end)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: swing end     4/11', end='')
                time.sleep(0.4)
            P_ori['init_sw_end'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # stance midUp
            self.var.move2Point = 0
            self.move_2_XYZABC(p.st_midUp)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: stance mid up     5/11', end='')
                time.sleep(0.4)
            P_ori['st_midUp'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # stance mid
            self.var.move2Point = 0
            self.move_2_XYZABC(p.st_mid)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: stance mid    6/11', end='')
                time.sleep(0.4)
            P_ori['st_mid'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()
            
            # stance midLow
            self.var.move2Point = 0
            self.move_2_XYZABC(p.st_midLow)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: stance mid low    7/11', end='')
                time.sleep(0.4)
            P_ori['st_midLow'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # stance end
            self.var.move2Point = 0
            self.move_2_XYZABC(p.st_end)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: stance end    8/11', end='')
                time.sleep(0.4)
            P_ori['st_end'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # swing midLow
            self.var.move2Point = 0
            self.move_2_XYZABC(p.sw_midLow)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: swing_mid_low     9/11', end='')
                time.sleep(0.4)
            P_ori['sw_midLow'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            # swing mid
            self.var.move2Point = 0
            self.move_2_XYZABC(p.sw_mid)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: swing_mid     10/11', end='')
                time.sleep(0.4)
            P_ori['sw_mid'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()
        
            # swing midUp
            self.var.move2Point = 0
            self.move_2_XYZABC(p.sw_midUp)
            time.sleep(1)
            self.setCompliance([1000,1000,2000,2,2,2])
            while self.var.move2Point == 0:
                print('\r Point: swing_midUp     11/11', end='')
                time.sleep(0.4)
            P_ori['sw_midUp'] = kuka.ToolPosition[0][3:]
            self.resetCompliance()

            self.var.move2Point = 0

            # save point orientations
            key = f'P{P}'
            values = P_ori
            save_data(key, values)
            saved_data_update(self.var)
            
            print('=============   ORIENTATIONS WERE SAVED SUCCESSFULY  ==============')



    
