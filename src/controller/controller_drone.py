from inputs import get_gamepad
import math
import threading
import time

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.B = 0
        

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read_controller_commands(self): # return the buttons/triggers that you care about in this methode
        
        RT = self.RightTrigger
        LT = self.LeftTrigger
        RB = self.RightBumper
        LB = self.LeftBumper

        LJoystick_pitch = self.LeftJoystickY
        LJoystick_roll = self.LeftJoystickX
        
        A = self.A
        B = self.B
       
        return [RT, LT, RB, LB, LJoystick_pitch,LJoystick_roll,A,B]


    def _monitor_controller(self):
       
        while True:
            # After a quick test, the max is 5e-5 s. definitly enough.
            
            
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state


if __name__ == '__main__':
    joy = XboxController()
    while True:
        print(joy.read_controller_commands())





