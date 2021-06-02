def divide(dividend: int, divisor: int) -> int:
        s=dividend
        d=divisor
        d1=divisor
        if s<0:
            s=-s
        if d<0:
            d=-d
            d1=-d1
        if d==1:
            if (dividend<0 and divisor>0):
                return dividend
            if (dividend>0 and divisor<0):
                return -dividend
            else:
                return s
                
        q=0
        while s>=d1:
            s-=d
            q+=1
        if dividend*divisor>0:
            return q
        else:
            return -q