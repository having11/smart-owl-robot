from smart_owl import Smart_Owl
from pin_definitions import pin_defs, step_seq
import time
import sys

owl = Smart_Owl(pin_defs, step_seq)

owl.displayFromCamera()

time.sleep(5)

owl.displayFromCamera()

time.sleep(5)

owl.drive(200, 200)

for x in range(500):
    owl.displayFromCamera()
    time.sleep(0.1)

owl.end()

#sys.exit()