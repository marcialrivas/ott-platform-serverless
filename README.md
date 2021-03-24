# ott-platform-serverless

Serverless ott platform based on AWS services

---
## Code structure

The code of this project is divided in the following sections:

* [front-end-microservices](docs/front-end-microservices.md)

    `Includes all the necesary microservices to show the front end aplications and use it`
    
* back-end-microservices
* front-end-apps
* back-end-apps
* infrastructure
* ...

## CI/CD workflow


**Build** &rightarrow; SonarCloud &rightarrow; Unit testing &rightarrow; **Test** 
&rightarrow; QA deployment &rightarrow; Integration testing &rightarrow; 
Smoke testing &rightarrow; Load testing &rightarrow; 
**Deploy** &rightarrow; Prod deployment

### SonarCloud quality gates
