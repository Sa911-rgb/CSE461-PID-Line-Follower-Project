from controller import Robot


robot = Robot()

timestep = 2



lm=robot.getDevice("left_motor")
rm=robot.getDevice("right_motor")
lm1=robot.getDevice("left_motor1")
rm1=robot.getDevice("right_motor1")


lm.setPosition(float('inf'))
lm.setVelocity(0.0)
rm.setPosition(float('inf'))
rm.setVelocity(0.0)
lm1.setPosition(float('inf'))
lm1.setVelocity(0.0)
rm1.setPosition(float('inf'))
rm1.setVelocity(0.0)



sensors=[]
names=["ds_left2","ds_left1","ds_center","ds_right1","ds_right2"]
reading=[0,0,0,0,0]



previous_error=0.0
kp=3 #3
ki=0.1
kd=0.5 #0.5
Integral=0.0





for i in range (0,5):
    sensors.append(robot.getDevice(names[i]))
    sensors[i].enable(timestep)
    #print("sensor", i)



def getReading():
    for i in range (0,5):
        if int(sensors[i].getValue())>950:
            reading[i]=1
            print("sensor values > 950", sensors[i].getValue())

        else:
            reading[i]=0
            print("sensor values", sensors[i].getValue())

    #print(reading)



def PID():

    error=0

    coefficient=[-1000,-500, 0, 500,1000]

    #[0,0,1,1,0,0,0,0]

    #error=coefficeint[0]*reading[0]+coeffficient[1]*reading[1]+________

    for i in range(0,5):

        error+=coefficient[i]*reading[i]

    P=kp*error

    I=Integral+(ki*error)

    D=kd*(error-previous_error)

    

    

    correction=(P+I+D)/1000

    l_speed=3+correction
    print('l_speed corr', l_speed)

    r_speed=3-correction
    print('r_speed corr', r_speed)
    

    

    if l_speed<0.0  : l_speed=3.0

    if l_speed>10.0 : l_speed=10.0

    if r_speed<0.0  : r_speed=3.0

    if r_speed>10.0 : r_speed=10.0

    

    

    lm.setVelocity(l_speed)
    #print("lm", lm.setVelocity(l_speed))

    rm.setVelocity(r_speed)
    #print("rm", rm.setVelocity(r_speed))
    
    lm1.setVelocity(l_speed)
    #print("lm1", lm1.setVelocity(l_speed))

    rm1.setVelocity(r_speed)
    #print("rm1", rm1.setVelocity(r_speed))
    

    

    print("l_speed, r_speed, reading", l_speed,r_speed,reading)

    

    return I,error



while (robot.step(timestep) != -1):

    getReading()

    print("k values",kp, kd, ki)

    Integral,previous_error=PID()

    pass