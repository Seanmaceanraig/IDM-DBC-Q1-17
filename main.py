import math

#Q01
mass = 1 #kg

#Q02
rollingResistance = mass*0.4 #N

#Q03 (TBC)
totalResistingForce = rollingResistance #N (TBC)

#Q04
powerEfficiency = 0.85

#Q05 (TBC)
motorShaftSpeed = 1 #rev.s-1 (Nm)
motorTorque = 1 #Nm (Tm)
speedOfAxle = 1 #rev.s-1 (Na)
diameterOfMotor = 1 #m (Dm)
diameterOfAxle = 1 #m (Da)
diameterOfWheel = 1 #m (Dw)

vehicleVelocity = math.pi*speedOfAxle*diameterOfWheel #ms-1 (u)
transmissionEfficiency = (speedOfAxle/motorShaftSpeed)/(diameterOfMotor/diameterOfAxle) #(e)
drivingForce = 2*motorTorque*(diameterOfAxle/(diameterOfMotor*diameterOfWheel)) #N (Fd)

print("Section 5:")
print("   Vehicle Velocity:",vehicleVelocity,"m.s-1")
print("   Transmission Efficiency:",transmissionEfficiency)
print("   Driving Force",drivingForce,"N")

#Q06
pulleyRatio = diameterOfAxle/diameterOfMotor

print("\nSection 6:")
print("   Pulley Ratio:",pulleyRatio)

#Q07
#Q08
largePulleyRadius = 1 #m (r1)
smallPulleyRadius = 1 #m (r2)
pulleySeparation = 1 #m (C)
tensionTautPulleySide = 1 #N (F1)
coefficientOfFriction = 0.4 #(mu)

contactAngleBtwnPulleys = math.pi-(2*asin((largePulleyRadius-smallPulleyRadius)/pulleySeparation)) #rad (B)
maxPermitTorque = tensionTautPulleySide*smallPulleyRadius*(1-pow(math.e,coefficientOfFriction*contactAngleBtwnPulleys*-1)) #Nm (Mmax)

lengthStretchedBelt = math.pi*(largePulleyRadius+smallPulleyRadius)+(2*pulleySeparation)+(pow(largePulleyRadius-smallPulleyRadius,2)/pulleySeparation) #m (Lb)

deltaBeltLength = 0 #m (deltaL)
originalBeltLength = 0 #m (L0)
strainInBelt = deltaBeltLength/originalBeltLength #m.m-1 (Epsilon)

if(strainInBelt >= 0 and strainInBelt < 0.1):
    elasticModulus = 6 #MPa (E)
elif(strainInBelt > 0.1 and strainInBelt <= 0.4):
    elasticModulus = 3 #MPa (E)
else:
    raise Exception("Invalid value for strainInBelt. Must be 0 <= strainInBelt <= 0.4.")

stressInBelt = elasticModulus*strainInBelt #MPa.m.m-1 (sigma)

tensionSlackPulleySide = tensionTautPulleySide/(pow(math.e,coefficientOfFriction*contactAngleBtwnPulleys)) #F2
totalTension = tensionSlackPulleySide+tensionTautPulleySide #F

beltCrossSectionalArea = 1 #(m2)
tensionInBelt = totalTension/beltCrossSectionalArea #(sigma)

#Q09
#Q10
#Q11
#Q12
#Q13
#Q14
#Q15
#Q16
#Q17
