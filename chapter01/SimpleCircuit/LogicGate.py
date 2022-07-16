# LogicGate Base Class
class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

# BinaryGate Base Class
class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.get_label() + "-->"))
        else:
            return self.pinA.get_from().get_output()

    def get_pin_b(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.get_label() + "-->"))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
             self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

# UnaryGate Base Class
class UnaryGate(LogicGate):
    def __init__(self,label):
        super().__init__(label)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.get_label() + "-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

# AndGate
class AndGate(BinaryGate):
    def __int__(self,n):
        super(AndGate, self).__int__(n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 and b==1:
            return 1
        else:
            return 0
# OrGate
class OrGate(BinaryGate):
    def __int__(self,n):
        super(OrGate, self).__int__(n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 or b==1:
            return 1
        else:
            return 0
# NotGate
class NotGate(UnaryGate):
    def __int__(self,n):
        super(OrGate, self).__int__(n)

    def perform_gate_logic(self):
        a = self.get_pin()
        if a==0:
            return 1
        else:
            return 0

# Connector
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate


# main
def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())

main()