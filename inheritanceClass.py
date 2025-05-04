class Speaker:
    brand = "Beatpill" # class atribute

    def __init__(self,color,model):
        self.color = color # instance atribute
        self.model = model # instance atribute

    def power_on(self):
        print(f"Powering on {self.color} {self.model}")
    
    def power_of(self):
        print(f"Powering off {self.color} {self.model}")

class SmartSpeaker(Speaker):
    def __init__(self, color, model,voice_assistant="No Info"):
        super().__init__(color, model)
        self.voive_assistant = voice_assistant
    
    def say_hello(self,speaker_name):
        self.voive_assistant = speaker_name
        print(f"Hello, I am {speaker_name}")


spkr1 = Speaker("black","85XB5")
smart_speaker = SmartSpeaker("black","XYZ123")
smart_speaker.power_on()
smart_speaker.say_hello("Alexa")