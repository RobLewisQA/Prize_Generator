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
        //stage('Push') { 
        //    steps{
        //        sh 'docker-compose push' 
        //    }
        //}
        stage('Swarm Config') { 
            steps{
                sh 'cd ansible'
                sh 'ls'
                sh 'ls -a'
                sh 'ansible-galaxy collection install community.docker'
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage('Deploy') {
            steps{
                sh 'cd Prize_Project'
                sh 'docker-compose up'
            }   
        }
    }
}