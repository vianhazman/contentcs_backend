import imageio, os
from django.conf import settings
from objects.models import Video


class MetadataFetch:
    def getVideoDuration(id):
        video_obj = Video.objects.get(id=id)
        VIDEO_PATH = os.path.join(settings.MEDIA_ROOT,
                                  str(video_obj.video_file))
        try:
            reader = imageio.get_reader(VIDEO_PATH)
            video_duration = reader.get_meta_data()['duration']
            video_obj.video_duration_in_seconds = video_duration
            video_obj.save()
            return video_obj
        except FileNotFoundError:
            return None


