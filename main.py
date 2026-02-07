from src.tasks.fetch_video import FetchVideo
from src.threads.threads import Threads
from src.utils.logger import Logger, Level
from src.video.video import Video


VIDEO_URL = ""
RESOLUTION = "1920x1080" # 1920x1080 or 1080p works !
FPS: int = 60 # Enter a number or None if not available for the video.

def main():
    try:
        video = Video(url=VIDEO_URL, resolution=RESOLUTION, fps=FPS)

        threads = Threads()
        threads.start_all()

        for _ in range(len(threads)):
            threads.add_task(FetchVideo(video=video, thread_count=len(threads)))

        results: dict = threads.stop_all()

        video.save(results)
    except Exception as e:
        Logger.log("Unexpected behavior, the video might've not been downloaded successfully. Error will follow", level=Level.WARNING, to_std_out=True)
        Logger.log(e, level=Level.WARNING, to_std_out=True)

if __name__ == "__main__":
    main()