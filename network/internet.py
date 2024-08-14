import threading
import time
import queue

class Frame:
    def __init__(self, data):
        self.header = "HEADER"
        self.data = data
        self.footer = "FOOTER"
        self.checksum = self.calculate_checksum()

    def calculate_checksum(self):
        return sum(ord(char) for char in self.data) % 256

    def is_valid(self):
        return self.checksum == self.calculate_checksum()

    def __str__(self):
        return f"{self.header}{self.data}{self.footer}{self.checksum}"

class Sender:
    def __init__(self, clock_period, media):
        self.clock_period = clock_period
        self.media = media

    def send_bit(self, bits_chunk):
        print(f"Sender: Sending bits {bits_chunk}")
        self.media.put(bits_chunk)
        time.sleep(self.clock_period)

class Receiver:
    def __init__(self, clock_period, media):
        self.clock_period = clock_period
        self.media = media
        self.buffer = ""

    def receive_bit(self):
        while True:
            bits_chunk = self.media.get()
            if bits_chunk is None:
                break
            self.buffer += bits_chunk
            frame_length = 6 + len(self.buffer[6:-9]) + 6 + 3
            if len(self.buffer) >= frame_length:
                frame_str = self.buffer[:frame_length]
                self.buffer = self.buffer[frame_length:]
                yield frame_str
            time.sleep(self.clock_period)

class MacSender:
    def __init__(self, frames_to_send, clock_period, media):
        self.frames_to_send = frames_to_send
        self.clock_period = clock_period
        self.media = media
        self.index = 0
        self.physical_sender = Sender(clock_period, media)

    def send_frame(self):
        while self.index < len(self.frames_to_send):
            frame = self.frames_to_send[self.index]
            self.index += 1
            print(f"MacSender: Sending frame {frame}")
            self.physical_sender.send_bit(str(frame))

class MacReceiver:
    def __init__(self, clock_period, media):
        self.clock_period = clock_period
        self.media = media
        self.physical_receiver = Receiver(clock_period, media)

    def receive_frame(self):
        for frame_str in self.physical_receiver.receive_bit():
            header = frame_str[:6]
            footer = frame_str[-9:-3]
            checksum = int(frame_str[-3:])
            data = frame_str[6:-9]
            frame = Frame(data)
            frame.checksum = checksum
            if frame.is_valid():
                print(f"MacReceiver: Received valid frame with data {frame.data}")
            else:
                print("MacReceiver: Received invalid frame")
            time.sleep(self.clock_period)

def main():
    frames_to_send = [Frame("101"), Frame("010"), Frame("101"), Frame("011")]
    clock_period = 0.5
    media = queue.Queue()

    mac_sender = MacSender(frames_to_send, clock_period, media)
    mac_receiver = MacReceiver(clock_period, media)

    sender_thread = threading.Thread(target=mac_sender.send_frame)
    receiver_thread = threading.Thread(target=mac_receiver.receive_frame)

    sender_thread.start()
    receiver_thread.start()

    sender_thread.join()
    media.put(None)  # 发送结束信号
    receiver_thread.join()

if __name__ == "__main__":
    main()