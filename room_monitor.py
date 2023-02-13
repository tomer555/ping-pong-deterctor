from gpiozero import MotionSensor
from datetime import datetime
from time import sleep
from abc import ABC, abstractmethod
from retry import retry

class RoomMonitor(ABC):

    sensor: MotionSensor
    last_motion_time: datetime
    room_status: str
    motion: bool

    def __init__(self, sensor, check_interval_seconds = 10, idle_till_free_seconds = 30) -> None:
        self.sensor = sensor
        self.last_motion_time = datetime.now()
        self.room_status = "FREE"
        self.motion = False
        self.check_interval_seconds = check_interval_seconds
        self.idle_till_free_seconds = idle_till_free_seconds

    def registerEvents (self):
        self.sensor.when_motion = self.onMotionDetected
    
    def onMotionDetected(self):
        self.last_motion_time = datetime.now()
        self.motion = True

    @abstractmethod
    @retry((Exception), tries=3, delay=2, backoff=2)
    def handleRoomOccupied ():
        pass
    
    @abstractmethod
    @retry((Exception), tries=3, delay=2, backoff=2)
    def handleRoomFree ():
        pass

    def listen(self):
        while True:
            seconds_since_last_motion = (datetime.now()- self.last_motion_time).total_seconds()
            print(f'room_status: {self.room_status}')
            print(f'motion: {self.motion}')
            if (not self.motion and self.room_status != "FREE" and seconds_since_last_motion > self.idle_till_free_seconds):
                self.room_status = "FREE"
                try:
                    self.handleRoomFree()
                except Exception as err:
                    print(f'error while trying to run room free handler: {err}')
            elif (self.motion and self.room_status != "BUSY"):
                self.room_status = "BUSY"
                try:
                    self.handleRoomOccupied()
                except Exception as err:
                    print(f'error while trying to run room occupied handler: {err}')
            self.motion = False
            sleep(self.check_interval_seconds)