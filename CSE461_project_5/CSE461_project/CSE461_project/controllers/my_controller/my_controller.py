from controller import Robot


robot = Robot()

timestep = 2

sensors=[]
sensor_names=["ds_left2","ds_left1","ds_right1","ds_right2", "ds_center"]
sensor_val = [0]*len(sensor_names)

for i in sensor_names:
    sensors.append(robot.getDevice(i))
    sensors[-1].enable(timestep)

motors = []
motor_names = ["right_motor", "left_motor", "right_motor1", "left_motor1"]

for i in motor_names:    
    motors.append(robot.getDevice(i))
    motors[-1].setPosition(float('inf'))
    motors[-1].setVelocity(0.0)
  
previous_error = intg = diff = prop =0.0
kp=3 #3
ki=0.0
kd=1 #0.5

  
def pid(error):
    global previous_error, intg, diff, kp, ki, kd
    prop = error
    intg = error + intg
    diff = error - previous_error
    balance = (kp*prop) + (ki*intg) + (kd*diff) 
    previous_error = error
    return balance
 
    
def setSpeed(base_speed, balance):     
    motors[0].setVelocity(base_speed + balance)
    motors[1].setVelocity(base_speed - balance)
    motors[2].setVelocity(base_speed + balance)
    motors[3].setVelocity(base_speed - balance)

while (robot.step(timestep) != -1):
    for i in range(len(sensors)):
        sensor_val[i] = sensors[i].getValue()
        print(f"{sensor_names[i]} : {sensor_val[i]}\n" + "*"*40) 
        
    if 1000 in sensor_val[0:4]:
        if sensor_val[0] > 950 and sensor_val[1] > 950 and sensor_val[2] <950 and sensor_val[3] < 950:
            setSpeed(5, 0)    
