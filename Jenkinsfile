pipeline {
    agent any
    environment{
    //    DATABASE_URI = credentials('DATABASE_URI')
          registry = "roblewisqa/prize_project"
          registryCredential = 'dockerhub_id'
          dockerImage = ''
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
        //stage('Push') { 
        //    steps{

        //        }
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
                sh 'docker swarm init && docker stack deploy --compose-file docker-compose.yaml prize_project'
            }   
        }
    }
}