from creational.factory.after.factory_exporter.fast_exporter import FastExporterFactory
from creational.factory.after.factory_exporter.high_quality_exporter import HighQualityExporterFactory
from creational.factory.after.factory_exporter.master_exporter import MasterExporterFactory

FACTORIES = {
    "low": FastExporterFactory(),
    "high": HighQualityExporterFactory(),
    "master": MasterExporterFactory()
}