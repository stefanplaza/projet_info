class SingletonView:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonView, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        # Initialisation de la vue
