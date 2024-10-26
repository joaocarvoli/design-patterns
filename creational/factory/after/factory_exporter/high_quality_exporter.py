from creational.factory.after.audio.aac_audio_exporter import AACAudioExporter
from creational.factory.after.audio.audio_exporter import AudioExporter
from creational.factory.after.factory_exporter.exporter_factory import ExporterFactory
from creational.factory.after.video.h264hi422p_video_exporter import H264Hi422PVideoExporter
from creational.factory.after.video.video_exporter import VideoExporter


class HighQualityExporter(ExporterFactory):
    """
        Concrete implementation of an ExporterFactory.
        The HighQualityExporter, provides a slower exportation process but a higher quality.
    """

    def create_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

    def create_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()
