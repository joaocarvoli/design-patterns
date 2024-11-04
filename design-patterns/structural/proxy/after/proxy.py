from real_subject import RealSubject

class Proxy:
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        # Add additional logic here if needed
        print("Proxy: Checking access prior to firing a real request.")
        return self._real_subject.request()