from real_subject import RealSubject

def client_code(subject: RealSubject):
    print(subject.request())

if __name__ == "__main__":
    real_subject = RealSubject()
    client_code(real_subject)