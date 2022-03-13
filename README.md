
# Predict Your chances for Admission 

### Description
To apply for a master's degree is a very expensive and intensive work. With this models students will decide whether to apply for a master's degree or not.



## Field Name and Description

**GRE-** Graduate Record Examinations score

**TOEFL-** Standardized test used to measure the English-language ability of non-native speakers wishing to enroll in English-speaking universities.

**University Rating-** Rating of university.

**SOP-** Statement of purpose is the rated score of a grad school applicant’s Statement of Purpose.

**LOR-** Letter of Recommendation is a document that provides the admission officers with a comprehensive insight into your suitable candidature, for admission into the concerned University.

**GPA-** Cumulative Grade Point Average is a grade pointing system used in the educational sector.

**Research-** Is having any research experience.



Deployment steps through local system to Heroku server
1.Login to Heroku Server

## Deployment 
#### Through local system to Heroku Server

Deployment steps through local system to Heroku server

1.Go to the project directory and login to Heroku Server using CLI
```bash
  heroku login 
```

2.After login to heroku server create new app.

3.Select deployment method as Heroku CLI and execute below mention script.

```bash
$ git init
$ heroku git:remote -a <name of app>
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

4.After execution of above script try to open the created app.
if everything is good then our app is appeared other wise error will be thrown.

#### Through Git to Heroku Server

Step 1 & 2 is same for git to heroku server.

1.select deployment method as Github.

2.Connect the created app to Github.Once connection has been established then select the repository.

3.choose the branch to deploy and click on deploy branch button.
That it's all about deployment.





## Screenshots

![Input Page](https://github.com/niteshpandeyofficial/Admission-Prediction/blob/6a7e18de1c3d4d5f0685567ca322fbcfe5f60ad1/Main_Page.PNG?raw=true "Optional Title")
![Output Page](https://github.com/niteshpandeyofficial/Admission-Prediction/blob/f47bd6df1326e126d44eb4995dc0f1d6315f6a9a/predicted_page.PNG?raw=true "Optional Title")
## 🔗 Deployed Links
[Click Here](https://dashboard.heroku.com/apps/admission-prediction-demo)

