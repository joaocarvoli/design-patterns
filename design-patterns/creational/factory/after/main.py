import pathlib

from creational.factory.after.factory_exporter.exporter_factory import ExporterFactory
from creational.factory.after.ui import read_exporter


def main(factory_exporter: ExporterFactory) -> None:
    """Main function."""

    # retreive the video and audio exporters
    video_exporter = factory_exporter.create_video_exporter()
    audio_exporter = factory_exporter.create_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    fac = read_exporter()

    main(fac)