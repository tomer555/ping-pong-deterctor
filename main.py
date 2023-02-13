from gpiozero import MotionSensor
from ping_pong_monitor import PingPongMonitor

sensor = MotionSensor(4)

ping_pong_monitor = PingPongMonitor(sensor)

ping_pong_monitor.listen()

