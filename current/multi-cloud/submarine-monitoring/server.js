const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const { Kafka } = require('kafkajs');

// Initialize Express
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files
app.use(express.static('public'));

// Kafka Consumer Setup with KafkaJS
const kafka = new Kafka({
    clientId: 'submarine-monitoring-12',  // Your client ID
    brokers: `redpanda:19092`,  // Redpanda Cloud broker
});

const consumer = kafka.consumer({ groupId: 'submarine-monitoring-group' });

const run = async () => {
    // Connect the consumer
    await consumer.connect();
    await consumer.subscribe({ topic: 'mariana_trench', fromBeginning: true });

    // Listen for messages
    await consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
            const submarineData = JSON.parse(message.value.toString());
            io.emit('submarineData', {
                timestamp: submarineData.timestamp,
                depth: submarineData.depth,
                pressure_mpa: submarineData.pressure_mpa,
                temperature: submarineData.temperature,
                signal_strength_db: submarineData.signal_strength_db
            });
        }
    });
};

run().catch(console.error);

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
