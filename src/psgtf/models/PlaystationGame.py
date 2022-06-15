class PlaystationGame:
    name = ""
    id = ""
    platform = ""

    def __init__(self, name, id, platform):
        self.name = name
        self.id = id
        self.platform = platform
        

    def __str__(self):
        return self.name + " " + self.id + " -> " + self.platform 


    def get_name(self):
        return self.name


    def get_id(self):
        return self.id


    def get_platform(self):
        return self.platform