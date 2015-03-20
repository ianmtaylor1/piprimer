import RPi.GPIO as GPIO

class BinaryLEDCounter:
    
    def __init__(self,pinlist):
        self._pins = pinlist
        for p in pinlist:
            if GPIO.gpio_function(p)==GPIO.OUT:
                GPIO.setup(p,GPIO.OUT)
            else:
                GPIO.setup(p,GPIO.OUT,initial=GPIO.LOW)
    
    def maxvalue(self):
        return 2**len(self._pins) - 1
    
    def getvalue(self):
        v = 0
        for i,p in enumerate(self._pins):
            if GPIO.input(p)==GPIO.HIGH:
                v += 2**i
        return v
    
    def setvalue(self,value):
        if value > self.maxvalue():
            raise Exception('Value {0} greater than max: {1}'.format(value,self.maxvalue()))
        for p in self._pins:
            if value%2==1:
                GPIO.output(p,GPIO.HIGH)
            else:
                GPIO.output(p,GPIO.LOW)
            value = value//2

