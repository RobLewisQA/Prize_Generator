pipeline {
    agent any
    environment{
        DATABASE_URI
    }
    stages {
        //stage('Test') {
        //}
        stage('Build') {
            sh 'docker-compose build'  
        }
        stage('Push') { 
            sh 'docker-compose push' 
        }
        stage('Swarm Config') { 
             sh 'ansible-playbook -i inventory.yaml playbook.yaml'
        }
        //stage('Deploy') {
        //    sh 'docker stack deploy'  
        }
    }
}