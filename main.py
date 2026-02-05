from src.tasks.fetch_video import FetchVideo
from src.threads.threads import Threads
from src.video.video import Video


VIDEO_URL = ""
RESOLUTION = "1920x1080" # 1920x1080 or 1080p works !
FPS: int = 60 # Enter a number or None if not available for the video.

def main():
    video = Video(url=VIDEO_URL, resolution="1920x1080", fps=FPS)

    threads = Threads()
    threads.start_all()

    for _ in range(len(threads)):
        threads.add_task(FetchVideo(video=video, thread_count=len(threads)))

    results: dict = threads.stop_all()

    video.save(results)

if __name__ == "__main__":
    main()