# Legal AI Readme

For organizations leveraging AI, the challenge often lies in efficiently processing and transforming unstructured data into usable formats for AI models. Take the legal field, for example, where documents like court case files need to be summarized, tagged, and converted into embeddings before allowing similarity or semantic search and retrieval. Redpanda Connect integrates with OpenAI and other AI services to enable real-time AI-powered data processing. It consumes unstructured data, transforming it via embedding models to generate embeddings for fast, scalable AI workflows.

Link to [video](https://youtu.be/4wgz0OjoYTo)

## Getting Started

To get started with Redpanda Connect and leverage its AI-powered data processing capabilities, follow these steps:

1. Register for Redpanda Serverless: [link to registration page](http://cloud.redpanda.com)

2. Setup Pinecone: [link to Pinecone](https://www.pinecone.io)

3. Register for OpenAI: [link to OpenAI](http://openai.com)

4. Install RPK: [link to RPK installation guide](https://docs.redpanda.com/current/get-started/rpk-install/)

## Usage

Once you have completed the setup, you can use Redpanda Connect for legal AI workflows by following these steps:

1. Create an `.env` file to save the environment variables required for Redpanda Connect. 

    ```bash
    OPENAI_API_KEY=""
    RP_BOOTSTRAP_SERVER=""
    RP_SASL_MECHANISM=""
    RP_USER_USERNAME=""
    RP_USER_PASSWORD=""
    PINECONE_HOST=""
    PINECONE_API_KEY=""
    ```

2. Run `legal-load.yaml` to load the necessary data.

    ```bash
    rpk connect run -e .env legal-load.yaml
    ```

3. Run `legal-converter` locally or deploy it on Redpanda Serverless.
   ```bash
    rpk connect run -e .env legal-converter.yaml
    ```

## Querying Court Cases

To query the court cases using the `query.py` script, follow these steps:

1. Make sure you have created the `.env` file and saved the required environment variables for Redpanda Connect.

2. Open a terminal or command prompt and navigate to the directory where the `query.py` script is located.

    ```bash
    python3 -m venv env
    pip install -r  requirements.txt
    ```
3. Run the following command to execute the script:

    ```bash
    export $(grep -v '^#' .env | xargs)
    python3 query.py
    ```

    This will initiate the query process and retrieve relevant information from the court cases.

4. Review the output or specify additional parameters in the script to customize the query results.

Remember to adjust the script according to your specific requirements and ensure that the necessary dependencies are installed.
