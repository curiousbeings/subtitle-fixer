subtitles={}
subtitles={"count":1,"start_time":{"1":""},"end_time":{"1":""},"subtitles":[]}


def delay_hasten(operate_on,delay_hasten_by_value):		#function to delay or hasten the subtitle
	sec=int(operate_on[2])
	min=int(operate_on[1])
	hour=int(operate_on[0])
	if sec+delay_hasten_by_value > 59:
		sec = 60-sec+delay_hasten_by_value
		min+=1
	else:
		sec+=delay_hasten_by_value
	if len(str(sec))==1:
		operate_on[2]="0"+str(sec)
	elif sec==0:
		operate_on[2]="00"
	else:
		operate_on[2]=str(sec)
		
	if len(str(min))==1:
		operate_on[1]="0"+str(min)
	elif min==0:
		operate_on[1]="00"
	else:
		operate_on[1]=str(min)
	#print sec
	return operate_on

	
def create_sub_file(path,delay_hasten_by_value,target):
	with open(path,"rb") as fo:
		write_file=open(target,"wb")
		#write_file.write("1")
		#write_file.close()
		b= fo.read(1)
		i=1
		while b!="": #check end of file
		
			if(b=="\r" and fo.read(1) =="\n"):    #check for first occurrence of line break
				write_file.write("\r\n")			#Write that line break as it is
				b=fo.read(1)
				if(b=="\r"and fo.read(1)=="\n"):	#check for a consecutive line break. If true means a new subtitle is starting
					subtitles["count"]+=1			#Add to the count of total subtitles
					subtitles["start_time"][str(subtitles["count"])]="" 	
					subtitles["end_time"][str(subtitles["count"])]=""
					write_file.write("\r\n")
					i=1
				elif(i==1):							#here start collecting the start and end time of a sub
					while b!=" ":
						subtitles["start_time"][str(subtitles["count"])]+=b
						b=fo.read(1)
					start_time=""
					seperated_time = subtitles["start_time"][str(subtitles["count"])].split(",")
					mil_sec = seperated_time[1]
					operate_on = seperated_time[0].split(":")
					#print operate_on
					if(operate_on[1]>delay_hasten_by_value):
						start_time=":".join(delay_hasten(operate_on,delay_hasten_by_value)) + "," + mil_sec
						#print start_time
					#write_file.write(subtitles["start_time"][str(subtitles["count"])])
					write_file.write(start_time)
					write_file.write(" ")
					b=fo.read(4)				
					write_file.write(b)				#writes "--> "
					b=fo.read(1)
					while b!="\r":
						subtitles["end_time"][str(subtitles["count"])]+=b
						b=fo.read(1)
					end_time=""
					seperated_time = subtitles["end_time"][str(subtitles["count"])].split(",")
					mil_sec = seperated_time[1]
					operate_on = seperated_time[0].split(":")
					#print operate_on
					if(operate_on[1]>delay_hasten_by_value):
						end_time=":".join(delay_hasten(operate_on,delay_hasten_by_value)) + "," + mil_sec
					write_file.write(end_time)
					i=2
			else:				#if nota then this is the subtitle, write it as it is
				write_file.write(b)
			b=fo.read(1)
	write_file.close()
	

