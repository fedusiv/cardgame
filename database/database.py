class DataBase:
    # Singleton part
    _instance = None

    @staticmethod
    def instance():
        if DataBase._instance is None:
            DataBase()
        return DataBase._instance

    def __init__(self):
        DataBase.__instance = self
