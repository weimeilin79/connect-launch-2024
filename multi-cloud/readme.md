# Multi-Cloud Data Consolidation

One of the most common challenges in modern data pipelines is consolidating data from various sources, especially in multi-cloud environments. Each source may have its own format, protocol, or even data measurement units. This can make it difficult to ensure a unified and normalized data stream.

In this guide, we will walk you through the process of setting up a multi-cloud data consolidation pipeline using AWS SQS and an SFTP server hosted on Google Cloud. We will also explore how to address the complexities introduced by different protocols, security requirements, and data formats.

Let's get started! [Video](https://youtu.be/b0t6E3xKtAc)

## Step 1: Sign up for Redpanda Serverless

Before we begin, you will need to sign up for Redpanda Serverless. Redpanda is a scalable and high-performance messaging platform that will serve as the backbone of our data consolidation pipeline. Visit the Redpanda website and follow the sign-up instructions to create an account.

## Step 2: Setup AWS SQS

Next, we will set up AWS Simple Queue Service (SQS) to collect data from various sources. SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

To set up SQS, follow these steps:

1. Log in to your AWS Management Console.
2. Navigate to the SQS service.
3. Create a new queue and configure its settings according to your requirements.
4. Take note of the queue URL and access credentials, as we will need them later in the pipeline setup.

## Step 3: Setup SFTP Server on Google Cloud

We will also collect data from an SFTP server hosted on Google Cloud. Setting up an SFTP server on Google Cloud involves the following steps:

1. Log in to your Google Cloud Console.
2. Navigate to the Compute Engine service.
3. Create a new virtual machine instance and configure it as an SFTP server.
4. Configure the necessary firewall rules and network settings to allow inbound connections to the SFTP server.
5. Take note of the server's IP address, username, and password, as we will need them later in the pipeline setup.

That's it! You have now set up the foundation for your multi-cloud data consolidation pipeline. In the next steps, we will explore how to integrate these components and ensure a unified and normalized data stream.


## Step 4: Run the SFTP & SQS Simulator

To generate data simulating the signal generated by the submarine, we will run the SFTP and SQS simulator using rpk command line tool. 

Make sure you have the following prerequisites in place before running the simulator:

1. Install Redpanda Serverless and set up the necessary environment variables in the `.env` file.
2. Configure the simulator settings in the `.env` file, including the SFTP server details and SQS queue URL.

    ```bash
    YOUR_SFTP_SERVER=""
    YOUR_SFTP_USERNAME=""
    YOUR_SFTP_PASSWORD=""
    YOUR_SQS_URL=""
    YOUR_AWS_REGION=""
    YOUR_AWS_ID=""
    YOUR_AWS_SECRET=""
    RP_BOOTSTRAP_SERVER=""
    RP_SASL_MECHANISM=""
    RP_USER_USERNAME=""
    RP_USER_PASSWORD=""
    ```

    Set the environment variable 
    ```bash
    export $(grep -v '^#' .env | xargs)
    ```


3. This command will start the simulator and generate data that mimics the real-time signal.
    ```bash
    rpk connect run -e .env sqs-simulator` 
    ```

    ```bash
    rpk connect run -e .env sftp-simulator` 
    ```

This will start the simulator and begin generating simulated data. You can monitor the data flow and verify its accuracy by checking the logs and monitoring the SQS queue.



## Step 5: Deploy data convergence pipeline

To complete the data consolidation pipeline, we need to deploy the data convergence pipeline that consumes data from both the SQS queue and the SFTP server. Follow these steps to deploy the pipeline:

1. Open the `demo-sftp.yaml` and `demo-sqs.yaml` files.
2. Update the settings and credentials in the YAML files according to your specific configuration.
3. Copy the contents of the YAML files.
4. Go to the Redpanda Serverless connector page.
5. Paste the pipeline configuration into the connector page.
6. Save the configuration and deploy the pipeline.

Once the pipeline is deployed, it will start consuming data from the SQS queue and the SFTP server, consolidating the data into a unified and normalized data stream.
You have successfully deployed the data convergence pipeline in a serverless environment, enabling the consolidation of data from multiple sources.


# Step 6: Start the Node.js App in Submarine Monitoring

To access the submarine monitoring application, follow these steps:

1. Set the environment variable by running the following command:
   ```bash
   cd submarine-monitoring
   export $(grep -v '^#' .env | xargs)
   ```

2. Install the necessary dependencies by running the following command:
   ```bash
   npm install
   ```

3. Start the Node.js app by running the following command:
   ```bash
   node index.js
   ```

4. Access the application by navigating to `localhost:3000` in your web browser.

Congratulations! You have successfully set up and run the SFTP and SQS simulator, generating data that simulates the signal generated by the submarine.


