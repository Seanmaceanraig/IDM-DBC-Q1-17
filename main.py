import math

#Q01
aftWheelSize = 69 #mm
fwdWheelSize = 40 #mm

wheelMassLookup = [40, 56, 69, 90, 0.0025,0.010,0.050,0.050]

aluminiumArea = (0.120*0.220)+(2*math.pi*0.005*0.08) #mm2

mass = 0 #kg (enter if known, or leave at zero and the system will calculate it)

if(mass == 0):
    mass += (2*wheelMassLookup[wheelMassLookup.index(aftWheelSize)+4] + 2*wheelMassLookup[wheelMassLookup.index(fwdWheelSize)+4]) #adding mass of wheels
    mass += (0.045+0.004+0.005+0.125+0.400) #adding mass of batteries, battery connector, motor, and water bottle
    mass += (aluminiumArea*0.001*2710) #adding mass of aluminium

print("Section 1:")
print("   Wheel Specs Used: Fwd:",fwdWheelSize,"mm | Aft:",aftWheelSize,"mm")
print("   Mass:",round(mass,4),"kg")

#Q02
rollingResistance = mass*0.4 #N

print("\nSection 2:")
print("   Rolling Resistance:",rollingResistance,"N")

#Q03
resistanceDTGravity = mass*9.81*math.sin(math.radians(5))
totalResistingForce = rollingResistance+resistanceDTGravity #N

print("\nSection 3:")
print("   Resistance due to Gravity:",resistanceDTGravity,"N")
print("   Total Resisting Forces:",totalResistingForce,"N")

#Q04
powerEfficiency = 0.85

print("\nSection 4:")
print("   Power Efficiency:",powerEfficiency)

#Q05 (TBC)
motorShaftSpeed = 49.5 #rev.s-1 (Nm)
motorTorque = 25/1000 #Nm (Tm)
speedOfAxle = 5.5 #rev.s-1 (Na)
diameterOfMotor = 4/1000 #m (Dm)
diameterOfAxle = 4/1000 #m (Da)
diameterOfWheel = aftWheelSize/1000 #m (Dw)

vehicleVelocity = math.pi*speedOfAxle*diameterOfWheel #ms-1 (u)
transmissionEfficiency = (speedOfAxle/motorShaftSpeed)/(diameterOfMotor/diameterOfAxle) #(e)
drivingForce = 2*motorTorque*(diameterOfAxle/(diameterOfMotor*diameterOfWheel)) #N (Fd)

print("\nSection 5:")
print("   Vehicle Velocity:",vehicleVelocity,"m.s-1")
print("   Transmission Efficiency:",transmissionEfficiency)
print("   Driving Force",drivingForce,"N")

#Q06
pulleyRatio = diameterOfAxle/diameterOfMotor
#steadyStateSpd = 

print("\nSection 6:")
print("   Pulley Ratio:",pulleyRatio)
#print("   Steady State Speed:",steadyStateSpd,"m.s-1")

#Q07
#Q08
print("\nSection 8:")
largePulleyRadius = 1 #m (r1)
smallPulleyRadius = 1 #m (r2)
pulleySeparation = 1 #m (C)
tensionTautPulleySide = 1 #N (F1)
coefficientOfFriction = 0.4 #(mu)

contactAngleBtwnPulleys = math.pi-(2*math.asin((largePulleyRadius-smallPulleyRadius)/pulleySeparation)) #rad (B)
maxPermitTorque = tensionTautPulleySide*smallPulleyRadius*(1-pow(math.e,coefficientOfFriction*contactAngleBtwnPulleys*-1)) #Nm (Mmax)

lengthStretchedBelt = math.pi*(largePulleyRadius+smallPulleyRadius)+(2*pulleySeparation)+(pow(largePulleyRadius-smallPulleyRadius,2)/pulleySeparation) #m (Lb)

deltaBeltLength = 1 #m (deltaL)
originalBeltLength = 1 #m (L0)
strainInBelt = deltaBeltLength/originalBeltLength #m.m-1 (Epsilon)

if(strainInBelt >= 0 and strainInBelt < 0.1):
    elasticModulus = 6 #MPa (E)
elif(strainInBelt > 0.1 and strainInBelt <= 0.4):
    elasticModulus = 3 #MPa (E)
else:
    print("   Invalid value for strainInBelt. Expected: 0 <= strainInBelt <= 0.4, Received:",strainInBelt)
    elasticModulus = 0
    #raise Exception("Invalid value for strainInBelt. Must be 0 <= strainInBelt <= 0.4.")

stressInBelt = elasticModulus*strainInBelt #MPa.m.m-1 (sigma)

tensionSlackPulleySide = tensionTautPulleySide/(pow(math.e,coefficientOfFriction*contactAngleBtwnPulleys)) #F2
totalTension = tensionSlackPulleySide+tensionTautPulleySide #F

beltCrossSectionalArea = 1 #(m2)
tensionInBelt = totalTension/beltCrossSectionalArea #(sigma)

#Pulley Ratio Calculations
print("Section X: Pulley Ratio Calculations")

C1 = 75.25 #mm
C2 = 80.00 #mm

D = 57 #mm
d = 47 #mm

B = math.pi-(2*math.asin(((D/2)-(d/2))/C2))
print("B:",B)

v = 0.1 #m.s-1 Belt velocity
EstCoefFric = 0.4
E = 6 #MPa
L100 = math.pi*100 #mm
BOD = 3 #mm
LP1 = math.pi*((D+d)/2)+(2*C1)+(pow(D-d,2)/(4*C1))
LP2 = math.pi*((D+d)/2)+(2*C2)+(pow(D-d,2)/(4*C2))
print("LP1:",LP1,"|LP2:",LP2)

StrnStretch = (LP2-LP1)/LP1
StrsStretch = E*StrnStretch #N.mm-2
FrceStretch = StrsStretch*math.pi*(pow(BOD,2)/2)
FRatio = pow(math.e,EstCoefFric*B)

print("Stress due to Stretch:",StrsStretch)
print("Strain due to Stretch:",StrnStretch)
print("Force due to Stretch:",FrceStretch)
print("Force Ratio F1:F2:",FRatio)
