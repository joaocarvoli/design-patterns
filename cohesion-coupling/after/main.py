from app import Application

def main():
    app = Application()
    registered_vehicle = app.register_vehicle("Volkswagen ID3")
    print(registered_vehicle)

if __name__ == "__main__":
    main()