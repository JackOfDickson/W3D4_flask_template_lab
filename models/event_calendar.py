from models.event import Event

event1 = Event("02/02/2022", "Gus's birthday", 30, "Pebbles", "Top lolz")
event2 = Event("03/04/2022", "Jack's big day out", 17, "Crazy Golf", "Some crazy golf with the lads")
event_list = [event1, event2]

def add_new_event(new_event):
    event_list.append(new_event)