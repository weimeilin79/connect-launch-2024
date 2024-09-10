import random
import time
import json
import uuid
import signal
import sys
import os
from kafka import KafkaProducer


# Function to generate random user music listening log
def generate_music_log():
    user_id = str(uuid.uuid4())
    gender = random.choice(["Male", "Female", "Non-binary"])
    geo = random.choice(["North America", "Europe", "Asia", "South America", "Africa", "Australia"])
    music_type = random.choice(["Pop", "Rock", "Hip-Hop", "Classical", "Jazz", "Electronic", "Country"])
    listening_device = random.choice(["Mobile", "Desktop", "Tablet", "Smart Speaker", "Car"])
    year_of_music = random.choice([str(year) for year in range(1950, 2024)])
    song_id = str(uuid.uuid4())
    
    log = {
        "user_id": user_id,
        "gender": gender,
        "geo": geo,
        "music_type": music_type,
        "listening_device": listening_device,
        "year_of_music": year_of_music,
        "song_id": song_id
    }
    
    return log

producer = None

# Graceful shutdown handler
def signal_handler(sig, frame):
    print("\nGracefully stopping the log generator...")
    global producer  
    producer.close()  
    sys.exit(0)

# Main function to generate logs and send them to Kafka
def main():
    global producer  

    try:
        # Set up Kafka producer
        producer = KafkaProducer(
            bootstrap_servers=os.environ["RP_BOOTSTRAP_SERVER"],  
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        )

        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        topic_name = 'music-listening-logs'
        
        print("Starting the log generator. Press Ctrl+C to stop.")
        while True:
            for _ in range(200):  # Generate 200 records per second
                log = generate_music_log()
                producer.send(topic_name, value=log)
            time.sleep(1)  # Wait for 1 second before generating the next batch

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if producer is not None:
            print("Closing producer in finally block...")
            producer.close()
        print("Producer closed.")

if __name__ == "__main__":
    main()