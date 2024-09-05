
# Connect Demo Object Store

This repository contains the necessary steps to efficiently store large volumes of streaming data for long-term analysis using Redpanda Connect and ClickHouse.
[Video](https://www.youtube.com/watch?v=1LOoGSdHtsQ)

## Starting simulator and deploy data pipeline

Before getting started, make sure you have completed the following steps:

1. Sign up for Redpanda Serverless.
2. Set up environment variables by creating a `.env` file. Create an `.env` file to save the environment variables required for Redpanda Connect. 

    ```bash
    RP_BOOTSTRAP_SERVER=""
    RP_SASL_MECHANISM=""
    RP_USER_USERNAME=""
    RP_USER_PASSWORD=""
    ```

    Set the environment variable 
    ```bash
    export $(grep -v '^#' .env | xargs)
    ```
3. Run `music_logger.py` to start simulating music logs


    ```bash
    python3 -m venv env
    pip install -r  requirements.txt
    ```
    Run the following command to execute the script:

    ```bash
    python3 music_logger.py
    ```
4. Deploy the `music_log_store.yaml` on Redpanda Server, and update the required credentials.


## Setting up ClickHouse

To set up ClickHouse and configure the necessary tables, follow these steps:

1. Create a Docker network:

```bash
docker network create clickhouse-network
```

2. Run the ClickHouse server container:

```bash
docker run -d \
    --name demo-clickhouse-server \
    --ulimit nofile=262144:262144 \
    --network clickhouse-network \
    -p 18123:8123 \
    -p 19000:9000 \
    clickhouse/clickhouse-server
```

3. Access the ClickHouse client:

```bash
docker exec -it demo-clickhouse-server clickhouse-client
```

4. Set up the `music_logs_s3_raw` table:

```sql
CREATE TABLE music_logs_s3_raw (
        user_id UUID,
        gender String,
        geo String,
        music_type String,
        listening_device String,
        year_of_music UInt16,
        song_id UUID,
        timestamp DateTime
) ENGINE = S3('https://your-s3-bucket-name.s3.amazonaws.com/logs/*','your-access-key', 'your-secret-key', JSONEachRow);
```

## Running Statistics Queries

Once the setup is complete, you can run various statistics queries on the `music_logs_s3_raw` table:

### Most Listened Device

```sql
SELECT
        listening_device,
        COUNT(*) AS listen_count
FROM
        music_logs_s3_raw
GROUP BY
        listening_device
ORDER BY
        listen_count DESC
LIMIT 1;
```

### Music Types Ranking for "Smart Speaker"

```sql
SELECT
        music_type,
        COUNT(*) AS listen_count
FROM
        music_logs_s3_raw
WHERE
        listening_device = 'Smart Speaker'
GROUP BY
        music_type
ORDER BY
        listen_count DESC;
```

### Music Types Ranking for "Car"

```sql
SELECT
        music_type,
        COUNT(*) AS listen_count
FROM
        music_logs_s3_raw
WHERE
        listening_device = 'Car'
GROUP BY
        music_type
ORDER BY
        listen_count DESC;
```

### Most Listened Eras (Years) for Jazz Music

```sql
SELECT
        year_of_music,
        COUNT(*) AS listen_count
FROM
        music_logs_s3_raw
WHERE
        music_type = 'Jazz'
GROUP BY
        year_of_music
ORDER BY
        listen_count DESC;
```

Remember to replace `https://your-s3-bucket-name.s3.amazonaws.com/logs/*`, `your-access-key`, and `your-secret-key` with the appropriate values.

