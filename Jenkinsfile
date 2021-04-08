pipeline {
    agent any
    //environment{
    //    DATABASE_URI
    //}
    stages {
        //stage('Test') {
        //}
        stage('Build') {
            steps{
                sh 'docker-compose build'
            }
        }
        stage('Push') { 
            steps{
                sh 'docker-compose push' 
            }
        }
        stage('Swarm Config') { 
            steps{
                sh sh 'ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage('Deploy') {
            steps{
                 sh 'docker-compose up'
            }   
        }
    }
}