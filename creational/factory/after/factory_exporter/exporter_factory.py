from abc import ABC, abstractmethod

from creational.factory.before.fac import VideoExporter, AudioExporter


class ExporterFactory(ABC):
    """
        Factory that represents a combinatino of a video and audio codec.
        The instance only creates and doesn't maintains.
    """

    @abstractmethod
    def create_video_exporter(self) -> VideoExporter:
        """
            Returns a new instance of a video exporter
        """
        pass

    @abstractmethod
    def create_audio_exporter(self) -> AudioExporter:
        """
            Returns a new instance of a audio exporter
        """
        pass