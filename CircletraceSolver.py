import numpy as np

class Solver():
    def Solver(self,obst,start,end,dangle):

        a = obst[0]
        b = obst[1]
        r = obst[2] + 10

        c = start[0]
        d = start[1]

        e = end[0]
        f = end[1]

        def getarg(x1,y1):
            temp1 = np.arctan2([y1-b],[x1-a])
            if temp1 < 0:
                temp1 = temp1 + 2*np.pi
            return temp1 * 180/np.pi

        def quadsolver(coeff):
            a = coeff[0]
            b = coeff[1]
            c = coeff[2]
            d = np.sqrt(b**2 - 4*a*c)
            y1 = (-b+d)/(2*a)
            y2 = (-b-d)/(2*a)
            return y1,y2

        g = -(f-d)
        h = (e-c)
        i = (f*c) - (e*d)

        if g != 0:
            coeff = [(h**2/g**2)+1 ,(((2*h*i)/(g**2)) + ((2*h*a)/g) - (2*b)) ,(((i**2)/(g**2)) + (a**2) + (2*a*i/g) + (b**2) - (r**2))]
            #y1,y2 = np.roots(coeff)
            y1,y2 = quadsolver(coeff)
            print(y1,y2)
            x1 = -(h*y1 + i)/g
            x2 = -(h*y2 + i)/g
        else:
            y1,y2 = -i/h
            coeff = [1,-2*a,(((i**2)/(h**2)) + (a**2) + (2*b*i/g) + (b**2) - (r**2))]
            x1,x2 = quadsolver(coeff)

        def distbetweenpts(x1,y1,x2,y2):
            return np.sqrt((x1-x2)**2 + (y1-y2)**2)

        d1 = distbetweenpts(x1,y1,c,d)
        d2 = distbetweenpts(x2,y2,c,d)

        nearpt = []
        farpt = []
        if d1 < d2:
            nearpt = (x1,y1)
            farpt = (x2,y2)
        else:
            nearpt = (x2,y2)
            farpt = (x1,y1)

        path = []

        #path.append((c,d))

        path.append((nearpt[0],nearpt[1]))

        theta1 = float(getarg(nearpt[0],nearpt[1]))
        theta2 = float(getarg(farpt[0],farpt[1]))

        operation = ''
        if(abs(theta1-theta2)>180):
            if(theta1>theta2):
                operation = '+'
            else:
                operation = '-'
        else:
            if(theta1>theta2):
                operation = '-'
            else:
                operation = '+'

        cangle = theta1
        eps = 1
        count = 0
        while(abs(cangle - theta2)>2):
            if(operation is '+'):
                cangle = cangle + eps
            else:
                cangle = cangle - eps
            cangle = cangle%360
            x = a + r*np.cos(cangle*np.pi/180)
            y = b + r*np.sin(cangle*np.pi/180)
            if (count%dangle == 0):
                path.append((float(x),float(y)))
            count = count + 1
        #path.append((float(e),float(f)))
        return path
