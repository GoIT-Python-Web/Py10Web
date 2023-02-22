class VideoFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print(f"Decoding video file: {self.filename}")


class AudioFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print(f"Decoding audio file: {self.filename}")


class SubtitlesFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print(f"Decoding subtitle file: {self.filename}")


class VideoPlayerFacade:
    def __init__(self, video_file: VideoFile, audio_file: AudioFile, subtitle_file: SubtitlesFile):
        self.video_file = video_file
        self.audio_file = audio_file
        self.subtitle_file = subtitle_file

    def play(self):
        self.video_file.decode()
        self.audio_file.decode()
        self.subtitle_file.decode()


if __name__ == '__main__':
    video_file = VideoFile('my_home_video.mp4')
    audio_file = AudioFile('my_home_video.mp3')
    subtitle_file = SubtitlesFile('my_home_video.srt')

    player = VideoPlayerFacade(video_file, audio_file, subtitle_file)
    player.play()
