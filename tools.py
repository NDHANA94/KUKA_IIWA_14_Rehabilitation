#!/usr/bin/env python

import json
# ========================================  
#      * Author: nipun.dhananjaya@gmail.com  
#      * Created: xx.08.2022  
# ======================================== 


# ============= Control parameters ==============================
class VARIABLES():                                             #|
    def __init__(self):    
        self.start = False  
                                          #|                        
        self.tool = 'tool1'                                    #|
                                                               #|
        self.j_vel = 0.1                                       #|
        self.j_acc = 0.1                                       #|
        self.j_jrk = 0.1                                       #|
                                                               #|
        self.xy_imp = 600                                      #|
        self.z_imp = 1000                                      #|
        self.abc_imp = 200                                     #|
        self.damp = 1                                          #|
                                                               #|
        self.j1 = 0                                            #|
        self.j2 = 50                                           #|
        self.j3 = 0                                            #|
        self.j4 = -50                                          #|
        self.j5 = 0                                            #|
        self.j6 = 82                                           #|
        self.j7 = 45                                           #|
                                                               #|
        self.default_position = self.XYZABC()                  #|
        self.leftLeg_init_pos = self.XYZABC()                  #|
        self.rightLeg_init_pos = self.XYZABC()                 #|
                                                               #|
        self.xy_compliant = 1                                  #|
        self.z_compliant = 5                                   #|
        self.abc_compliant = 1                                 #|
                                                               #|
        self.selectedLeg = 'left'                              #|
        self.moveMode = 'ptp'                                  #|
                                                               #|
        self.gaitMode = False                                  #|
        self.step_h = 200                                      #|
        self.blendingOri = 8                                   #|
        self.dx = 80                                           #|
        self.dy = 20                                           #|
        self.dz = 100                                          #|
        self.gaitSpd = 80                                      #|
        self.cur_leg = 'left'                                  #|
        self.isCycleFinished = False                            #|
        self.isInitialSwing = True
        self.isInitialStance = True
        self.isSwingFinished = False
        self.isStanceFinished = False
        self.move2Point = 0    
        self.point_tracker = 'init'                            #|
                                                               #|
        self.setPointOrientation = False

        self.close = False                                     #|

        self.P1_ABC = self.ABC()
        self.P2_ABC = self.ABC()
        self.P3_ABC = self.ABC()
        self.P4_ABC = self.ABC()
        self.P5_ABC = self.ABC()
        self.P6_ABC = self.ABC()

    class ABC():
        def __init__ (self):
            self.initSW_midLow = [140, 0, -179]
            self.initSW_mid = [140, 0, -179]
            self.initSW_midUp = [140, 0, -179]
            self.sw_end = [140, 0, -179]
            self.st_midUp = [140, 0, -179]
            self.st_mid = [140, 0, -179]
            self.st_midLow = [140, 0, -179]
            self.st_end = [140, 0, -179]
            self.sw_midLow = [140, 0, -179]
            self.sw_mid = [140, 0, -179]
            self.sw_midUp = [140, 0, -179]


                                                               #|
    class XYZABC():                                            #|
        def __init__(self):                                    #|
            self.x = 600                                       #|
            self.y = 0                                         #|
            self.z = 0                                         #|
            self.a = 134                                       #|
            self.b = 6                                         #|
            self.c = -179                                      #|
# ===============================================================




# ===========================================================================================================================================================================================
# ================================================ KEYS ===============================================================================================================================
# ===========================================================================================================================================================================================

class KEYS():
    def __init__(self):
        self.but = self.__Buttons()
        self.slider = self.__Slider()
        self.disp = self.__Disp()
        self.radio = self.__Radio()
        self.checkBox = self.__CheckBox()
        self.spin = self.__Spin()
        self.input = self.__Input()
        

    class __Buttons():
        def __init__(self):
            self.connect = 'but_connect'
            self.set_tool = 'but_set_tool'
            self.set_imp = 'but_set_imp'
            self.set_zero_angs = 'but_set_zero_angs'
            self.set_angs = 'but_set_angs'
            self.move2defualtInitPos = 'but_move2defualtInitPos'
            self.freeMode = 'but_freeMode'
            self.setCurPos_as_legInitPos = 'but_setCurPos_as_legInitPos'
            self.saveKinParams = 'but_saveKin'
            self.saveImpParams = 'but_saveImp'
            self.saveAngs = 'but_saveAngs'
            self.saveXYZABC = 'but_saveXYZABC'
            self.saveFreeModeParams = 'but_saveFreeMode'
            self.saveGaitParams = 'but_saveGait'
            self.P1 = 'but_P1'
            self.P2 = 'but_P2'
            self.P3 = 'but_P3'
            self.P4 = 'but_P4'
            self.P5 = 'but_P5'
            self.P6 = 'but_P6'
            self.Move2LegInit = 'but_move2legInit'
            
    
    class __Slider():
        def __init__(self):
            self.j_vel = 'Sl_Jvel'
            self.j_acc = 'Sl_Jacc'
            self.j_jrk = 'Sl_Jjrk'
            self.xyImp = 'Sl_xyImp'
            self.zImp = 'Sl_zImp'
            self.abcImp = 'Sl_abcImp'
            self.damp = 'Sl_damp'
            self.J1 = 'Sl_j1'
            self.J2 = 'Sl_j2'
            self.J3 = 'Sl_j3'
            self.J4 = 'Sl_j4'
            self.J5 = 'Sl_j5'
            self.J6 = 'Sl_j6'
            self.J7 = 'Sl_j7'
            self.X = 'Sl_x'
            self.Y = 'Sl_y'
            self.Z = 'Sl_z'
            self.A = 'Sl_a'
            self.B = 'Sl_b'
            self.C = 'Sl_c'
            self.xyCompliant = 'Sl_xyComp'
            self.zCompliant = 'Sl_zComp'
            self.abcCompliant = 'Sl_abcComp'
            self.step_h = 'Sl_stepH'
            self.dx = 'Sl_dx'
            self.dy = 'Sl_dy'
            self.dz = 'Sl_dz'
            self.gaitSpd = 'Sl_speed'

    class __Disp():
        def __init__(self):
            self.j_vel = 'Dsp_Jvel'
            self.j_acc = 'Dsp_Jacc'
            self.j_jrk = 'Dsp_Jjrk'
            self.xyImp = 'Dsp_xyImp'
            self.zImp = 'Dsp_zImp'
            self.abcImp = 'Dsp_abcImp'
            self.damp = 'Dsp_damp'
            self.J1 = 'Dsp_j1'
            self.J2 = 'Dsp_j2'
            self.J3 = 'Dsp_j3'
            self.J4 = 'Dsp_j4'
            self.J5 = 'Dsp_j5'
            self.J6 = 'Dsp_j6'
            self.J7 = 'Dsp_j7'
            self.X = 'Dsp_x'
            self.Y = 'Dsp_y'
            self.Z = 'Dsp_z'
            self.A = 'Dsp_a'
            self.B = 'Dsp_b'
            self.C = 'Dsp_c'
            self.xyCompliant = 'Dsp_xyComp'
            self.zCompliant = 'Dsp_zComp'
            self.abcCompliant = 'Dsp_abcComp'
            self.step_h = 'Dsp_stepH'
            self.dx = 'Dsp_dx'
            self.dy = 'Dsp_dy'
            self.dz = 'Dsp_dz'
            self.gaitSpd = 'Dsp_speed'
            self.nowX = 'Dsp_nowX'
            self.nowY = 'Dsp_nowY'
            self.nowZ = 'Dsp_nowZ'
            self.nowA = 'Dsp_nowA'
            self.nowB = 'Dsp_nowB'
            self.nowC = 'Dsp_nowC'
            self.nowJ1 = 'Dsp_nowJ1'
            self.nowJ2 = 'Dsp_nowJ2'
            self.nowJ3 = 'Dsp_nowJ3'
            self.nowJ4 = 'Dsp_nowJ4'
            self.nowJ5 = 'Dsp_nowJ5'
            self.nowJ6 = 'Dsp_nowJ6'
            self.nowJ7 = 'Dsp_nowJ7'
            self.setPointOri = 'Dsp_setOri'
            
    
    class __Radio():
        def __init__(self):
            self.leftLeg = 'rd_left'
            self.rightLeg = 'rd_right'
            self.ptp = 'rd_ptp'
            self.lin = 'rd_lin'
            self.arc = 'rd_arc'
    
    class __CheckBox():
        def __init__(self):
            self.gait = 'CB_gait'
            self.setPointOri = 'CB_setOri'

    class __Spin():
        def __init__(self):
            self.blend = 'Sp_blend'

    class __Input():
        def __init__(self):
            self.tool = 'In_tool'




def get_saved_data():
    try:
        f = open('data.json')
        data_file_ = json.load(f)
        return data_file_    
    except:
        print('No data file found!')
    
    
data_file = get_saved_data()




def save_data(key, values):
    
    data_file[key] = values
    with open('data.json', 'w') as f:
        json.dump(data_file, f)
    return 1

def saved_data_update(var):
    if data_file != None:
        if 'kin_params' in data_file.keys():
            var.j_vel = float(data_file['kin_params']['vel'])   if 'vel' in data_file['kin_params'] else print('No saved joint velocity data found!')
            var.j_acc = float(data_file['kin_params']['acc'])   if 'acc' in data_file['kin_params'] else print('No saved joint acceleration data found!')
            var.j_jrk = float(data_file['kin_params']['jerk'])  if 'jerk' in data_file['kin_params'] else print('No saved joint jerk data found!')
            

        if 'imp_params' in data_file.keys():
            var.xy_imp = int(data_file['imp_params']['xy'])     if 'xy' in data_file['imp_params'] else print('No saved xy impedence data found!')
            var.z_imp = int(data_file['imp_params']['z'])       if 'z' in data_file['imp_params'] else print('No saved z impedence data found!')
            var.abc_imp = int(data_file['imp_params']['abc'])   if 'abc' in data_file['imp_params'] else print('No saved abc impedence data found!')
            var.damp = float(data_file['imp_params']['damp'])     if 'damp' in data_file['imp_params'] else print('No saved damp ratio data found!')

        if 'joint_angs' in data_file.keys():
            var.j1 = int(data_file['joint_angs']['j1'])   if 'j1' in data_file['joint_angs'] else print('No saved j1 angle data found!')
            var.j2 = int(data_file['joint_angs']['j2'])   if 'j2' in data_file['joint_angs'] else print('No saved j2 angle data found!')
            var.j3 = int(data_file['joint_angs']['j3'])   if 'j3' in data_file['joint_angs'] else print('No saved j3 angle data found!')
            var.j4 = int(data_file['joint_angs']['j4'])   if 'j4' in data_file['joint_angs'] else print('No saved j4 angle data found!')
            var.j5 = int(data_file['joint_angs']['j5'])   if 'j5' in data_file['joint_angs'] else print('No saved j5 angle data found!')
            var.j6 = int(data_file['joint_angs']['j6'])   if 'j6' in data_file['joint_angs'] else print('No saved j6 angle data found!')
            var.j7 = int(data_file['joint_angs']['j7'])   if 'j7' in data_file['joint_angs'] else print('No saved j7 angle data found!')

        if 'XYZABC' in data_file.keys():
            var.default_position.x = int(data_file['XYZABC']['x'])    if 'x' in data_file['XYZABC'] else print('No saved x data found!')
            var.default_position.y = int(data_file['XYZABC']['y'])    if 'y' in data_file['XYZABC'] else print('No saved x data found!')
            var.default_position.z = int(data_file['XYZABC']['z'])    if 'z' in data_file['XYZABC'] else print('No saved x data found!')
            var.default_position.a = int(data_file['XYZABC']['a'])    if 'a' in data_file['XYZABC'] else print('No saved x data found!')
            var.default_position.b = int(data_file['XYZABC']['b'])    if 'b' in data_file['XYZABC'] else print('No saved x data found!')
            var.default_position.c = int(data_file['XYZABC']['c'])    if 'c' in data_file['XYZABC'] else print('No saved x data found!')

        if 'left' in data_file.keys():
            var.leftLeg_init_pos.x = float(data_file['left']['init_pos'][0])    if 'init_pos' in data_file['left'] else print('No saved left leg initial position [0] data found!')
            var.leftLeg_init_pos.y = float(data_file['left']['init_pos'][1])    if 'init_pos' in data_file['left'] else print('No saved left leg initial position [1] data found!')
            var.leftLeg_init_pos.z = float(data_file['left']['init_pos'][2])    if 'init_pos' in data_file['left'] else print('No saved left leg initial position [2] data found!')
            var.leftLeg_init_pos.a = float(data_file['left']['init_pos'][3])    if 'init_pos' in data_file['left'] else print('No saved left leg initial position [3] data found!')
            var.leftLeg_init_pos.b = float(data_file['left']['init_pos'][4])    if 'init_pos' in data_file['left'] else print('No saved left leg initial position [4] data found!')
            var.leftLeg_init_pos.c = float(data_file['left']['init_pos'][5])    if 'init_pos' in data_file['left'] else print('No saved left leg initial position [5] data found!')

        if 'right' in data_file.keys():
            var.rightLeg_init_pos.x = float(data_file['right']['init_pos'][0])  if 'init_pos' in data_file['right'] else print('No saved right leg initial position [0] data found!')
            var.rightLeg_init_pos.y = float(data_file['right']['init_pos'][1])  if 'init_pos' in data_file['right'] else print('No saved right leg initial position [1] data found!')
            var.rightLeg_init_pos.z = float(data_file['right']['init_pos'][2])  if 'init_pos' in data_file['right'] else print('No saved right leg initial position [2] data found!')
            var.rightLeg_init_pos.a = float(data_file['right']['init_pos'][3])  if 'init_pos' in data_file['right'] else print('No saved right leg initial position [3] data found!')
            var.rightLeg_init_pos.b = float(data_file['right']['init_pos'][4])  if 'init_pos' in data_file['right'] else print('No saved right leg initial position [4] data found!')
            var.rightLeg_init_pos.c = float(data_file['right']['init_pos'][5])  if 'init_pos' in data_file['right'] else print('No saved right leg initial position [5] data found!')

        if 'compliant' in data_file.keys():
            var.xy_compliant = int(data_file['compliant']['xy'])    if 'xy' in data_file['compliant'] else print('No saved xy compliant data found!')
            var.z_compliant = int(data_file['compliant']['z'])      if 'z' in data_file['compliant'] else print('No saved z compliant data found!')
            var.abc_compliant = int(data_file['compliant']['abc'])    if 'abc' in data_file['compliant'] else print('No saved abc compliant data found!')

        if 'locomotion' in data_file.keys():
            var.gait_speed = int(data_file['locomotion']['gait_spd'])   if 'gait_spd' in data_file['locomotion'] else print('No saved gait speed data found!')
            var.step_h = int(data_file['locomotion']['step_h'])         if 'step_h' in data_file['locomotion'] else print('No saved step_h data found!')
            var.blendingOri = data_file['locomotion']['blend']          if 'blend' in data_file['locomotion'] else print('No saved blend data found!')
            var.dx = int(data_file['locomotion']['dx'])                 if 'dx' in data_file['locomotion'] else print('No saved dx data found!')
            var.dy = int(data_file['locomotion']['dy'])                 if 'dy' in data_file['locomotion'] else print('No saved dy data found!')
            var.dz = int(data_file['locomotion']['dz'])                 if 'dz' in data_file['locomotion'] else print('No saved dz data found!')
        
        if 'P1' in data_file.keys():
            var.P1_ABC.initSW_midLow    =  data_file['P1']['init_sw_midLow']
            var.P1_ABC.initSW_mid       =  data_file['P1']['init_sw_mid']
            var.P1_ABC.initSW_midUp     = data_file['P1']['init_sw_midUp']
            var.P1_ABC.sw_end           = data_file['P1']['init_sw_end']
            var.P1_ABC.st_midUp         = data_file['P1']['st_midUp']
            var.P1_ABC.st_mid           = data_file['P1']['st_mid']
            var.P1_ABC.st_midLow        = data_file['P1']['st_midLow']
            var.P1_ABC.st_end           = data_file['P1']['st_end']
            var.P1_ABC.sw_midLow        = data_file['P1']['sw_midLow']
            var.P1_ABC.sw_mid           = data_file['P1']['sw_mid']
            var.P1_ABC.sw_midUp         = data_file['P1']['sw_midUp']

        if 'P2' in data_file.keys():
            var.P2_ABC.initSW_midLow    = data_file['P2']['init_sw_midLow']
            var.P2_ABC.initSW_mid       = data_file['P2']['init_sw_mid']
            var.P2_ABC.initSW_midUp     = data_file['P2']['init_sw_midUp']
            var.P2_ABC.sw_end           = data_file['P2']['init_sw_end']
            var.P2_ABC.st_midUp         = data_file['P2']['st_midUp']
            var.P2_ABC.st_mid           = data_file['P2']['st_mid']
            var.P2_ABC.st_midLow        = data_file['P2']['st_midLow']
            var.P2_ABC.st_end           = data_file['P2']['st_end']
            var.P2_ABC.sw_midLow        = data_file['P2']['sw_midLow']
            var.P2_ABC.sw_mid           = data_file['P2']['sw_mid']
            var.P2_ABC.sw_midUp         = data_file['P2']['sw_midUp']

        if 'P3' in data_file.keys():
            var.P3_ABC.initSW_midLow    = data_file['P3']['init_sw_midLow']
            var.P3_ABC.initSW_mid       = data_file['P3']['init_sw_mid']
            var.P3_ABC.initSW_midUp     = data_file['P3']['init_sw_midUp']
            var.P3_ABC.sw_end           = data_file['P3']['init_sw_end']
            var.P3_ABC.st_midUp         = data_file['P3']['st_midUp']
            var.P3_ABC.st_mid           = data_file['P3']['st_mid']
            var.P3_ABC.st_midLow        = data_file['P3']['st_midLow']
            var.P3_ABC.st_end           = data_file['P3']['st_end']
            var.P3_ABC.sw_midLow        = data_file['P3']['sw_midLow']
            var.P3_ABC.sw_mid           = data_file['P3']['sw_mid']
            var.P3_ABC.sw_midUp         = data_file['P3']['sw_midUp']

        if 'P4' in data_file.keys():
            var.P4_ABC.initSW_midLow    =  data_file['P4']['init_sw_midLow']
            var.P4_ABC.initSW_mid       =  data_file['P4']['init_sw_mid']
            var.P4_ABC.initSW_midUp     = data_file['P4']['init_sw_midUp']
            var.P4_ABC.sw_end           = data_file['P4']['init_sw_end']
            var.P4_ABC.st_midUp         = data_file['P4']['st_midUp']
            var.P4_ABC.st_mid           = data_file['P4']['st_mid']
            var.P4_ABC.st_midLow        = data_file['P4']['st_midLow']
            var.P4_ABC.st_end           = data_file['P4']['st_end']
            var.P4_ABC.sw_midLow        = data_file['P4']['sw_midLow']
            var.P4_ABC.sw_mid           = data_file['P4']['sw_mid']
            var.P4_ABC.sw_midUp         = data_file['P4']['sw_midUp']

        if 'P5' in data_file.keys():
            var.P5_ABC.initSW_midLow    = data_file['P5']['init_sw_midLow']
            var.P5_ABC.initSW_mid       = data_file['P5']['init_sw_mid']
            var.P5_ABC.initSW_midUp     = data_file['P5']['init_sw_midUp']
            var.P5_ABC.sw_end           = data_file['P5']['init_sw_end']
            var.P5_ABC.st_midUp         = data_file['P5']['st_midUp']
            var.P5_ABC.st_mid           = data_file['P5']['st_mid']
            var.P5_ABC.st_midLow        = data_file['P5']['st_midLow']
            var.P5_ABC.st_end           = data_file['P5']['st_end']
            var.P5_ABC.sw_midLow        = data_file['P5']['sw_midLow']
            var.P5_ABC.sw_mid           = data_file['P5']['sw_mid']
            var.P5_ABC.sw_midUp         = data_file['P5']['sw_midUp']

        if 'P6' in data_file.keys():
            var.P6_ABC.initSW_midLow    = data_file['P6']['init_sw_midLow']
            var.P6_ABC.initSW_mid       = data_file['P6']['init_sw_mid']
            var.P6_ABC.initSW_midUp     = data_file['P6']['init_sw_midUp']
            var.P6_ABC.sw_end           = data_file['P6']['init_sw_end']
            var.P6_ABC.st_midUp         = data_file['P6']['st_midUp']
            var.P6_ABC.st_mid           = data_file['P6']['st_mid']
            var.P6_ABC.st_midLow        = data_file['P6']['st_midLow']
            var.P6_ABC.st_end           = data_file['P6']['st_end']
            var.P6_ABC.sw_midLow        = data_file['P6']['sw_midLow']
            var.P6_ABC.sw_mid           = data_file['P6']['sw_mid']
            var.P6_ABC.sw_midUp         = data_file['P6']['sw_midUp']
        
    else:
        print('No Data File')


# ===========================================================================================================================================================================================
# ================================================ GUI LAYOUT ===============================================================================================================================
# ===========================================================================================================================================================================================
def rehab_gui_layout(sg, var, key):
    layout = [
        [sg.Input('tool1', key= key.input.tool , size=(70, 30)), sg.Button('Set Tool', key=key.but.set_tool, size=(70,30))],


        # -----------------------------------------   Kinematics parameters  ---------------------------------------------------------------------
        [sg.Text('')],
        [sg.Text(' Kinematic Parameters:', size=(150, 20), background_color='green', text_color='white')],

        [sg.Slider((0,10), tick_interval=100, orientation = 'h', background_color = 'black', default_value = int(var.j_vel*10), enable_events=True, size = (50,5), key=key.slider.j_vel),
            sg.Text(int(var.j_vel*10), key=key.disp.j_vel, size=(50,20)),
            sg.Text('Joint Velocity', size=(130,20), text_color='skyblue')],

        [sg.Slider((0,10), tick_interval=100, orientation = 'h', background_color = 'black', default_value = int(var.j_acc*10), enable_events=True, size = (50,5), key=key.slider.j_acc),
            sg.Text(int(var.j_acc*10), key=key.disp.j_acc, size=(50,20)),
            sg.Text('Joint Acceleration', size=(130,20), text_color='skyblue')],

        [sg.Slider((0,10), tick_interval=100, orientation = 'h', background_color = 'black', default_value = int(var.j_jrk*10), enable_events=True, size = (50,5), key=key.slider.j_jrk),
            sg.Text(int(var.j_jrk*10), key=key.disp.j_jrk, size=(50,20)),
            sg.Text('Joint Jerk', size=(130,20), text_color='skyblue')],

        [sg.Text(' ', size=(500,20)), sg.Button('Save', size=(180,30), key=key.but.saveKinParams, button_color=('white','gray'))],

        
        # -------------------------------------------   Impedence Parameters    ---------------------------------------------------------------------------
        [sg.Text('')],
        [sg.Text(' Impedence Parameters:', size=(150, 20), background_color='green', text_color='white')],

        [sg.Slider((0,2000), tick_interval=100, orientation = 'h', background_color = 'black', default_value = var.xy_imp, enable_events=True, size = (50,5), key=key.slider.xyImp),
            sg.Text(var.xy_imp, key=key.disp.xyImp, size=(50,20)),
            sg.Text('XY Impedence', size=(130,20), text_color='skyblue')],

        [sg.Slider((0,2000), tick_interval=100, orientation = 'h', background_color = 'black', default_value = var.z_imp, enable_events=True, size = (50,5), key=key.slider.zImp),
            sg.Text(var.z_imp, key=key.disp.zImp, size=(50,20)),
            sg.Text('Z Impedence', size=(130,20), text_color='skyblue')],
        
        [sg.Slider((0,1000), tick_interval=100, orientation = 'h', background_color = 'black', default_value = var.abc_imp, enable_events=True, size = (50,5), key=key.slider.abcImp),
            sg.Text(var.abc_imp, key=key.disp.abcImp, size=(50,20)),
            sg.Text('ABC Impedence', size=(130,20), text_color='skyblue')],
        
        [sg.Slider((0,10), tick_interval=100, orientation = 'h', background_color = 'black', default_value = int(var.damp*10), enable_events=True, size = (50,5), key=key.slider.damp),
            sg.Text(int(var.damp*10), key=key.disp.damp, size=(50,20)),
            sg.Text('Damping Ratio', size=(130,20), text_color='skyblue')],

        [sg.Button('Set Impedence', size=(500, 30), key=key.but.set_imp), sg.Text('   ', size=(10,20)),
        sg.Button('Save', size=(180,30), key=key.but.saveImpParams, button_color=('white','gray'))],

        # -------------------------------------------------  Joint Angles  --------------------------------------------------------------------------------
        [sg.Text('')],
        [sg.Text(' Set Joint Angles:', size=(150, 20), background_color='green', text_color='white')],

        [sg.Slider((-179,180), orientation = 'h', background_color = 'black', default_value = var.j1, enable_events=True, size = (50,5), key=key.slider.J1),
            sg.Text(var.j1, key=key.disp.J1, size=(50,20)),
            sg.Text('Joint[1] angle', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(-179.0,180.0),   orientation = 'h', background_color = 'black', default_value = var.j2, enable_events=True, size = (50,5), key=key.slider.J2),
            sg.Text(var.j2, key=key.disp.J2, size=(50,20)),
            sg.Text('Joint[2] angle', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(-179.0,180.0),   orientation = 'h', background_color = 'black', default_value = var.j3, enable_events=True, size = (50,5), key=key.slider.J3),
            sg.Text(var.j3, key=key.disp.J3, size=(50,20)),
            sg.Text('Joint[3] angle', size=(130,20), text_color='skyblue')], 
        [sg.Slider((-179,180),  orientation = 'h', background_color = 'black', default_value = var.j4, enable_events=True, size = (50,5), key=key.slider.J4),
            sg.Text(var.j4, key=key.disp.J4, size=(50,20)),
            sg.Text('Joint[4] angle', size=(130,20), text_color='skyblue')],  
        [sg.Slider(range=(-179.0,180.0),   orientation = 'h', background_color = 'black', default_value = var.j5, enable_events=True, size = (50,5), key=key.slider.J5),
            sg.Text(var.j5, key=key.disp.J5, size=(50,20)),
            sg.Text('Joint[5] angle', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(-179.0,180.0),   orientation = 'h', background_color = 'black', default_value = var.j6, enable_events=True, size = (50,5), key=key.slider.J6),
            sg.Text(var.j6, key=key.disp.J6, size=(50,20)),
            sg.Text('Joint[6] angle', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(-179.0,180.0),   orientation = 'h', background_color = 'black', default_value = var.j7, enable_events=True, size = (50,5), key=key.slider.J7),
            sg.Text(var.j7, key=key.disp.J7, size=(50,20)),
            sg.Text('Joint[7] angle', size=(130,20), text_color='skyblue')],

        [sg.Button('Set Angles zero', size=(250, 30), key=key.but.set_zero_angs), sg.Button('Set Angles', size=(250, 30), key=key.but.set_angs),
        sg.Text('   ', size=(10,20)), sg.Button('Save', size=(180,30), key=key.but.saveAngs, button_color=('white','gray'))],


        # -------------------------------------------------  default XYZABC Position  ----------------------------------------------------------------------------
        [sg.Text('')],
        [sg.Text(' Set Initial Position:', size=(150, 20), background_color='green', text_color='white')],

        [sg.Slider((-700,700), orientation = 'h', background_color = 'black', default_value = var.default_position.x, enable_events=True, size = (50,5), key=key.slider.X),
            sg.Text(var.default_position.x, key=key.disp.X, size=(50,20)),
            sg.Text('X', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(-700,700),   orientation = 'h', background_color = 'black', default_value = var.default_position.y, enable_events=True, size = (50,5), key=key.slider.Y),
            sg.Text(var.default_position.y, key=key.disp.Y, size=(50,20)),
            sg.Text('Y', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(-400,800),   orientation = 'h', background_color = 'black', default_value = var.default_position.z, enable_events=True, size = (50,5), key=key.slider.Z),
            sg.Text(var.default_position.z, key=key.disp.Z, size=(50,20)),
            sg.Text('Z', size=(130,20), text_color='skyblue')], 
        [sg.Slider((-179,180),  orientation = 'h', background_color = 'black', default_value = var.default_position.a, enable_events=True, size = (50,5), key=key.slider.A),
            sg.Text(var.default_position.a, key=key.disp.A, size=(50,20)),
            sg.Text('A', size=(130,20), text_color='skyblue')],  
        [sg.Slider(range=(-179,180),   orientation = 'h', background_color = 'black', default_value = var.default_position.b, enable_events=True, size = (50,5), key=key.slider.B),
            sg.Text(var.default_position.b, key=key.disp.B, size=(50,20)),
            sg.Text('B', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(-179,180),   orientation = 'h', background_color = 'black', default_value = var.default_position.c, enable_events=True, size = (50,5), key=key.slider.C),
            sg.Text(var.default_position.c, key=key.disp.C, size=(50,20)),
            sg.Text('C', size=(130,20), text_color='skyblue')],

        [ sg.Button('Move To Default Init Position', size=(500, 30), key=key.but.move2defualtInitPos),
        sg.Text('   ', size=(10,20)), sg.Button('Save', size=(180,30), key=key.but.saveXYZABC, button_color=('white','gray'))],


        # -------------------------------------------------  Free Mode (Compliant) ----------------------------------------------------------------------------
        [sg.Text('')],
        [sg.Text(' Free Mode:', size=(150, 20), background_color='green', text_color='white')],

        [sg.Slider((0,10), orientation = 'h', background_color = 'black', default_value = var.xy_compliant, enable_events=True, size = (50,5), key=key.slider.xyCompliant),
            sg.Text(var.xy_compliant, key=key.disp.xyCompliant, size=(50,20)),
            sg.Text('XY', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(0,100),   orientation = 'h', background_color = 'black', default_value = var.z_compliant, enable_events=True, size = (50,5), key=key.slider.zCompliant),
            sg.Text(var.z_compliant, key=key.disp.zCompliant, size=(50,20)),
            sg.Text('Z', size=(130,20), text_color='skyblue')],
        [sg.Slider(range=(0,10),   orientation = 'h', background_color = 'black', default_value = var.abc_compliant, enable_events=True, size = (50,5), key=key.slider.abcCompliant),
            sg.Text(var.abc_compliant, key=key.disp.abcCompliant, size=(50,20)),
            sg.Text('ABC', size=(130,20), text_color='skyblue')], 

        [sg.Button('Set Cur Pos as Leg Init Pos', size=(250, 30), key=key.but.setCurPos_as_legInitPos), sg.Button('Free Mode', size=(250, 30), key=key.but.freeMode, button_color=sg.NICE_BUTTON_COLORS[4]),
        sg.Text('   ', size=(10,20)), sg.Button('Save', size=(180,30), key=key.but.saveFreeModeParams, button_color=('white','gray'))],
        
        
        # -------------------------------------------------  Leg Movements ----------------------------------------------------------------------------
        [sg.Text('')],
        [sg.Text(' Leg Movements:', size=(150, 20), background_color='green', text_color='white')],

        [sg.Text(' Select Leg:', size=(150, 20), text_color=None),
        sg.Radio('Left', 1, default=True, size=(100,30), enable_events=True, key=key.radio.leftLeg), sg.Radio('Right', 1, size=(100,30), enable_events=True, key=key.radio.rightLeg)],

        [sg.Text('Select Move Mode: ', size=(150,20)), 
            sg.Radio('ptp', 2, size=(50,30), default=True, enable_events=True, key=key.radio.ptp), sg.Radio('lin', 2, size=(50,30), enable_events=True, key=key.radio.lin), 
            sg.Radio('arc', 2, size=(50,30), enable_events=True, key=key.radio.arc)],
        
        [sg.Checkbox('gait', size=(80,40), enable_events=True, key=key.checkBox.gait, background_color='blue', text_color='white'),
        sg.Slider(range=(10,300), orientation='h', background_color='black', default_value=var.step_h, enable_events=True, size=(20,5), key=key.slider.step_h),
        sg.Text(var.step_h, key=key.disp.step_h, size=(30,20)),
        sg.Text('Step Height', text_color='skyblue', size=(100,20)), 

        sg.Spin([x for x in range(0, 10+1)], int(var.blendingOri*10), size=(60,60), key=key.spin.blend, enable_events=True),
        sg.Text('BlendingOri', size=(80,20), text_color='skyblue')],

        [sg.Slider(range=(0,200), orientation='h', default_value=var.dx, enable_events=True, size=(30,5), key=key.slider.dx),
        sg.Text(var.dx, key=key.disp.dx, size=(30,20)), sg.Text('dx', size=(30,20), text_color='skyblue')],
        [sg.Slider(range=(0,200), orientation='h', default_value=var.dy, enable_events=True, size=(30,5), key=key.slider.dy),
        sg.Text(var.dy, key=key.disp.dy, size=(30,20)), sg.Text('dy', size=(30,20), text_color='skyblue')],
        [sg.Slider(range=(0,200), orientation='h', default_value=var.dz, enable_events=True, size=(30,5), key=key.slider.dz),
        sg.Text(var.dz, key=key.disp.dz, size=(30,20)), sg.Text('dz', size=(30,20), text_color='skyblue')],
        
        [sg.Slider((10,100), tick_interval=100, orientation = 'h', default_value = var.gaitSpd, enable_events=True, size = (30,5), key=key.slider.gaitSpd),
        sg.Text(var.gaitSpd, key=key.disp.gaitSpd, size=(30,20)),
        sg.Text('Speed', size=(40,20), text_color='skyblue'),
        sg.Text('   ', size=(140,20)), sg.Button('Save', size=(180,30), key=key.but.saveGaitParams, button_color=('white','gray'))],

        [sg.Button('P1', key=key.but.P1, size=(180,50), button_color=sg.NICE_BUTTON_COLORS[3]), sg.Button('P2', key=key.but.P2, size=(180,50), button_color=sg.NICE_BUTTON_COLORS[3]),
        sg.Button('P3', key=key.but.P3, size=(180,50), button_color=sg.NICE_BUTTON_COLORS[3])],
        [sg.Button('P4', key=key.but.P4, size=(180,50), button_color=sg.NICE_BUTTON_COLORS[3]), sg.Button('P5', key=key.but.P5, size=(180,50), button_color=sg.NICE_BUTTON_COLORS[3]),
         sg.Button('P6', key=key.but.P6, size=(180,50), button_color=sg.NICE_BUTTON_COLORS[3]), sg.Checkbox('Set point Orientations',enable_events=True, size=(150,30), key= key.checkBox.setPointOri )],
        [sg.Button('Move Leg To Initial Position', key=key.but.Move2LegInit, size=(550, 50), button_color=sg.NICE_BUTTON_COLORS[4])],



        # ----------------------------------------------- OUTPUTS --------------------------------------------------------------------------------------------
        [sg.Text('')],
        [sg.Text('Robot Feedbacks: ', background_color='green',text_color='white', size=(120,20))],
        [sg.Text('Position::', size=(80,30))],
        [sg.Text(' X:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowX, text_color='white'), 
         sg.Text(' Y:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowY, text_color='white'), 
         sg.Text(' Z:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowZ, text_color='white'),
         sg.Text(' A:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowA, text_color='white'), 
         sg.Text(' B:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowB, text_color='white'),
         sg.Text(' C:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowC, text_color='white'), sg.Text('[mm]', size=(30,30), text_color='white')],

        [sg.Text('Joint Angles::', size=(80,30))],
        [sg.Text('J1:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowJ1, text_color='white'), 
         sg.Text('J2:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowJ2, text_color='white'),
         sg.Text('J3:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowJ3, text_color='white'),
         sg.Text('J4:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowJ4, text_color='white'), 
         sg.Text('J5:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowJ5, text_color='white'),
         sg.Text('J6:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowJ6, text_color='white'),
         sg.Text('J7:', size=(20,30)), sg.Text('0', size=(50,30), key=key.disp.nowJ7, text_color='white'), sg.Text('[Degrees]', size=(70,30), text_color='white'),
        ],

        

        [sg.Output(size=(68,10), key = "_output_")],

        
    ]
    return layout
