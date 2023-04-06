#!/usr/bin/env python
# ========================================  
#      * Author: nipun.dhananjaya@gmail.com  
#      * Created: xx.08.2022  
# ======================================== 
import numpy as np

class P1():
    def __init__(self, var_):
        self.var = var_
        self.initP = self.__init_point()

        self.init_point = f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'
        self.init_sw_midLow = self.__get_initSwing_midLow_point()
        self.init_sw_mid = self.__get_initSwing_mid_point()
        self.init_sw_midUp = self.__get_initSwing_midUp_point()
        self.sw_end = self.__get_swingEnd_point()

        self.sw_midLow = self.__get_swing_midLow_point()
        self.sw_mid = self.__get_swing_mid_point()
        self.sw_midUp = self.__get_swing_midUp_point()

        self.st_midLow = self.__get_stance_midLow_point()
        self.st_mid = self.__get_stance_mid_point()
        self.st_midUp = self.__get_stance_midUp_point()
        self.st_end = self.__get_stance_end_point()

    def __init_point(self):
        if self.var.cur_leg == 'left':
            return self.var.leftLeg_init_pos
        elif self.var.cur_leg == 'right':
            return self.var.rightLeg_init_pos

    # -------------------- stance points -------------------------------------------
    def __get_stance_midUp_point(self):
        st_midUp = np.zeros([6])
        st_midUp[0] = self.initP.x - self.var.dx/2
        st_midUp[1] = self.initP.y - self.var.dy/2
        st_midUp[2] = self.initP.z + self.var.dz
        st_midUp[3] = self.var.P1_ABC.st_midUp[0]
        st_midUp[4] = self.var.P1_ABC.st_midUp[1]
        st_midUp[5] = self.var.P1_ABC.st_midUp[2]
        return f'{st_midUp[0]} {st_midUp[1]} {st_midUp[2]} {st_midUp[3]} {st_midUp[4]} {st_midUp[5]}'

    def __get_stance_mid_point(self):
        return f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'

    def __get_stance_midLow_point(self):
        st_midLow = np.zeros([6])
        st_midLow[0] = self.initP.x + self.var.dx/2*0.8
        st_midLow[1] = self.initP.y - self.var.dy/2*0.8
        st_midLow[2] = self.initP.z - self.var.dz*0.8
        st_midLow[3] = self.var.P1_ABC.st_midLow[0]
        st_midLow[4] = self.var.P1_ABC.st_midLow[1]
        st_midLow[5] = self.var.P1_ABC.st_midLow[2]
        return f'{st_midLow[0]} {st_midLow[1]} {st_midLow[2]} {st_midLow[3]} {st_midLow[4]} {st_midLow[5]}'

    def __get_stance_end_point(self):
        st_end = np.zeros([6])
        st_end[0] = self.initP.x + self.var.dx*0.8
        st_end[1] = self.initP.y - self.var.dy*0.8
        st_end[2] = self.initP.z - 2*self.var.dz*0.8
        st_end[3] = self.var.P1_ABC.st_end[0]
        st_end[4] = self.var.P1_ABC.st_end[1]
        st_end[5] = self.var.P1_ABC.st_end[2]
        return f'{st_end[0]} {st_end[1]} {st_end[2]} {st_end[3]} {st_end[4]} {st_end[5]}'

    # -------------------- init swing points -------------------------------------------
    def __get_initSwing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x - self.var.dx/4
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z + 2/4*self.var.dz
        sw_midLow[3] = self.var.P1_ABC.initSW_midLow[0]
        sw_midLow[4] = self.var.P1_ABC.initSW_midLow[1]
        sw_midLow[5] = self.var.P1_ABC.initSW_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_initSwing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x - self.var.dx/2
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z + self.var.dz
        sw_mid[3] = self.var.P1_ABC.initSW_mid[0]
        sw_mid[4] = self.var.P1_ABC.initSW_mid[1]
        sw_mid[5] = self.var.P1_ABC.initSW_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_initSwing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x - self.var.dx*3/4
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz * 3/2
        sw_midUp[3] = self.var.P1_ABC.initSW_midUp[0]
        sw_midUp[4] = self.var.P1_ABC.initSW_midUp[1]
        sw_midUp[5] = self.var.P1_ABC.initSW_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

    def __get_swingEnd_point(self):
        sw_end = np.zeros([6])
        sw_end[0] = self.initP.x - self.var.dx
        sw_end[1] = self.initP.y - self.var.dy
        sw_end[2] = self.initP.z + 2*self.var.dz
        sw_end[3] = self.var.P1_ABC.sw_end[0]
        sw_end[4] = self.var.P1_ABC.sw_end[1]
        sw_end[5] = self.var.P1_ABC.sw_end[2]
        return f'{sw_end[0]} {sw_end[1]} {sw_end[2]} {sw_end[3]} {sw_end[4]} {sw_end[5]}'

    # -------------------- main swing points -------------------------------------------
    def __get_swing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x + self.var.dx/2*0.8
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z - self.var.dz*0.8
        sw_midLow[3] = self.var.P1_ABC.sw_midLow[0]
        sw_midLow[4] = self.var.P1_ABC.sw_midLow[1]
        sw_midLow[5] = self.var.P1_ABC.sw_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_swing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z 
        sw_mid[3] = self.var.P1_ABC.sw_mid[0]
        sw_mid[4] = self.var.P1_ABC.sw_mid[1]
        sw_mid[5] = self.var.P1_ABC.sw_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_swing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x - self.var.dx/2
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz
        sw_midUp[3] = self.var.P1_ABC.sw_midUp[0]
        sw_midUp[4] = self.var.P1_ABC.sw_midUp[1]
        sw_midUp[5] = self.var.P1_ABC.sw_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'


class P2():
    def __init__(self, var_):
        self.var = var_
        self.initP = self.__init_point()

        self.init_point = f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'
        self.init_sw_midLow = self.__get_initSwing_midLow_point()
        self.init_sw_mid = self.__get_initSwing_mid_point()
        self.init_sw_midUp = self.__get_initSwing_midUp_point()
        self.sw_end = self.__get_swingEnd_point()

        self.sw_midLow = self.__get_swing_midLow_point()
        self.sw_mid = self.__get_swing_mid_point()
        self.sw_midUp = self.__get_swing_midUp_point()

        self.st_midLow = self.__get_stance_midLow_point()
        self.st_mid = self.__get_stance_mid_point()
        self.st_midUp = self.__get_stance_midUp_point()
        self.st_end = self.__get_stance_end_point()

    def __init_point(self):
        if self.var.cur_leg == 'left':
            return self.var.leftLeg_init_pos
        elif self.var.cur_leg == 'right':
            return self.var.rightLeg_init_pos

    # -------------------- stance points -------------------------------------------
    def __get_stance_midUp_point(self):
        st_midUp = np.zeros([6])
        st_midUp[0] = self.initP.x 
        st_midUp[1] = self.initP.y - self.var.dy/2
        st_midUp[2] = self.initP.z + self.var.dz
        st_midUp[3] = self.var.P2_ABC.st_midUp[0]
        st_midUp[4] = self.var.P2_ABC.st_midUp[1]
        st_midUp[5] = self.var.P2_ABC.st_midUp[2]
        return f'{st_midUp[0]} {st_midUp[1]} {st_midUp[2]} {st_midUp[3]} {st_midUp[4]} {st_midUp[5]}'

    def __get_stance_mid_point(self):
        return f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'

    def __get_stance_midLow_point(self):
        st_midLow = np.zeros([6])
        st_midLow[0] = self.initP.x 
        st_midLow[1] = self.initP.y - self.var.dy/2*0.8
        st_midLow[2] = self.initP.z - self.var.dz*0.8
        st_midLow[3] = self.var.P2_ABC.st_midLow[0]
        st_midLow[4] = self.var.P2_ABC.st_midLow[1]
        st_midLow[5] = self.var.P2_ABC.st_midLow[2]
        return f'{st_midLow[0]} {st_midLow[1]} {st_midLow[2]} {st_midLow[3]} {st_midLow[4]} {st_midLow[5]}'

    def __get_stance_end_point(self):
        st_end = np.zeros([6])
        st_end[0] = self.initP.x 
        st_end[1] = self.initP.y - self.var.dy*0.8
        st_end[2] = self.initP.z - 2*self.var.dz*0.8
        st_end[3] = self.var.P2_ABC.st_end[0]
        st_end[4] = self.var.P2_ABC.st_end[1]
        st_end[5] = self.var.P2_ABC.st_end[2]
        return f'{st_end[0]} {st_end[1]} {st_end[2]} {st_end[3]} {st_end[4]} {st_end[5]}'

    # -------------------- init swing points -------------------------------------------
    def __get_initSwing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x 
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z + 2/4*self.var.dz
        sw_midLow[3] = self.var.P2_ABC.initSW_midLow[0]
        sw_midLow[4] = self.var.P2_ABC.initSW_midLow[1]
        sw_midLow[5] = self.var.P2_ABC.initSW_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_initSwing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z + self.var.dz
        sw_mid[3] = self.var.P2_ABC.initSW_mid[0]
        sw_mid[4] = self.var.P2_ABC.initSW_mid[1]
        sw_mid[5] = self.var.P2_ABC.initSW_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_initSwing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x 
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz * 3/2
        sw_midUp[3] = self.var.P2_ABC.initSW_midUp[0]
        sw_midUp[4] = self.var.P2_ABC.initSW_midUp[1]
        sw_midUp[5] = self.var.P2_ABC.initSW_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

    def __get_swingEnd_point(self):
        sw_end = np.zeros([6])
        sw_end[0] = self.initP.x 
        sw_end[1] = self.initP.y - self.var.dy
        sw_end[2] = self.initP.z + 2*self.var.dz
        sw_end[3] = self.var.P2_ABC.sw_end[0]
        sw_end[4] = self.var.P2_ABC.sw_end[1]
        sw_end[5] = self.var.P2_ABC.sw_end[2]
        return f'{sw_end[0]} {sw_end[1]} {sw_end[2]} {sw_end[3]} {sw_end[4]} {sw_end[5]}'

    # -------------------- swing points -------------------------------------------
    def __get_swing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x 
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z - self.var.dz*0.8
        sw_midLow[3] = self.var.P2_ABC.sw_midLow[0]
        sw_midLow[4] = self.var.P2_ABC.sw_midLow[1]
        sw_midLow[5] = self.var.P2_ABC.sw_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_swing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z 
        sw_mid[3] = self.var.P2_ABC.sw_mid[0]
        sw_mid[4] = self.var.P2_ABC.sw_mid[1]
        sw_mid[5] = self.var.P2_ABC.sw_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_swing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x 
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz
        sw_midUp[3] = self.var.P2_ABC.sw_midUp[0]
        sw_midUp[4] = self.var.P2_ABC.sw_midUp[1]
        sw_midUp[5] = self.var.P2_ABC.sw_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'



class P3():
    def __init__(self, var_):
        self.var = var_
        self.initP = self.__init_point()

        self.init_point = f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'
        self.init_sw_midLow = self.__get_initSwing_midLow_point()
        self.init_sw_mid = self.__get_initSwing_mid_point()
        self.init_sw_midUp = self.__get_initSwing_midUp_point()
        self.sw_end = self.__get_swingEnd_point()

        self.sw_midLow = self.__get_swing_midLow_point()
        self.sw_mid = self.__get_swing_mid_point()
        self.sw_midUp = self.__get_swing_midUp_point()

        self.st_midLow = self.__get_stance_midLow_point()
        self.st_mid = self.__get_stance_mid_point()
        self.st_midUp = self.__get_stance_midUp_point()
        self.st_end = self.__get_stance_end_point()

    def __init_point(self):
        if self.var.cur_leg == 'left':
            return self.var.leftLeg_init_pos
        elif self.var.cur_leg == 'right':
            return self.var.rightLeg_init_pos

    # -------------------- stance points -------------------------------------------
    def __get_stance_midUp_point(self):
        st_midUp = np.zeros([6])
        st_midUp[0] = self.initP.x + self.var.dx/2
        st_midUp[1] = self.initP.y - self.var.dy/2
        st_midUp[2] = self.initP.z + self.var.dz
        st_midUp[3] = self.var.P3_ABC.st_midUp[0]
        st_midUp[4] = self.var.P3_ABC.st_midUp[1]
        st_midUp[5] = self.var.P3_ABC.st_midUp[2]
        return f'{st_midUp[0]} {st_midUp[1]} {st_midUp[2]} {st_midUp[3]} {st_midUp[4]} {st_midUp[5]}'

    def __get_stance_mid_point(self):
        return f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'

    def __get_stance_midLow_point(self):
        st_midLow = np.zeros([6])
        st_midLow[0] = self.initP.x - self.var.dx/2*0.8
        st_midLow[1] = self.initP.y - self.var.dy/2*0.8
        st_midLow[2] = self.initP.z - self.var.dz*0.8
        st_midLow[3] = self.var.P3_ABC.st_midLow[0]
        st_midLow[4] = self.var.P3_ABC.st_midLow[1]
        st_midLow[5] = self.var.P3_ABC.st_midLow[2]
        return f'{st_midLow[0]} {st_midLow[1]} {st_midLow[2]} {st_midLow[3]} {st_midLow[4]} {st_midLow[5]}'

    def __get_stance_end_point(self):
        st_end = np.zeros([6])
        st_end[0] = self.initP.x - self.var.dx*0.8
        st_end[1] = self.initP.y - self.var.dy*0.8
        st_end[2] = self.initP.z - 2*self.var.dz*0.8
        st_end[3] = self.var.P3_ABC.st_end[0]
        st_end[4] = self.var.P3_ABC.st_end[1]
        st_end[5] = self.var.P3_ABC.st_end[2]
        return f'{st_end[0]} {st_end[1]} {st_end[2]} {st_end[3]} {st_end[4]} {st_end[5]}'

    # -------------------- init swing points -------------------------------------------
    def __get_initSwing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x + self.var.dx/4
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z + 2/4*self.var.dz
        sw_midLow[3] = self.var.P3_ABC.initSW_midLow[0]
        sw_midLow[4] = self.var.P3_ABC.initSW_midLow[1]
        sw_midLow[5] = self.var.P3_ABC.initSW_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_initSwing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x + self.var.dx/2
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z + self.var.dz
        sw_mid[3] = self.var.P3_ABC.initSW_mid[0]
        sw_mid[4] = self.var.P3_ABC.initSW_mid[1]
        sw_mid[5] = self.var.P3_ABC.initSW_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_initSwing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x + self.var.dx*3/4
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz * 3/2
        sw_midUp[3] = self.var.P3_ABC.initSW_midUp[0]
        sw_midUp[4] = self.var.P3_ABC.initSW_midUp[1]
        sw_midUp[5] = self.var.P3_ABC.initSW_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

    def __get_swingEnd_point(self):
        sw_end = np.zeros([6])
        sw_end[0] = self.initP.x + self.var.dx
        sw_end[1] = self.initP.y - self.var.dy
        sw_end[2] = self.initP.z + 2*self.var.dz
        sw_end[3] = self.var.P3_ABC.sw_end[0]
        sw_end[4] = self.var.P3_ABC.sw_end[1]
        sw_end[5] = self.var.P3_ABC.sw_end[2]
        return f'{sw_end[0]} {sw_end[1]} {sw_end[2]} {sw_end[3]} {sw_end[4]} {sw_end[5]}'

    # -------------------- main swing points -------------------------------------------
    def __get_swing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x - self.var.dx/2*0.8
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z - self.var.dz*0.8
        sw_midLow[3] = self.var.P3_ABC.sw_midLow[0]
        sw_midLow[4] = self.var.P3_ABC.sw_midLow[1]
        sw_midLow[5] = self.var.P3_ABC.sw_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_swing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z 
        sw_mid[3] = self.var.P3_ABC.sw_mid[0]
        sw_mid[4] = self.var.P3_ABC.sw_mid[1]
        sw_mid[5] = self.var.P3_ABC.sw_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_swing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x + self.var.dx/2
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz
        sw_midUp[3] = self.var.P3_ABC.sw_midUp[0]
        sw_midUp[4] = self.var.P3_ABC.sw_midUp[1]
        sw_midUp[5] = self.var.P3_ABC.sw_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

class P4():
    def __init__(self, var_):
        self.var = var_
        self.initP = self.__init_point()

        self.init_point = f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'
        self.init_sw_midLow = self.__get_initSwing_midLow_point()
        self.init_sw_mid = self.__get_initSwing_mid_point()
        self.init_sw_midUp = self.__get_initSwing_midUp_point()
        self.sw_end = self.__get_swingEnd_point()

        self.sw_midLow = self.__get_swing_midLow_point()
        self.sw_mid = self.__get_swing_mid_point()
        self.sw_midUp = self.__get_swing_midUp_point()

        self.st_midLow = self.__get_stance_midLow_point()
        self.st_mid = self.__get_stance_mid_point()
        self.st_midUp = self.__get_stance_midUp_point()
        self.st_end = self.__get_stance_end_point()

    def __init_point(self):
        if self.var.cur_leg == 'left':
            return self.var.leftLeg_init_pos
        elif self.var.cur_leg == 'right':
            return self.var.rightLeg_init_pos

    # -------------------- stance points -------------------------------------------
    def __get_stance_midUp_point(self):
        st_midUp = np.zeros([6])
        st_midUp[0] = self.initP.x - self.var.dx/2
        st_midUp[1] = self.initP.y - self.var.dy/2
        st_midUp[2] = self.initP.z + self.var.dz/2
        st_midUp[3] = self.var.P4_ABC.st_midUp[0]
        st_midUp[4] = self.var.P4_ABC.st_midUp[1]
        st_midUp[5] = self.var.P4_ABC.st_midUp[2]
        return f'{st_midUp[0]} {st_midUp[1]} {st_midUp[2]} {st_midUp[3]} {st_midUp[4]} {st_midUp[5]}'

    def __get_stance_mid_point(self):
        return f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'

    def __get_stance_midLow_point(self):
        st_midLow = np.zeros([6])
        st_midLow[0] = self.initP.x + self.var.dx/2*0.8
        st_midLow[1] = self.initP.y - self.var.dy/2*0.8
        st_midLow[2] = self.initP.z - self.var.dz*0.8/2
        st_midLow[3] = self.var.P4_ABC.st_midLow[0]
        st_midLow[4] = self.var.P4_ABC.st_midLow[1]
        st_midLow[5] = self.var.P4_ABC.st_midLow[2]
        return f'{st_midLow[0]} {st_midLow[1]} {st_midLow[2]} {st_midLow[3]} {st_midLow[4]} {st_midLow[5]}'

    def __get_stance_end_point(self):
        st_end = np.zeros([6])
        st_end[0] = self.initP.x + self.var.dx*0.8
        st_end[1] = self.initP.y - self.var.dy*0.8
        st_end[2] = self.initP.z - 2*self.var.dz*0.8/2
        st_end[3] = self.var.P4_ABC.st_end[0]
        st_end[4] = self.var.P4_ABC.st_end[1]
        st_end[5] = self.var.P4_ABC.st_end[2]
        return f'{st_end[0]} {st_end[1]} {st_end[2]} {st_end[3]} {st_end[4]} {st_end[5]}'

    # -------------------- init swing points -------------------------------------------
    def __get_initSwing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x - self.var.dx/4
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z + self.var.dz/4
        sw_midLow[3] = self.var.P4_ABC.sw_midLow[0]
        sw_midLow[4] = self.var.P4_ABC.sw_midLow[1]
        sw_midLow[5] = self.var.P4_ABC.sw_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_initSwing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x - self.var.dx/2
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z + self.var.dz/2
        sw_mid[3] = self.var.P4_ABC.initSW_mid[0]
        sw_mid[4] = self.var.P4_ABC.initSW_mid[1]
        sw_mid[5] = self.var.P4_ABC.initSW_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_initSwing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x - self.var.dx*3/4
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz * 3/2/2
        sw_midUp[3] = self.var.P4_ABC.initSW_midUp[0]
        sw_midUp[4] = self.var.P4_ABC.initSW_midUp[1]
        sw_midUp[5] = self.var.P4_ABC.initSW_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

    def __get_swingEnd_point(self):
        sw_end = np.zeros([6])
        sw_end[0] = self.initP.x - self.var.dx
        sw_end[1] = self.initP.y - self.var.dy
        sw_end[2] = self.initP.z + 2*self.var.dz/2
        sw_end[3] = self.var.P4_ABC.sw_end[0]
        sw_end[4] = self.var.P4_ABC.sw_end[1]
        sw_end[5] = self.var.P4_ABC.sw_end[2]
        return f'{sw_end[0]} {sw_end[1]} {sw_end[2]} {sw_end[3]} {sw_end[4]} {sw_end[5]}'

    # -------------------- main swing points -------------------------------------------
    def __get_swing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x + self.var.dx/2*0.8
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z - self.var.dz*0.8/2
        sw_midLow[3] = self.var.P4_ABC.sw_midLow[0]
        sw_midLow[4] = self.var.P4_ABC.sw_midLow[1]
        sw_midLow[5] = self.var.P4_ABC.sw_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_swing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z 
        sw_mid[3] = self.var.P4_ABC.sw_mid[0]
        sw_mid[4] = self.var.P4_ABC.sw_mid[1]
        sw_mid[5] = self.var.P4_ABC.sw_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_swing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x - self.var.dx/2
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz/2
        sw_midUp[3] = self.var.P4_ABC.sw_midUp[0]
        sw_midUp[4] = self.var.P4_ABC.sw_midUp[1]
        sw_midUp[5] = self.var.P4_ABC.sw_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'


class P5():
    def __init__(self, var_):
        self.var = var_
        self.initP = self.__init_point()

        self.init_point = f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'
        self.init_sw_midLow = self.__get_initSwing_midLow_point()
        self.init_sw_mid = self.__get_initSwing_mid_point()
        self.init_sw_midUp = self.__get_initSwing_midUp_point()
        self.sw_end = self.__get_swingEnd_point()

        self.sw_midLow = self.__get_swing_midLow_point()
        self.sw_mid = self.__get_swing_mid_point()
        self.sw_midUp = self.__get_swing_midUp_point()

        self.st_midLow = self.__get_stance_midLow_point()
        self.st_mid = self.__get_stance_mid_point()
        self.st_midUp = self.__get_stance_midUp_point()
        self.st_end = self.__get_stance_end_point()

    def __init_point(self):
        if self.var.cur_leg == 'left':
            return self.var.leftLeg_init_pos
        elif self.var.cur_leg == 'right':
            return self.var.rightLeg_init_pos

    # -------------------- stance points -------------------------------------------
    def __get_stance_midUp_point(self):
        st_midUp = np.zeros([6])
        st_midUp[0] = self.initP.x 
        st_midUp[1] = self.initP.y - self.var.dy/2
        st_midUp[2] = self.initP.z + self.var.dz/2
        st_midUp[3] = self.var.P5_ABC.st_midUp[0]
        st_midUp[4] = self.var.P5_ABC.st_midUp[1]
        st_midUp[5] = self.var.P5_ABC.st_midUp[2]
        return f'{st_midUp[0]} {st_midUp[1]} {st_midUp[2]} {st_midUp[3]} {st_midUp[4]} {st_midUp[5]}'

    def __get_stance_mid_point(self):
        return f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'

    def __get_stance_midLow_point(self):
        st_midLow = np.zeros([6])
        st_midLow[0] = self.initP.x 
        st_midLow[1] = self.initP.y - self.var.dy/2*0.8
        st_midLow[2] = self.initP.z - self.var.dz*0.8/2
        st_midLow[3] = self.var.P5_ABC.st_midLow[0]
        st_midLow[4] = self.var.P5_ABC.st_midLow[1]
        st_midLow[5] = self.var.P5_ABC.st_midLow[2]
        return f'{st_midLow[0]} {st_midLow[1]} {st_midLow[2]} {st_midLow[3]} {st_midLow[4]} {st_midLow[5]}'

    def __get_stance_end_point(self):
        st_end = np.zeros([6])
        st_end[0] = self.initP.x 
        st_end[1] = self.initP.y - self.var.dy*0.8
        st_end[2] = self.initP.z - 2*self.var.dz*0.8/2
        st_end[3] = self.var.P5_ABC.st_end[0]
        st_end[4] = self.var.P5_ABC.st_end[1]
        st_end[5] = self.var.P5_ABC.st_end[2]
        return f'{st_end[0]} {st_end[1]} {st_end[2]} {st_end[3]} {st_end[4]} {st_end[5]}'

    # -------------------- init swing points -------------------------------------------
    def __get_initSwing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x 
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z + self.var.dz/4
        sw_midLow[3] = self.var.P5_ABC.initSW_midLow[0]
        sw_midLow[4] = self.var.P5_ABC.initSW_midLow[1]
        sw_midLow[5] = self.var.P5_ABC.initSW_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_initSwing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z + self.var.dz/2
        sw_mid[3] = self.var.P5_ABC.initSW_mid[0]
        sw_mid[4] = self.var.P5_ABC.initSW_mid[1]
        sw_mid[5] = self.var.P5_ABC.initSW_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_initSwing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz * 3/2/2
        sw_midUp[3] = self.var.P5_ABC.initSW_midUp[0]
        sw_midUp[4] = self.var.P5_ABC.initSW_midUp[1]
        sw_midUp[5] = self.var.P5_ABC.initSW_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

    def __get_swingEnd_point(self):
        sw_end = np.zeros([6])
        sw_end[0] = self.initP.x 
        sw_end[1] = self.initP.y - self.var.dy
        sw_end[2] = self.initP.z + 2*self.var.dz/2
        sw_end[3] = self.var.P5_ABC.sw_end[0]
        sw_end[4] = self.var.P5_ABC.sw_end[1]
        sw_end[5] = self.var.P5_ABC.sw_end[2]
        return f'{sw_end[0]} {sw_end[1]} {sw_end[2]} {sw_end[3]} {sw_end[4]} {sw_end[5]}'

    # -------------------- main swing points -------------------------------------------
    def __get_swing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x 
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z - self.var.dz*0.8/2
        sw_midLow[3] = self.var.P5_ABC.sw_midLow[0]
        sw_midLow[4] = self.var.P5_ABC.sw_midLow[1]
        sw_midLow[5] = self.var.P5_ABC.sw_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_swing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z 
        sw_mid[3] = self.var.P5_ABC.sw_mid[0]
        sw_mid[4] = self.var.P5_ABC.sw_mid[1]
        sw_mid[5] = self.var.P5_ABC.sw_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_swing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x 
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz/2
        sw_midUp[3] = self.var.P5_ABC.sw_midUp[0]
        sw_midUp[4] = self.var.P5_ABC.sw_midUp[1]
        sw_midUp[5] = self.var.P5_ABC.sw_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

class P6():
    def __init__(self, var_):
        self.var = var_
        self.initP = self.__init_point()

        self.init_point = f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'
        self.init_sw_midLow = self.__get_initSwing_midLow_point()
        self.init_sw_mid = self.__get_initSwing_mid_point()
        self.init_sw_midUp = self.__get_initSwing_midUp_point()
        self.sw_end = self.__get_swingEnd_point()

        self.sw_midLow = self.__get_swing_midLow_point()
        self.sw_mid = self.__get_swing_mid_point()
        self.sw_midUp = self.__get_swing_midUp_point()

        self.st_midLow = self.__get_stance_midLow_point()
        self.st_mid = self.__get_stance_mid_point()
        self.st_midUp = self.__get_stance_midUp_point()
        self.st_end = self.__get_stance_end_point()

    def __init_point(self):
        if self.var.cur_leg == 'left':
            return self.var.leftLeg_init_pos
        elif self.var.cur_leg == 'right':
            return self.var.rightLeg_init_pos

    # -------------------- stance points -------------------------------------------
    def __get_stance_midUp_point(self):
        st_midUp = np.zeros([6])
        st_midUp[0] = self.initP.x + self.var.dx/2
        st_midUp[1] = self.initP.y - self.var.dy/2
        st_midUp[2] = self.initP.z + self.var.dz/2
        st_midUp[3] = self.var.P6_ABC.st_midUp[0]
        st_midUp[4] = self.var.P6_ABC.st_midUp[1]
        st_midUp[5] = self.var.P6_ABC.st_midUp[2]
        return f'{st_midUp[0]} {st_midUp[1]} {st_midUp[2]} {st_midUp[3]} {st_midUp[4]} {st_midUp[5]}'

    def __get_stance_mid_point(self):
        return f'{self.initP.x} {self.initP.y} {self.initP.z} {self.initP.a} {self.initP.b} {self.initP.c}'

    def __get_stance_midLow_point(self):
        st_midLow = np.zeros([6])
        st_midLow[0] = self.initP.x - self.var.dx/2*0.8
        st_midLow[1] = self.initP.y - self.var.dy/2*0.8
        st_midLow[2] = self.initP.z - self.var.dz*0.8/2
        st_midLow[3] = self.var.P6_ABC.st_midLow[0]
        st_midLow[4] = self.var.P6_ABC.st_midLow[1]
        st_midLow[5] = self.var.P6_ABC.st_midLow[2]
        return f'{st_midLow[0]} {st_midLow[1]} {st_midLow[2]} {st_midLow[3]} {st_midLow[4]} {st_midLow[5]}'

    def __get_stance_end_point(self):
        st_end = np.zeros([6])
        st_end[0] = self.initP.x - self.var.dx*0.8
        st_end[1] = self.initP.y - self.var.dy*0.8
        st_end[2] = self.initP.z - 2*self.var.dz*0.8/2
        st_end[3] = self.var.P6_ABC.st_end[0]
        st_end[4] = self.var.P6_ABC.st_end[1]
        st_end[5] = self.var.P6_ABC.st_end[2]
        return f'{st_end[0]} {st_end[1]} {st_end[2]} {st_end[3]} {st_end[4]} {st_end[5]}'

    # -------------------- init swing points -------------------------------------------
    def __get_initSwing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x + self.var.dx/4
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z + self.var.dz/4
        sw_midLow[3] = self.var.P6_ABC.initSW_midLow[0]
        sw_midLow[4] = self.var.P6_ABC.initSW_midLow[1]
        sw_midLow[5] = self.var.P6_ABC.initSW_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_initSwing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x + self.var.dx/2
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z + self.var.dz/2
        sw_mid[3] = self.var.P6_ABC.initSW_mid[0]
        sw_mid[4] = self.var.P6_ABC.initSW_mid[1]
        sw_mid[5] = self.var.P6_ABC.initSW_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_initSwing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x + self.var.dx*3/4
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz * 3/2/2
        sw_midUp[3] = self.var.P6_ABC.initSW_midUp[0]
        sw_midUp[4] = self.var.P6_ABC.initSW_midUp[1]
        sw_midUp[5] = self.var.P6_ABC.initSW_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'

    def __get_swingEnd_point(self):
        sw_end = np.zeros([6])
        sw_end[0] = self.initP.x + self.var.dx
        sw_end[1] = self.initP.y - self.var.dy
        sw_end[2] = self.initP.z + 2*self.var.dz/2
        sw_end[3] = self.var.P6_ABC.sw_end[0]
        sw_end[4] = self.var.P6_ABC.sw_end[1]
        sw_end[5] = self.var.P6_ABC.sw_end[2]
        return f'{sw_end[0]} {sw_end[1]} {sw_end[2]} {sw_end[3]} {sw_end[4]} {sw_end[5]}'

    # -------------------- main swing points -------------------------------------------
    def __get_swing_midLow_point(self):
        sw_midLow = np.zeros([6])
        sw_midLow[0] = self.initP.x - self.var.dx/2*0.8
        sw_midLow[1] = self.initP.y - self.var.step_h*0.8
        sw_midLow[2] = self.initP.z - self.var.dz*0.8/2
        sw_midLow[3] = self.var.P6_ABC.sw_midLow[0]
        sw_midLow[4] = self.var.P6_ABC.sw_midLow[1]
        sw_midLow[5] = self.var.P6_ABC.sw_midLow[2]
        return f'{sw_midLow[0]} {sw_midLow[1]} {sw_midLow[2]} {sw_midLow[3]} {sw_midLow[4]} {sw_midLow[5]}'

    def __get_swing_mid_point(self):
        sw_mid = np.zeros([6])
        sw_mid[0] = self.initP.x 
        sw_mid[1] = self.initP.y - self.var.step_h
        sw_mid[2] = self.initP.z 
        sw_mid[3] = self.var.P6_ABC.sw_mid[0]
        sw_mid[4] = self.var.P6_ABC.sw_mid[1]
        sw_mid[5] = self.var.P6_ABC.sw_mid[2]
        return f'{sw_mid[0]} {sw_mid[1]} {sw_mid[2]} {sw_mid[3]} {sw_mid[4]} {sw_mid[5]}'

    def __get_swing_midUp_point(self):
        sw_midUp = np.zeros([6])
        sw_midUp[0] = self.initP.x + self.var.dx/2
        sw_midUp[1] = self.initP.y - self.var.step_h*0.8
        sw_midUp[2] = self.initP.z + self.var.dz/2
        sw_midUp[3] = self.var.P6_ABC.sw_midUp[0]
        sw_midUp[4] = self.var.P6_ABC.sw_midUp[1]
        sw_midUp[5] = self.var.P6_ABC.sw_midUp[2]
        return f'{sw_midUp[0]} {sw_midUp[1]} {sw_midUp[2]} {sw_midUp[3]} {sw_midUp[4]} {sw_midUp[5]}'
