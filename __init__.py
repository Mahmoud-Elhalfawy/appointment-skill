from mycroft import MycroftSkill, intent_file_handler


class Appointment(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('appointment.intent')
    def handle_appointment(self, message):
        self.speak_dialog('appointment')


def create_skill():
    return Appointment()

