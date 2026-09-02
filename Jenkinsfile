pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               // This will now execute perfectly since pipenv is installed
               // sh 'pipenv --python python3 sync'
				sh 'pipenv --python /usr/local/bin/python3.12 install'
            }
        }
        stage('Test') {
            steps {
               // This will run your Python unit tests
               sh 'pipenv run pytest'
            }
        }
        stage('Package') {
	    when{
		    anyOf{ branch "main"; branch "master"; branch 'release'; branch "dev"  }
	    }
            steps {
               // This creates the zip package file dynamically
               sh 'zip -r sbdl.zip lib'
            }
        }
	stage('Release') {
	   when{
	      branch 'release'
	   }
           steps {
             // Instead of copying over the internet to the author's dead IP,
                // this safely saves your package into a deployments folder on your own VM
               sh 'mkdir -p /var/jenkins_home/deployments'
               sh 'cp sbdl.zip /var/jenkins_home/deployments/'
               echo 'Package deployed successfully to your local Azure workspace directory!'
              
               //   sh "scp -i /home/prashant/cred/edge-node_key.pem -o 'StrictHostKeyChecking no' -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.sh conf prashant@40.117.123.105:/home/prashant/sbdl-qa"
           }
        }
	stage('Deploy') {
	   when{
	      branch 'master'
	   }
           steps {
               // Copies packages straight into your VM's Production environment path
                sh 'mkdir -p /var/jenkins_home/production-deploy'
                sh 'cp sbdl.zip log4j.properties sbdl_main.py sbdl_submit.sh conf /var/jenkins_home/production-deploy/'
                echo 'Project successfully deployed to the production-ready directory!'
               // sh "scp -i /home/prashant/cred/edge-node_key.pem -o 'StrictHostKeyChecking no' -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.sh conf prashant@40.117.123.105:/home/prashant/sbdl-prod"
           }
        }
    }
}
