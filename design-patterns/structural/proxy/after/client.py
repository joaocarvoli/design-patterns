from real_subject import RealSubject
from proxy import Proxy

def client_code(subject: Proxy):
    print(subject.request())

if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    client_code(proxy)