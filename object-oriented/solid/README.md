# S.O.L.I.D

## S - Single Responsibility Principle (SRP)

The SRP states that a class, interface, or method should have only one reason to change, meaning it should be responsible for a single aspect of the application. For example, an `Order` class should manage only order-specific functions, such as setting the payment method or tracking order status. It should not handle unrelated tasks like notifying the user about the payment or managing payment details. Each of these responsibilities—order processing, notifications, and payment handling—should be managed by separate classes. As functionality becomes more specific, further splitting may be needed to maintain clear boundaries.

## O - Open-Closed Principle (OCP)

The OCP states that a class, interface, or method should be open for extension but closed for modification. This means that once a structure is implemented, you should extend its functionality to support new features or requirements without altering the existing code. For instance, if you have a `Payment` class, adding a new payment method should involve creating an extension, not modifying the existing, stable code. This helps to preserve reliability and avoid introducing bugs in tested components.

## L - Liskov Substitution Principle (LSP)

The LSP states that subclasses should extend or add to the behavior of their parent class without altering its expected functionality. In other words, derived classes should be substitutable for their base classes without affecting the correctness of the program. For example, if you have an abstract class `Payment` with a constructor that takes order and security code as parameters, any subclass, like `DebitPayment` or `CreditPayment`, should adhere to this structure and display relevant security information. A `PaypalPayment` subclass, for instance, should not misuse the security code parameter to display unrelated data, like an email address, simply because it doesn't use a security code. If a subclass doesn’t align with the parent’s requirements, it might indicate that the subclass should not inherit from that particular class.

## I - Interface Segregation Principle (ISP)

The ISP states that a class should only implement behaviors that are relevant to its specific responsibilities. In other words, interfaces should be designed so that classes are not forced to implement methods they don’t need. For example, if `DebitPayment` requires email authentication while `PaypalPayment` relies on SMS authentication, it would be better to create separate interfaces for each authentication type rather than including both in a common `Payment` interface. Classes that need these features should implement only the interfaces they require, which could be achieved through multiple inheritance or mix-ins, depending on the language. Without ISP, a class might end up inheriting irrelevant methods, which can lead to incorrect implementations or errors.

## D - Dependency Inversion Principle (DIP)

The DIP states that classes should depend on abstractions, not on specific implementations. For example, if `DebitPayment` and `CreditPayment` both use authorizer classes to validate their payment methods, these payment methods (e.g., email, SMS, or CAPTCHA verification) should not rely on concrete implementations of the authorizers. Instead, they should depend on a generic authorization interface or abstraction. This approach allows the two payment types to remain flexible and independent from specific authorization implementations, making it easier to swap or extend authorizers without modifying the payment classes themselves.
