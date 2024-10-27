from creational.factory.after.factory_exporter.exporter_factory import ExporterFactory
from creational.factory.after.factory_exporter.factories_picker import FACTORIES


def read_exporter() -> ExporterFactory:
    """
        Method responsible for interact with user input from keyboard and select desired option
    """

    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in FACTORIES:
            return FACTORIES[export_quality]
        print(f"Unknown output quality option: {export_quality}.")