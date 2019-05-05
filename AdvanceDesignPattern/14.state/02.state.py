from state_machine import acts_as_state_machine, State, Event, before, after, InvalidStateTransition

@acts_as_state_machine
class Person:
    name = "Jim"

    sleeping = State(initial=True)
    running = State()
    cleaning = State()

    run = Event(from_states=sleeping, to_state=running)
    cleanup = Event(from_states=running, to_state=cleaning)
    sleep = Event(from_states=(running, cleaning), to_state=sleeping)

    @before("sleep")
    def sleep_before(self):
        print("After the busy day start. {} is going to sleep.".format(self.name))

    @after("sleep")
    def sleep_after(self):
        print("After finish the whole day. {} sleep well".format(self.name))
    
    @before('run')
    def run_before(self):
        print('exec before_run')    
    
    @after('run')
    def run_after(self):
        print('exec after_run')    

    @before("cleanup")
    def cleanup_before(self):
        print("exec before_cleanup")
    
    @after("cleanup")
    def cleanup_after(self):
        print("exec after_cleanup")


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print('Error: transition of {} from {} to {} failed with error'.format(
            process.name, process.current_state, event_name, err))


person = Person()

# print("the init state of person is {}".format(person.current_state))
assert "sleeping"==person.current_state

person.run()
# print("the state after person.run is {}".format(person.current_state))
assert "running"==person.current_state

person.cleanup()
# print("the state after person.cleanup is {}".format(person.current_state))
assert "cleaning"==person.current_state

person.sleep()
# print("the state after person.sleep is {}".format(person.current_state))
assert "sleeping"==person.current_state