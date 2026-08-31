from pyatcrobo2.parts import DCMotor
import time

m1 = DCMotor('M1')
m2 = DCMotor('M2')


class Robot:
    def __init__(self, forward):
        self.m_speeds = [0, 0]
        self.m_default_rots = [forward, forward]
        self.m_rots = self.m_default_rots

    def set_motors(self, s1, s2):
        self.m_speeds = [s1, s2]

    def set_rotation(self, rot1=None, rot2=None):
        if rot1 is None and rot2 is None:
            self.m_rots = self.m_default_rots
        else:
            self.m_rots = [rot1, rot2]

    def move(self):
        if self.m_rots[0] == "cw":
            m1.cw()
        else:
            m1.ccw()

        if self.m_rots[1] == "cw":
            m2.cw()
        else:
            m2.ccw()

        m1.power(self.m_speeds[0])
        m2.power(self.m_speeds[1])

    def timed_move(self, duration_ms):
        self.move()
        time.sleep_ms(duration_ms)
        self.brake()

    def brake(self):
        self.m_speeds = [0, 0]
        m1.brake()
        m2.brake()
