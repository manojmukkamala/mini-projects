from pyspark.sql import SparkSession

# Configuration
APP_NAME = "spark-test"
MASTER_URL = "spark://rpi-node-01:7077"

def main():
    print(f"Initializing Spark Session... connecting to {MASTER_URL}")
    
    # 1. Initialize Spark Session
    spark = SparkSession.builder \
        .master(MASTER_URL) \
        .appName(APP_NAME) \
        .config("spark.dynamicAllocation.enabled", "true") \
        .config("spark.shuffle.service.enabled", "true") \
        .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("ERROR") # Keep logs clean to see the result clearly

    try:
        # 2. Create a distributed dataset
        # We use a range of 1M numbers and split them into 10 partitions.
        # This forces Spark to distribute the data across your Pi workers.
        print("Dispatching distributed workload to workers...")
        data = sc.parallelize(range(1, 1000000001), 12)

        # 3. Perform an Action
        # .count() is an action that requires every partition to report back.
        # If the network is broken, this is where the script will hang.
        result = data.count()
        
        print("\n" + "="*30)
        print(f"SUCCESS: Distributed count completed.")
        print(f"Total Elements: {result}")
        print("="*30)

    except Exception as e:
        print(f"\nFAILURE: An error occurred during execution:\n{e}")
    finally:
        spark.stop()
        print("Spark Session closed.")

if __name__ == "__main__":
    main()