from sense_hat import SenseHat

COLLECTION = 'raspberry'
DOCUMENT = 'student-pi'

pi_ref = db.collection(COLLECTION).document(DOCUMENT)

sense = SenseHat()

def data():
	while True:
		pressure = sense.get_pressure()
		temp = sense.get_temperature()
		humidity = sense.get_humidity()