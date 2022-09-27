import pytest

class Location:
    def __init__ (self,name,country):
        self.name = name
        self.country = country
    def myLocation(self):
        print(self.name)


locl = Location("Theo", "Netherlands")
locl.myLocation()

def test_mylocation():
    test_local = Location("test1", "test2loc")
    assert test_local.myLocation() == "test1"

