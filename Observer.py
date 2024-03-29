events={"close_window":[]}
class EventHandler:
    def add_event(self,name,methods):
        global events
        events[name].append(methods)
    def event_trig(self,event,trazi):
        events[event][0](trazi)







