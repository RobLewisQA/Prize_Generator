pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        app_version = "version1"

    }
    stages {
        
        // execute tests from test_script
        stage('Test') {
            steps{
                sh 'bash test_script.sh'
            }
        }
        // execute build based on docker-compose
        stage('Build') {
            steps{
                sh 'docker-compose build'
            }
        }
        // execute push to Docker Hub
        stage('Push') { 
            steps{
                    sh 'docker-compose push'
                }
            }
        // execute ansible playbook execution referencing the inventory to configure roles to nodes in the cluster
        stage('Swarm Config') { 
            steps{
                sh 'ansible-galaxy collection install community.docker'
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml' 
            }
        }
        // executing the deployment of the stack
        stage('Deploy') {
            steps{
                sh 'bash deploy_script.sh'
            }   
        }
    }
}
