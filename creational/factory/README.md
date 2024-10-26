# Factory

The Factory (or Factory Method) is a creational design pattern responsible for managing the creation of instances of concrete classes through abstract factories. This pattern allows the extension or addition of new concrete classes without violating the **Open-Closed** principle from SOLID.

For example, consider a `VideoExporter` factory that supports multiple video encoding formats. The factory is responsible for creating the specific concrete classes, all of which inherit from a common `VideoExporter` interface or abstract class. The same principle applies to an `AudioExporter` factory, which similarly handles the creation of audio exporting objects.

In this pattern, a controller or mapping structure is often used to determine which factory to call based on the desired functionality. While this introduces a potential point of failure, it also enables easy expansion of the software, allowing new video or audio exporters to be added as the software grows.

### Benefits
- **Flexibility**: Enables the software to easily accommodate new exporters or classes without significant code changes.
- **Adheres to Open-Closed Principle**: New classes can be added without modifying existing code, keeping the system modular.

### Example
A `VideoExporter` factory can handle different video encoding formats, creating concrete classes like `H264BPVideoExporter`, `H264HI422PVideoExporter`, or `LossLessVideoExport`, each implementing a common interface. Similarly, an `AudioExporter` factory could manage audio exporting formats.
