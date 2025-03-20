create database company;
create table employees (
    customerID VARCHAR(100) PRIMARY KEY,
    gender VARCHAR(100),
    SeniorCitizen VARCHAR(100),	
    Partner VARCHAR(100),	
    Dependents VARCHAR(100),	
    tenure VARCHAR(100),	
    PhoneService VARCHAR(100),	
    MultipleLines VARCHAR(100),	
    InternetService VARCHAR(100),	
    OnlineSecurity VARCHAR(100),
    OnlineBackup VARCHAR(100),	
    DeviceProtection VARCHAR(100),	
    TechSupport	VARCHAR(100),
    StreamingTV	VARCHAR(100),
    StreamingMovies	VARCHAR(100),
    Contract VARCHAR(100),	
    PaperlessBilling VARCHAR(100),	
    PaymentMethod VARCHAR(100),	
    MonthlyCharges VARCHAR(100),	
    TotalCharges VARCHAR(100),	
    Churn VARCHAR(100) 
);
SHOW VARIABLES LIKE 'secure_file_priv';
SET GLOBAL local_infile = 1;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\WA_Fn-UseC_-Telco-Customer-Churn.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


		