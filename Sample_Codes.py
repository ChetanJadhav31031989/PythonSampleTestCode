import os
import sys

print("Sample Python Code")


class SampleClass:
    def __init__(self, **kwargs):
        self.ARGS = kwargs

    def samplerun(self):
        print("Hello....!")
        print("Datas: {}".format(self.ARGS))


objsample = SampleClass(Myname="Chetan", Surname="Jadhav", Designation="Technical Architect")
objsample.samplerun()

