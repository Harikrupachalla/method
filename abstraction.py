from abc import ABC, abstractmethod

class BOI(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass
    def offers(self):
        print("providing offers")

class SBI(BOI):
    def interest(self):
        print("In SBI bank 5 rupees interest")

class HDFC(BOI):
    def interest(self):
        print("In HDFC 7 rupees interest")

s=SBI()
h=HDFC()
s.bank_info()
s.interest()
h.bank_info()
h.interest()