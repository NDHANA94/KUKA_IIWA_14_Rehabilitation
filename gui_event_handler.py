#!/usr/bin/env python

import tools as tools
from kuka_tasks import KUKA_TASKS, kuka


key = tools.KEYS()
var = tools.VARIABLES()



def event_handler(window, event, values, key: key, var: var):
# def event_handler(window, event, values):
    
    kuka_tasks = KUKA_TASKS(var)
    # update kinematic parameters >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if values[key.slider.j_vel] != var.j_vel*10 or not var.start: 
        window.FindElement(key.disp.j_vel).Update(value=values[key.slider.j_vel])
        var.j_vel = float(values[key.slider.j_vel]/10)
        print('update joint velocity: {}'.format(var.j_vel))
        kuka_tasks.setVel(var.j_vel)
    
    if values[key.slider.j_acc] != var.j_acc*10 or not var.start:
        window.FindElement(key.disp.j_acc).Update(value=values[key.slider.j_acc])
        var.j_acc = float(values[key.slider.j_acc]/10)
        print('update joint acceleration: {}'.format(var.j_acc))
        kuka_tasks.setAcc(var.j_acc)

    if values[key.slider.j_jrk] != var.j_jrk*10 or not var.start:
        window.FindElement(key.disp.j_jrk).Update(value=values[key.slider.j_jrk])
        var.j_jrk = float(values[key.slider.j_jrk]/10)
        print('update joint jerk: {}'.format(var.j_jrk))
        kuka_tasks.setJrk(var.j_jrk)
        var.start = True




    # update Impedence parameters >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if values[key.slider.xyImp ] != var.xy_imp: 
        window.FindElement(key.disp.xyImp).Update(value=values[key.slider.xyImp])
        var.xy_imp = int(values[key.slider.xyImp])
        print('update xy impedence: {}'.format(var.xy_imp))
    
    if values[key.slider.zImp] != var.z_imp:
        window.FindElement(key.disp.zImp).Update(value=values[key.slider.zImp])
        var.z_imp = int(values[key.slider.zImp])
        print('update z impedence: {}'.format(var.z_imp))

    if values[key.slider.abcImp] != var.abc_imp:
        window.FindElement(key.disp.abcImp).Update(value=values[key.slider.abcImp])
        var.abc_imp = int(values[key.slider.abcImp])
        print('update abc impedence: {}'.format(var.abc_imp))

    if values[key.slider.damp] != var.damp*10:
        window.FindElement(key.disp.damp).Update(value=values[key.slider.damp])
        var.damp = float(values[key.slider.damp]/10)
        print('update damp ratio: {}'.format(var.damp))

    


    # update JOint Angles  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if values[key.slider.J1 ] != var.j1: 
        window.FindElement(key.disp.J1).Update(value=values[key.slider.J1])
        var.j1 = int(values[key.slider.J1])
        print('update default j[1]: {}'.format(var.j1))
    
    if values[key.slider.J2 ] != var.j2: 
        window.FindElement(key.disp.J2).Update(value=values[key.slider.J2])
        var.j2 = int(values[key.slider.J2])
        print('update default j[2]: {}'.format(var.j2))
    
    if values[key.slider.J3 ] != var.j3: 
        window.FindElement(key.disp.J3).Update(value=values[key.slider.J3])
        var.j3 = int(values[key.slider.J3])
        print('update default j[3]: {}'.format(var.j3))
    
    if values[key.slider.J4 ] != var.j4: 
        window.FindElement(key.disp.J4).Update(value=values[key.slider.J4])
        var.j4 = int(values[key.slider.J4])
        print('update default j[4]: {}'.format(var.j4))
    
    if values[key.slider.J5 ] != var.j5: 
        window.FindElement(key.disp.J5).Update(value=values[key.slider.J5])
        var.j5 = int(values[key.slider.J5])
        print('update default j[5]: {}'.format(var.j5))
    
    if values[key.slider.J6 ] != var.j6: 
        window.FindElement(key.disp.J6).Update(value=values[key.slider.J6])
        var.j6 = int(values[key.slider.J6])
        print('update default j[6]: {}'.format(var.j6))
    
    if values[key.slider.J7 ] != var.j7: 
        window.FindElement(key.disp.J7).Update(value=values[key.slider.J7])
        var.j7 = int(values[key.slider.J7])
        print('update default j[7]: {}'.format(var.j7))
    
    

    # UPDATE XYZABC >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if values[key.slider.X ] != var.default_position.x: 
        window.FindElement(key.disp.X).Update(value=values[key.slider.X])
        var.default_position.x = int(values[key.slider.X])
        print('update default position X: {}'.format(var.default_position.x))
    
    if values[key.slider.Y ] != var.default_position.y: 
        window.FindElement(key.disp.Y).Update(value=values[key.slider.Y])
        var.default_position.y = int(values[key.slider.Y])
        print('update default position Y: {}'.format(var.default_position.y))
    
    if values[key.slider.Z ] != var.default_position.z: 
        window.FindElement(key.disp.Z).Update(value=values[key.slider.Z])
        var.default_position.z = int(values[key.slider.Z])
        print('update default position Z: {}'.format(var.default_position.z))
    
    if values[key.slider.A ] != var.default_position.a: 
        window.FindElement(key.disp.A).Update(value=values[key.slider.A])
        var.default_position.a = int(values[key.slider.A])
        print('update default position A: {}'.format(var.default_position.a))
    
    if values[key.slider.B ] != var.default_position.b: 
        window.FindElement(key.disp.B).Update(value=values[key.slider.B])
        var.default_position.b = int(values[key.slider.B])
        print('update default position B: {}'.format(var.default_position.b))
    
    if values[key.slider.C ] != var.default_position.c: 
        window.FindElement(key.disp.C).Update(value=values[key.slider.C])
        var.default_position.c = int(values[key.slider.C])
        print('update default position C: {}'.format(var.default_position.c))

    

    # UPDATE FREEMODE PARAMETERS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if values[key.slider.xyCompliant ] != var.xy_compliant: 
        window.FindElement(key.disp.xyCompliant).Update(value=values[key.slider.xyCompliant])
        var.xy_compliant = int(values[key.slider.xyCompliant])
        print('update xy compliant: {}'.format(var.xy_compliant))
    
    if values[key.slider.zCompliant ] != var.z_compliant: 
        window.FindElement(key.disp.zCompliant).Update(value=values[key.slider.zCompliant])
        var.z_compliant = int(values[key.slider.zCompliant])
        print('update z compliant: {}'.format(var.z_compliant))
    
    if values[key.slider.abcCompliant ] != var.abc_compliant: 
        window.FindElement(key.disp.abcCompliant).Update(value=values[key.slider.abcCompliant])
        var.abc_compliant = int(values[key.slider.abcCompliant])
        print('update abc compliant: {}'.format(var.abc_compliant))

    

    # update gait parameters >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if values[key.radio.leftLeg] and var.cur_leg == 'right':
        var.cur_leg = 'left'
        print('Left Leg is selected')

    if values[key.radio.rightLeg] and var.cur_leg == 'left':
        var.cur_leg = 'right'
        print('Right Leg is selected')

    if values[key.radio.ptp] and var.moveMode != 'ptp':
        var.moveMode = 'ptp'
        print('ptp')
    
    if values[key.radio.lin] and var.moveMode != 'lin':
        var.moveMode = 'lin'
        print('lin')
    
    if values[key.radio.arc] and var.moveMode != 'arc':
        var.moveMode = 'arc'
        print('arc')

    if values[key.checkBox.gait] and not var.gaitMode:
        var.gaitMode = True
        print('Gait Mode is On!')
    if not values[key.checkBox.gait] and var.gaitMode:
        var.gaitMode = False
        print('Gait Mode is Off!')

    if values[key.slider.step_h] != var.step_h:
        window.FindElement(key.disp.step_h).Update(value=values[key.slider.step_h])
        var.step_h = float(values[key.slider.step_h])
        print('update step_h: {}'.format(var.step_h))

    if values[key.spin.blend] != var.blendingOri*10:
        var.blendingOri = float(values[key.spin.blend]/10)
        print('update BlendingOri.: {}'.format(var.blendingOri))

    if values[key.slider.dx] != var.dx:
        window.FindElement(key.disp.dx).Update(value=values[key.slider.dx])
        var.dx = float(values[key.slider.dx])
        print('update dx: {}'.format(var.dx))

    if values[key.slider.dy] != var.dy:
        window.FindElement(key.disp.dy).Update(value=values[key.slider.dy])
        var.dy = float(values[key.slider.dy])
        print('update dy: {}'.format(var.dy))
    
    if values[key.slider.dz] != var.dz:
        window.FindElement(key.disp.dz).Update(value=values[key.slider.dz])
        var.dz = float(values[key.slider.dz])
        print('update dz: {}'.format(var.dz))

    if values[key.checkBox.setPointOri]:
        var.setPointOrientation = True
    else:
        var.setPointOrientation = False
    

    if values[key.slider.gaitSpd] != var.gaitSpd:
        window.FindElement(key.disp.gaitSpd).Update(value=values[key.slider.gaitSpd])
        var.gaitSpd = float(values[key.slider.gaitSpd])
        print('update gait speed: {}'.format(var.gaitSpd))
        kuka_tasks.setCartVel(var.gaitSpd)
    # -----------------------------------------------------------------------------------------------------------------------------------------
    

    # SAVE DATA >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if event == key.but.saveKinParams:
        key_ = 'kin_params'
        values_ =  {'vel': var.j_vel, 'acc': var.j_acc, 'jerk': var.j_jrk}
        if tools.save_data(key_, values_):
            print('** Saving Kinematic Parameters **')
            
    if event == key.but.saveImpParams:
        key_ = 'imp_params'
        values_ =  {'xy': var.xy_imp, 'z': var.z_imp, 'abc': var.abc_imp, 'damp': var.damp}
        if tools.save_data(key_, values_):
            print('** Saving Impedence Parameters **')
    
    if event == key.but.saveAngs:
        key_ = 'joint_angs'
        values_ =  {'j1': var.j1, 'j2': var.j2, 'j3': var.j3, 'j4': var.j4, 'j5': var.j5, 'j6': var.j6, 'j7': var.j7}
        if tools.save_data(key_, values_):
            print('** Saving Default Joint Angles **')
    
    if event == key.but.saveXYZABC:
        key_ = 'XYZABC'
        values_ =  {'x': var.default_position.x, 'y': var.default_position.y, 'z': var.default_position.z, 'a': var.default_position.a, 'b': var.default_position.b, 'c': var.default_position.c}
        if tools.save_data(key_, values_):
            print('** Saving Default XYZABC **')
    
    if event == key.but.saveFreeModeParams:
        key_ = 'compliant'
        values_ =  {'xy': var.xy_compliant, 'z': var.z_compliant, 'abc': var.abc_compliant}
        if tools.save_data(key_, values_):
            print('** Saving FREE MODE parameters **')
    
    if event == key.but.saveGaitParams:
        key_ = 'locomotion'
        values_ =  {"gait_spd": var.gaitSpd, "step_h": var.step_h, "blend": var.blendingOri, "dx": var.dx, "dy": var.dy, "dz": var.dz}
        if tools.save_data(key_, values_):
            print('** Saving GAIT parameters **')

    # -----------------------------------------------------------------------------------------------------------------------------------------

    
    # KUKA TASKS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if event == key.but.set_tool:
        tool = values[key.input.tool]
        kuka_tasks.setTool(tool)

    if event == key.but.set_imp:
        imp = f'{var.xy_imp} {var.xy_imp} {var.z_imp} {var.abc_imp} {var.abc_imp} {var.abc_imp} {var.damp}'
        kuka_tasks.setImp(imp)

    if event == key.but.set_zero_angs:
        angs = '0 0 0 0 0 0 0'
        kuka_tasks.setAngs(angs)

    if event == key.but.set_angs:
        angs = f'{var.j1} {var.j2} {var.j3} {var.j4} {var.j5} {var.j6} {var.j7}'
        kuka_tasks.setAngs(angs)

    if event == key.but.move2defualtInitPos:
        initPos_default = f'{var.default_position.x} {var.default_position.y} {var.default_position.z} {var.default_position.a} {var.default_position.b} {var.default_position.c}'
        kuka_tasks.move_2_XYZABC(initPos_default, var.moveMode)

    if event == key.but.freeMode:
        comp = [var.xy_compliant, var.xy_compliant, var.z_compliant, var.abc_compliant, var.abc_compliant, var.abc_compliant]
        kuka_tasks.setCompliance(comp)
        while 1:
            event, values = window.read()
            window.FindElement('_output_').Update('')
            if event == key.but.freeMode:
                kuka_tasks.resetCompliance()
                break
            else:
                if event == key.but.setCurPos_as_legInitPos:
                    cur_xyzabc = kuka_tasks.getXYZABC()
                    print(cur_xyzabc)
                    if values[key.radio.leftLeg]:
                        var.cur_leg = 'left'
                        key_ = 'left'
                        values_ = {'init_pos': cur_xyzabc}
                        tools.save_data(key_, values_)
                        var.leftLeg_init_pos.x = cur_xyzabc[0]
                        var.leftLeg_init_pos.y = cur_xyzabc[1]
                        var.leftLeg_init_pos.z = cur_xyzabc[2]
                        var.leftLeg_init_pos.a = cur_xyzabc[3]
                        var.leftLeg_init_pos.b = cur_xyzabc[4]
                        var.leftLeg_init_pos.c = cur_xyzabc[5]
                        print("~ New Initial Point is recorded for Left Leg! ~")
                    if values[key.radio.rightLeg]:
                        var.cur_leg = 'right'
                        key_ = 'right'
                        values_ = {'init_pos': cur_xyzabc}
                        tools.save_data(key_, values_)
                        var.rightLeg_init_pos.x = cur_xyzabc[0]
                        var.rightLeg_init_pos.y = cur_xyzabc[1]
                        var.rightLeg_init_pos.z = cur_xyzabc[2]
                        var.rightLeg_init_pos.a = cur_xyzabc[3]
                        var.rightLeg_init_pos.b = cur_xyzabc[4]
                        var.rightLeg_init_pos.c = cur_xyzabc[5]
                        print("~ New Initial Point is recorded for Right Leg! ~")
                else:
                    print('Kuka is in COMPLIANCE MODE')
                    print('Click again Free Mode button to Exit!')

    if event == key.but.Move2LegInit:
        var.move2Point = 0

        if var.cur_leg == 'left':
            pos = f'{var.leftLeg_init_pos.x} {var.leftLeg_init_pos.y} {var.leftLeg_init_pos.z} {var.leftLeg_init_pos.a} {var.leftLeg_init_pos.b} {var.leftLeg_init_pos.c}'
            kuka_tasks.move_2_XYZABC(pos, 'ptp')
            print('moving to initial position of Left Leg')
        if var.cur_leg == 'right':
            pos = f'{var.rightLeg_init_pos.x} {var.rightLeg_init_pos.y} {var.rightLeg_init_pos.z} {var.rightLeg_init_pos.a} {var.rightLeg_init_pos.b} {var.rightLeg_init_pos.c}'
            kuka_tasks.move_2_XYZABC(pos, 'ptp')
            print('moving to initial position of Right Leg')

    if event == key.but.P1:
        var.move2Point = 1

    if event == key.but.P2:
        var.move2Point = 2


    if event == key.but.P3:
        var.move2Point = 3


    if event == key.but.P4:
        var.move2Point = 4


    if event == key.but.P5:
        var.move2Point = 5

    if event == key.but.P6:
        var.move2Point = 6

   
                    


    
        

