pipeline{
  agent any
     stages {
         stage('test'){
                   steps{bat 'python -m unittest discover'}}
         stage('Run'){
                   steps{bat 'python app.py'}}
         stage('Deploy'){ steps{
                   echo 'Deploying...'
                            }}}
         post{
            success{
                  echo 'Build, Run and Test successful'}
            failure{
                  echo 'Something went wrong'}}}