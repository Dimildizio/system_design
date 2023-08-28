# System Design Doc Template 

Oh, exploitable!

## ML System design - < Project > < MVP or Production System > < Num >


#### Vocabulary 

> Iteration - complete necessary routine to start a running small-scale working pilot
 
> BR - business requirements 
 
> EDA - Exploratory Data Analysis
 
> `Product Owner`, `Data Scientist` - roles

### 1. Goals

#### 1.1 Why do we start developing the product?

- Business goal - `Product Owner`

- Why would using ML be more efficient than current soluton? - `Product Owner` `Data Scientist`

- What should be considered as an `iteration` success form business point of view - `Product Owner`


#### 1.2. Business requirements and limitations  

- Brief BR description and links to comprehensive BR documents - `Product Owner`  
- Business limitations - `Product Owner`  
- What is expected from each `iteration` - `Product Owner`. 
- Product business process description (BPMN), how will the model be use in the current business process - `Product Owner`    
- What is considered a successful pilot? List different ways to develop the project - `Product Owner`

#### 1.3. Project\Iteration scope    

- What business requirements are expected to be fulfilled in a current iteration - `Data Scientist`   
- What is not going to be be fulfilled this iteration - `Data Scientist`  
- Describe the project from the clean code and replicability potential point of view - `Data Scientist`  
- Describe expected technical debt - `Data Scientist`


#### 1.4 Solution preconditions

- Describe all general solution preconditions used in business: What data is used, what's the prediction horizon, model granularity, etc - `Data Scientist`  


### 2. `Data Scientist` Methodology

#### 2.1. Setting the tasks

- What are we creating from ds standpoint? CV, optimization, prediction, clusterization, etc - `Data Scientist`  

#### 2.2. BPMN

#### 2.3. Steps required to solve the task - `Data Scientist`  


### 3 Getting small-scale pilot project ready
 
#### 3.1. Methods and metrics to evaluate the pilot performance  
  - Brief description of project design and ways to evaluate the project `Product Owner`, `Data Scientist` with `AB Group` 
  
#### 3.2. What is considered a successful pilot - `Product Owner`   
  
#### 3.3. Developing pilot
  
- Resources we have and resources we expect to use. - `Data Scientist` 

### 4. Integration into production  

#### 4.1. Pilot architecture

- Block-scheme: microservices, api, etc - `Data Scientist`  

#### 4.2. Structure and scalability 

- Explain the choice of structure - `Data Scientist` 
- Pros and cods of it - `Data Scientist` 
- Compare it to other solutions - `Data Scientist` 
  
#### 4.3. System requirements 

- SLA, capacity and delay - `Data Scientist`  
  
#### 4.4. Security and threats  
  
- Potential threats and security issues `Data Scientist`  
  
#### 4.5. Data safety

- GDPR (for EU) violations and other data-related legal issues - `Data Scientist`  
  
#### 4.6. Costs  
  
- Expected costs per month to maintain the system `Data Scientist`  
  
#### 4.5. Integration points  
  
- Services interactions, API -  `Data Scientist`  
  
#### 4.6. Risks  
  
- Describe risks and possible issues that should be prevented\avoided - `Data Scientist`   
