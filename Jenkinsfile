pipeline {
    agent any
    //environment{
    //    DATABASE_URI = credentials('DATABASE_URI')
    //      registry = "roblewisqa"
    //      registryCredential = 'dockerhub_id'
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
                sh 'ansible-galaxy collection install community.docker'
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml' 
            }
        }
        stage('Deploy') {
            steps{
                sh 'docker stack deploy --compose-file docker-compose.yaml Prize_Project'
            }   
        }
    }
}