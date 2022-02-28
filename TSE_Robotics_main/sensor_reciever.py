import socket, threading, os

HOST, PORT = "localhost", 8080

def save_data(log_file, data): #Append the data to a log file
    data = data.split(",")[0]#remove comma to add before if one doesnt exist
    if (os.path.exists(log_file)):
        data=","+data
    with open(log_file, "a+") as f:
        f.write(data)
        
def get_sensor_type(conn): # Get the sensor type, and set the log file
    sensor_type=conn.recv(1024).decode() #Get sensor type
    if sensor_type == "ph_sensor" or sensor_type == "oxygen_sensor" or sensor_type=="temperature_sensor" or "co2_sensor":
        sensor_name= sensor_type.split("_")[0]
        log_file = sensor_name+".csv"
        return log_file
    else:
        print("Error no data recieved!")
    
def recieveData(conn, addr):
    print("Sensor Connected with address: ", addr[0])
    with conn:
        conn.settimeout(5)
        log_file=get_sensor_type(conn)
        while True:
            try:
                data = conn.recv(1024).decode() #Recieve data
                print(data)
                if not data: break #Break if no data was recieved
                print(data)
                save_data(log_file,data)
            except Exception as s:
                print("Error:", s)
                break
        print("Sensor has disconnected")
        

def listen(): # Listen for incoming connections
    print("Waiting for connections...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT)) #Bind to specified host and port
        while True:
            sock.listen() #Listen for incoming connections
            conn, addr = sock.accept() #Accept the connection
            t = threading.Thread(target=recieveData, args=(conn, addr)) #New thread to run recieve data function
            t.start() #Start the new thread

if __name__ == '__main__':
    #Start socket
    SERVER = threading.Thread(target=listen)
    SERVER.start()
