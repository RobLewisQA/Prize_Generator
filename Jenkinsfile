pipeline {
    agent any
    //environment{
    //    DATABASE_URI = credentials('DATABASE_URI')
    //}
    stages {
        //stage('Test') {
        //}
        stage('Build') {
            steps{
                sh 'docker-compose build'
            }
        }
        //stage('Push') { 
        //    steps{
        //        sh 'docker-compose push' 
        //    }
        //}
        stage('Swarm Config') { 
            steps{
                sh 'cd ansible'
                sh 'ls'
                sh 'ansible-galaxy collection install community.docker'
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage('Deploy') {
            steps{
                sh 'cd /Prize_Generator && docker-compose up'
            }   
        }
    }
}