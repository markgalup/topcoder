


class Time(object):

	def whatTime(self, seconds):
		hours = str(seconds / 3600)
		min_secs = seconds % 3600
		mins = str(min_secs / 60)
		secs = str(min_secs % 60)
		
		hms_time = ":".join([hours, mins, secs])
		
		return hms_time
		
test = Time()
print test.whatTime(0)	#Returns: "0:0:0"
print test.whatTime(3661)	#Returns: "1:1:1"
print test.whatTime(5436)	#Returns: "1:30:36"
print test.whatTime(86399)	#Returns: "23:59:59"