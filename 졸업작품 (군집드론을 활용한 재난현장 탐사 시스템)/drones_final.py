# -*- coding: utf-8 -*-
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative, Vehicle, Command
from pymavlink import mavutil
import json, math, time, sys, ssl, threading
import logging, logging.handlers, traceback
import argparse 

parser = argparse.ArgumentParser(description='Commands vehicle using Amazon Echo.')
parser.add_argument('--connect', help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

drone_speed = 2

if args.connect == "sitl":
	connection_string = ['tcp:127.0.0.1:5760']
	print "Start simulator (SITL)"
	from dronekit_sitl import SITL
	sitl = SITL()
	sitl.download('copter', '3.3', verbose=True)
	sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
	sitl.launch(sitl_args, await_ready=True, restart=True)
elif args.connect == "solo":
	connection_string = ['udpin:0.0.0.0:12550','udpin:0.0.0.0:13550','udpin:0.0.0.0:14550', 'udpin:0.0.0.0:16550', 'udpin:0.0.0.0:19550', 'udpin:0.0.0.0:16550', 'udpin:0.0.0.0:19550', 'udpin:0.0.0.0:19550']
else:
	print "wrong argument: " + args.connect
	sys.exit()

def normalize_yaw(angle):
	if angle < 0:
		angle = (2 * math.pi) + angle
	
	return angle

def calc_xy (distance, angle, units = 'radians'):
	if units != 'radians':
		angle = math.radians(angle)
	
	angle = normalize_yaw(angle)
	x = distance * (math.cos(angle))
	y = distance * (math.sin(angle))

	return (round (x, 1), round (y, 1))

def arm_and_takeoff(aTargetAltitude, vehicle, num):
	errcnt = 0

	print "Basic pre-arm checks"

	while not vehicle.is_armable:
		print " Waiting for vehicle to initialise..."
		time.sleep(1)

	print "Arming motors"

	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True    

	while not vehicle.armed:      
		print " Waiting for arming..."
		time.sleep(1)

	print "Taking off!"
	vehicle.simple_takeoff(aTargetAltitude)

	while True:
		print " %d's Altitude: "%(num+1), vehicle.location.global_relative_frame.alt         
		if vehicle.location.global_relative_frame.alt>=aTargetAltitude - 1: 
			print "%d's Reached target altitude\n"%(num+1)
			break
		elif vehicle.location.global_relative_frame.alt < 0.15:
			errcnt += 1

		if errcnt > 5:
			break
		time.sleep(1)

def takeland(vehicle, num):
	vehicle.mode = VehicleMode("LAND")
	vehicle.flush()

def do_go(direction, distance, my_yaw, vehicle, num):
	
	print 'my_yaw = %s' % my_yaw

	if direction == 'forward':
		my_direction = my_yaw
	elif direction == 'back':
		my_direction = (my_yaw + math.pi) % (2*math.pi)
	elif direction == 'right':
		my_direction = (my_yaw + (math.pi / 2)) % (2*math.pi)
	elif direction == 'left':
		my_direction = (my_yaw + (math.pi * 1.5)) % (2*math.pi)
	elif direction == 'up':
		change_altitude(distance, vehicle, num)
		return
	elif direction == 'down':
		change_altitude(distance * -1, vehicle, num)
		return
	
	print my_direction
	my_xy = calc_xy(distance, my_direction)
	goto(my_xy[0], my_xy[1], vehicle, num)

def do_go_zigzag(direction, distance, my_yaw, vehicle, num):
	
	print 'my_yaw = %s' % my_yaw

	if direction == 'Left_up':
		my_direction = (my_yaw + (math.pi * 1.75)) % (2*math.pi)
	elif direction == 'Right_up':
		my_direction = (my_yaw + (math.pi * 0.25)) % (2*math.pi)
	
	print my_direction
	my_xy = calc_xy(distance, my_direction)
	goto(my_xy[0], my_xy[1], vehicle, num)

def goto(dNorth, dEast, vehicle, num):
	currentLocation = vehicle.location.global_relative_frame
	targetLocation = get_location_metres(currentLocation, dNorth, dEast)
	vehicle.simple_goto(targetLocation, drone_speed)

	while vehicle.mode.name == "GUIDED":
		remainingDistance = get_distance_metres(vehicle.location.global_relative_frame, targetLocation)
		print "%d's Distance to target : "%(num+1), remainingDistance
		if remainingDistance <= 1:
			print "%d's Reached target\n"%(num+1)
			break
		time.sleep(2)	

def change_altitude(meters_up, vehicle, num):

	vehicle.mode = VehicleMode("GUIDED")

	if vehicle.location.global_relative_frame.alt + meters_up < 3:
		print "Warning : Too close to the ground! Command discarded."
		return
	
	a_location = LocationGlobalRelative(vehicle.location.global_frame.lat, vehicle.location.global_frame.lon, vehicle.location.global_relative_frame.alt + meters_up)
	vehicle.simple_goto(a_location, drone_speed)

	while vehicle.mode.name == "GUIDED":
		remainingDistance = abs(a_location.alt - vehicle.location.global_relative_frame.alt)
		print "%d's Distance to target : "%(num+1), remainingDistance
		if remainingDistance <= 1:
			print "%d's Reached target\n"%(num+1)
			break
		time.sleep(2)
	vehicle.flush()

def thread_start(vehicle_list, func, arg = (), delay_time = 0):
	vehicle_thread_list = []
	num = 0
	for vehicle in vehicle_list:
		vehicle_thread = threading.Thread(target=func, args=arg + (vehicle, num))
		vehicle_thread_list.append(vehicle_thread)
		num += 1

	for t in vehicle_thread_list:
		t.start()
		time.sleep(delay_time)
	
	for t in vehicle_thread_list:
		t.join()

def do_save(Point, vehicle, num):
	print "%d's Departure to Point" %(num+1)
	point = Point[num]	
	vehicle.simple_goto(point, drone_speed)

	while vehicle.mode.name == "GUIDED":
		remain= get_distance_metres(vehicle.location.global_relative_frame, point)
		print "%d's Distance to target: "%(num+1),remain
		if remain <= 1:
			print "%d's Reached target\n"%(num+1)
			break
		time.sleep(2)

def do_save2(Point, vehicle, num):
	print "%d's Departure to Point" %(num+1)
	point = Point	
	vehicle.simple_goto(point, drone_speed)

	while vehicle.mode.name == "GUIDED":
		remain= get_distance_metres(vehicle.location.global_relative_frame, point)
		print "%d's Distance to target: "%(num+1),remain
		if remain <= 1:
			print "%d's Reached target\n"%(num+1)
			break
		time.sleep(2)

def get_distance_metres(aLocation1, aLocation2):
	dlat = aLocation2.lat - aLocation1.lat
	dlong = aLocation2.lon - aLocation1.lon
	return math.sqrt((dlat * dlat) + (dlong * dlong)) * 1.113195e5

def get_location_metres(original_location, dNorth, dEast):
	earth_radius = 6378137.0 

	dLat = dNorth / earth_radius #
	dLon = dEast / (earth_radius * math.cos (math.pi * original_location.lat / 180))

	newlat = original_location.lat + (dLat * 180 / math.pi)
	newlon = original_location.lon + (dLon * 180 / math.pi)

	if type(original_location) is LocationGlobal:
		targetLocation = LocationGlobal(newlat, newlon, original_location.alt)
	elif type(original_location) is LocationGlobalRelative:
		targetLocation = LocationGlobalRelative(newlat, newlon, original_location.alt)
	else:
		raise Exception("Invalid Location object passed")

	return targetLocation


def go_wave(vehicle, num):

	change_altitude(5, vehicle, num)
	change_altitude(-7, vehicle, num)
	change_altitude(5, vehicle, num)
 

def do_go_OneGPS(distance, my_yaw,lati,longit, vehicle, num, direction,drone_altitude):
	
	print 'my_yaw = %s' % my_yaw

	if direction == 'Left_down':
		my_direction = (my_yaw + (math.pi * 1.25)) % (2*math.pi)
	elif direction == 'Left_up':
		my_direction = (my_yaw + (math.pi * 1.75)) % (2*math.pi)
	elif direction == 'Right_up':
		my_direction = (my_yaw + (math.pi * 0.25)) % (2*math.pi)
	elif direction == 'Right_down':
		my_direction = (my_yaw + (math.pi * 0.75)) % (2*math.pi)
	
	
	print my_direction
	my_xy = calc_xy(distance, my_direction)
	goto_OneGPS(my_xy[0], my_xy[1], vehicle, num,lati,longit,drone_altitude)

def goto_OneGPS(dNorth, dEast, vehicle, num,lati,longit,drone_altitude): 
	currentLocation = vehicle.location.global_relative_frame  
	currentLocation.lat = lati
	currentLocation.lon = longit
	currentLocation.alt = drone_altitude 
	targetLocation = get_location_metres(currentLocation, dNorth, dEast)
	vehicle.simple_goto(targetLocation, drone_speed)

	while vehicle.mode.name == "GUIDED":
		remainingDistance = get_distance_metres(vehicle.location.global_relative_frame, targetLocation)
		print "%d's Distance to target : "%(num+1), remainingDistance
		if remainingDistance <= 1:
			print "%d's Reached target\n"%(num+1)
			break
		time.sleep(2)	

def thread_start_OneGPS(vehicle_list, func, arg = (), delay_time = 0): 
	vehicle_thread_list = []
	direction_OneGPS = ["Left_down","Left_up", "Right_up" ,"Right_down"]

	drone_altitude = [6,10,10,6] 

	num = 0
	for vehicle in vehicle_list:
		vehicle_thread = threading.Thread(target=func, args=arg + (vehicle, num, direction_OneGPS[num],drone_altitude[num])) 
		vehicle_thread_list.append(vehicle_thread)
		num += 1

	for t in vehicle_thread_list:
		t.start()
		time.sleep(delay_time)
	
	for t in vehicle_thread_list:
		t.join()


def do_go_mode_two(distance, my_yaw,lati,longit, vehicle, num, direction): 

	a = [(distance*3)/2, distance/2,distance/2, (distance *3)/2]
	 
	print 'my_yaw = %s' % my_yaw

	if direction == 'Left':
		my_direction = (my_yaw + (math.pi * 1.5)) % (2*math.pi)
	elif direction == 'Right':
		my_direction = (my_yaw + (math.pi / 2)) % (2*math.pi)
	
	
	print my_direction
	my_xy = calc_xy(a[num], my_direction)
	goto_mode_two(my_xy[0], my_xy[1], vehicle, num,lati,longit)

def goto_mode_two(dNorth, dEast, vehicle, num,lati,longit): 
	currentLocation = vehicle.location.global_relative_frame  
	currentLocation.lat = lati
	currentLocation.lon = longit
	targetLocation = get_location_metres(currentLocation, dNorth, dEast)
	vehicle.simple_goto(targetLocation, drone_speed)

	while vehicle.mode.name == "GUIDED":
		remainingDistance = get_distance_metres(vehicle.location.global_relative_frame, targetLocation)
		print "%d's Distance to target : "%(num+1), remainingDistance
		if remainingDistance <= 1:
			print "%d's Reached target\n"%(num+1)
			break
		time.sleep(2)	

def thread_start_mode_two(vehicle_list, func, arg = (), delay_time = 0): 
	vehicle_thread_list = []
	direction_OneGPS = ["Left","Left", "Right" ,"Right"]
	num = 0
	for vehicle in vehicle_list:
		vehicle_thread = threading.Thread(target=func, args=arg + (vehicle, num, direction_OneGPS[num])) 
		vehicle_thread_list.append(vehicle_thread)
		num += 1

	for t in vehicle_thread_list:
		t.start()
		time.sleep(delay_time)
	
	for t in vehicle_thread_list:
		t.join()



if __name__ == '__main__':

	vehicle_list = []
	home_gps_list = []

	circle_center = None
	rad = None

	drone_num = input("Please enter the number of drones : ")
	
	for i in range(drone_num):
		print "Connecting to vehicle on : " + connection_string[i]
		vehicle = connect(connection_string[i], wait_ready=True)
		vehicle_list.append(vehicle)
		print vehicle.location.global_relative_frame
				
	my_yaw = vehicle_list[0].attitude.yaw
	while True:

		menu_num = raw_input("""1.Command Launch\n2.End\nWhat command do you want : """)

		if menu_num == "1":
			input_alt = input("""Please enter an altitude : """)

			thread_start(vehicle_list, func = arm_and_takeoff, arg = (input_alt,))

			home_gps_list[:] = []
			for i in range(drone_num):
				
				home_gps_list.append(vehicle_list[i].location.global_relative_frame)

			while True:
				menu_num = raw_input("""1.Go\n2.Command Land\n3.Make wave\n4.return home\n5.Point\n6.GPS Value\n7.Go_Spread\n8.Go_Square\n9.Go_Zigzag\n10.Multi Point\n\nWhat command do you want : """)
				print '\n'

				if menu_num == '1':
					try:
						direction_menu = raw_input("""1.Forward\n2.Right\n3.Left\n4.Backward\n5.Up\n6.Down\nPlease select a direction : """)
						direction_num = int(direction_menu)
						direction_array = ["forward", "right", "left", "back", "up", "down"]
						print "\n"
						distance = input("Distance : ")
						print "\n"
						direction = direction_array[direction_num - 1]
					except ValueError:
						print 'Wrong input\n'

					thread_start(vehicle_list, func = do_go, arg=(direction, distance, my_yaw))

				elif menu_num == '2':
					thread_start(vehicle_list, func = takeland)
					break
									
	
				elif menu_num == '3':

					thread_start(vehicle_list, func = go_wave, delay_time=2)

				elif menu_num == '4':

					thread_start(vehicle_list, func = do_save, arg=(home_gps_list, ))	

				elif menu_num == '5':
					gps_list_lati = []
					gps_list_longi = []
					number = input("How many GPS coordinates are you going to enter? :")

					for i in range(number):
						print "Please enter the %d's gps " %(i+1)
						lati = input("Latitude : ")
						longi = input("Longitude : ")
						gps_list_lati.append(lati)
						gps_list_longi.append(longi)
						print "\n"

					for i in range(number):
						gps = vehicle_list[0].location.global_relative_frame 
						gps.lat = gps_list_lati[i]
						gps.lon = gps_list_longi[i]						
									
						thread_start(vehicle_list, func = do_save2, arg=(gps, )) 
						print vehicle.location.global_relative_frame

				elif menu_num == '6':
					for i in range(drone_num):
						gps = vehicle_list[i].location.global_relative_frame
						print "%d's Current GPS :" %(i+1),gps 	
					print '\n'


				elif menu_num == '7':			         
					
					lati = input("""Latitude : """) 
					longi = input("""Longitude : """) 
					
					while True :						
						
						interval = 8
						#distance = input("""Distance" : """)
 						
						if distance >= 50.0 :

							thread_start_mode_two(vehicle_list, func = do_go_mode_two, arg=(interval, my_yaw,lati,longi)) 
								
							direction_array = ["forward", "right", "left", "back", "up", "down"]
							direction = direction_array[2]
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/drone_num, my_yaw)) 
							direction = direction_array[3]
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/drone_num, my_yaw)) 
							direction = direction_array[1]
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/drone_num, my_yaw)) 
							direction = direction_array[0]
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/drone_num, my_yaw)) 
						
							thread_start(vehicle_list, func = do_save, arg=(home_gps_list, ))	
							break
						else :
							print "Too short distance(At least 50m)"						
								  			

				elif menu_num == '8':					
					
										
					lati = input("""Latitude : """) 
					longi = input("""Longitude : """) 
					
					while True:
												
						interval = 10 
						distance = input(""""Distance : """")

						if distance >=30.0:

							thread_start_OneGPS(vehicle_list, func = do_go_OneGPS, arg=(interval, my_yaw,lati,longi)) 

					
							direction_array = ["forward", "right", "left", "back", "up", "down"]
							direction = direction_array[2]
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/2, my_yaw))
							direction = direction_array[3]
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/2, my_yaw))
							direction = direction_array[1]
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/2, my_yaw)) 
							direction = direction_array[0]							
							thread_start(vehicle_list, func = do_go, arg=(direction, distance/2, my_yaw))
						
							thread_start(vehicle_list, func = do_save, arg=(home_gps_list, ))	
							break
						else :
							print "Too short distance(At least 30m)"

				elif menu_num == '9':
					
					lati = input("""Latitude : """) 
					longi = input("""Longitude : """) 
					
					while True :						
						
						interval = 8
						distance = input("""Distance" : """)
						
						diagonal = 10 
						length = math.sqrt((diagonal*diagonal)-(interval*interval))  
						repeat = int(distance/length) 

						if distance >= 25.0 : 
								
							direction_array = ["Left_up",'Right_up']
							
							remainder =0
							for i in range(repeat):
								remainder = remainder%2 
								thread_start(vehicle_list, func = do_go_zigzag, arg=(direction_array[remainder], diagonal, my_yaw)) 
								
								remainder += 1
								
							thread_start(vehicle_list, func = do_save, arg=(home_gps_list, ))	
							break
						else :
							print "Too short distance(At least 25m)"						

					
							
				elif menu_num == '10':
					gps_list = []
					for i in range(drone_num):
						print "Please enter the gps of drones " , i+1
						gps = vehicle_list[i].location.global_relative_frame 
						gps.lat = input("""Latitude : """)
						gps.lon = input("""Longitude : """)
						gps.alt = input("""Altitude : """)
										
						gps_list.append(gps)

					thread_start(vehicle_list, func = do_save, arg=(gps_list, )) 
				else:
					continue
				

		else:
			break