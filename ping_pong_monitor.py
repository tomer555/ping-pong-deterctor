from slack import sendSlackMessage
from room_monitor import RoomMonitor
from ping_pong_repository import PingPongRepository
from slack import sendSlackMessage

class PingPongMonitor(RoomMonitor):

    def __init__(self, sensor) -> None:
        super(PingPongMonitor, self).__init__(sensor, 10, 30)
        super().registerEvents()
        self.monitorRepository = PingPongRepository()

    def handleRoomOccupied(self):
        sendSlackMessage(self.room_status)
        self.monitorRepository.insert(self.last_motion_time, self.room_status)

    def handleRoomFree(self):
        sendSlackMessage(self.room_status)
        self.monitorRepository.insert(self.last_motion_time, self.room_status)
    