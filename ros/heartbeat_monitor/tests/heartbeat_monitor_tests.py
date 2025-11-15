import pytest
from heartbeat_monitor.heartbeat_monitor import HeartbeatMonitor

# Fake ROS2 clock
class FakeTime:
    def __init__(self, nanoseconds):
        self.nanoseconds = nanoseconds

class FakeClock:
    def __init__(self, value):
        self._value = value
    def now(self):
        return FakeTime(self._value)

# Fake ROS Header msg
class FakeHeader:
    def __init__(self, frame_id):
        self.frame_id = frame_id

def test_heartbeat_updates_timestamp(monkeypatch):
    node = HeartbeatMonitor()

    # Patch the clock so time is predictable
    fake_clock = FakeClock(123 * 1e9)
    monkeypatch.setattr(node, "get_clock", lambda: fake_clock)

    # Send fake message
    msg = FakeHeader("controller")
    node.heartbeat_callback(msg)

    assert node.expected_surface_nodes["controller"] == 123 * 1e9
