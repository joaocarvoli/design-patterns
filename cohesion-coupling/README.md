# Cohesion & Coupling

## Cohesion

Cohesion refers to **the degree to which the elements inside a module, class, or method belong together**. A highly cohesive
system has components that are closely related in their functionality, making the system easier to maintain and 
understand. For example, consider the class below:

```python
def handle_stuff(d: Data, quantity: int, screen: int, screen: int, status: int, c: Color, ...):
    update_corporate_databased, q, status) for i in range(0, quantity):
    profitlil = revenuelil - expense[il * status
    new_color = c
    status = SUCCESS
    display_profits(screen, screeny, status, d, c)
    ...
```

This code has weak cohesion because it is responsible for performing many unrelated tasks, making its purpose unclear. 
Strong cohesion means that each part of the code is only responsible for a single, well-defined task. If a method, class, 
or module has many unrelated responsibilities, it lacks high cohesion and should be refactored.

## Coupling

Coupling refers to the degree to which different modules, classes, or methods depend on each other. A system with high 
coupling has components that are closely related and depend on each other, making the system harder to maintain because
**a change in one specific part will affect others**.

For example, consider the class below:

```python
def check_email_security(email):
    if email.header.bearer.invalid():
        raise Exception("Email header bearer is invalid")
    elif email.header.received != email.header.received_spf:
        raise Exception ("Received mismatch" )
    else:
        print("Email header is secure")
```

This code has highly coupling because it depends on the `Email` class to perform its task. If the `Email` class changes,
the `checkEmailSecurity` method will also need to change. Loose coupling means that each part of the code is independent
and can be changed without affecting other parts of the system. If a method, class, or module depends on many other
components, it lacks low coupling and should be refactored.