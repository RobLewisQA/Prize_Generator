pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        app_version = "version1"

    }
    stages {
        
        // add multi-step testing stage here
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
                //script{
                //    docker.withRegistry('https://registry.hub.docker.com','dockerhub_id'){
                //    image.push("${env.app_version}")}
                ///    }
                }
            }

        stage('Swarm Config') { 
            steps{
                sh 'ansible-galaxy collection install community.docker'
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml' 
            }
        }

        stage('Deploy') {
            steps{
                sh 'cd && bash deploy-script.sh'
                //sh 'docker stack deploy --compose-file docker-compose.yaml prize_project'
                //sh 'docker-compose up'
            }   
        }
    }
}