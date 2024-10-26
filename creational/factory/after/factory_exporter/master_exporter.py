from creational.factory.after.audio.audio_exporter import AudioExporter
from creational.factory.after.audio.wav_audio_exporter import WAVAudioExporter
from creational.factory.after.factory_exporter.exporter_factory import ExporterFactory
from creational.factory.after.video.lossless_video_exporter import LosslessVideoExporter
from creational.factory.after.video.video_exporter import VideoExporter


class MasterExporter(ExporterFactory):
    """
        Concrete implementation of an ExporterFactory.
        The MasterExporter, provides the slowest exportation process but the highest quality.
    """

    def create_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()

    def create_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()
