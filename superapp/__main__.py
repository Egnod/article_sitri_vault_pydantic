from superapp.config import AppSettings

if __name__ == "__main__":
    config = AppSettings()

    print(config)
    print(config.dict())
