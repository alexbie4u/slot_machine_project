import pytest
from main import SlotMachine

def main():
    ...
    
def test_deposit():
    slot_machine = SlotMachine()
    assert slot_machine.deposit(10) == 10
    assert slot_machine._balance == 10

    
def test_number_of_lines():
    ...
    
