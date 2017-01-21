"""
Test our assembly interpreter.
"""

import sys
sys.path.append("..")


from unittest import TestCase, main

from Emu86.global_data import gdata
from Emu86.assemble import assemble


class AssembleTestCase(TestCase):

    def test_mov(self):
        assemble("mov eax, 1", gdata)
        self.assertEqual(gdata.registers["EAX"], 1)

    def test_add(self):
        gdata.registers["EAX"] = 2
        gdata.registers["EBX"] = 4
        assemble("add eax, ebx", gdata)
        self.assertEqual(gdata.registers["EAX"], 6)

    def test_sub(self):
        gdata.registers["EAX"] = 2
        gdata.registers["EBX"] = 4
        assemble("sub eax, ebx", gdata)
        self.assertEqual(gdata.registers["EAX"], -2)

    def test_imul(self):
        gdata.registers["EAX"] = 2
        gdata.registers["EBX"] = 4
        assemble("imul eax, ebx", gdata)
        self.assertEqual(gdata.registers["EAX"], 8)

    def test_and(self):
        gdata.registers["EAX"] = 27                     #...011011
        assemble("and eax, 23", gdata)                  #...001111
        self.assertEqual(gdata.registers["EAX"], 19)    #...001011

    def test_or(self):
        gdata.registers["EAX"] = 18                      #...010010
        assemble("or eax, 24", gdata)                    #...011000
        self.assertEqual(gdata.registers["EAX"], 26)     #...011010

    def test_xor(self):
        gdata.registers["EAX"] = 18                      #...010010
        assemble("xor eax, 24", gdata)                   #...011000
        self.assertEqual(gdata.registers["EAX"], 10)     #...001010

    def test_shl(self):
        gdata.registers["EAX"] = 18                      #...010010
        assemble("shl eax, 2", gdata)
        self.assertEqual(gdata.registers["EAX"], 72)     #..1001000

    def test_shr(self):
        gdata.registers["EAX"] = 18                      #...010010
        assemble("shr eax, 2", gdata)
        self.assertEqual(gdata.registers["EAX"], 4)      #...000100

    def test_neg(self):
        gdata.registers["EAX"] = 18
        assemble("neg eax", gdata)
        self.assertEqual(gdata.registers["EAX"], -18)

if __name__ == '__main__':
    main()