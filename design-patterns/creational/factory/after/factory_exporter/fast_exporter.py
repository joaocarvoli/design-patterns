from creational.factory.after.audio.aac_audio_exporter import AACAudioExporter
from creational.factory.after.audio.audio_exporter import AudioExporter
from creational.factory.after.factory_exporter.exporter_factory import ExporterFactory
from creational.factory.after.video.h264bp_video_exporter import H264BPVideoExporter
from creational.factory.after.video.video_exporter import VideoExporter


class FastExporterFactory(ExporterFactory):
    """
        Concrete implementation of an ExporterFactory.
        The FastExporter, focusing on fast exportation process and not quality.
    """

    def create_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

    def create_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()
