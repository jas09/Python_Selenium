pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/jas09/Python_Selenium.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                //bat 'python -m pytest --alluredir=allure-results --browser_name=chrome --url_key=MOBILE_SHOP --headless'
                bat 'python -m pytest -n 3 --alluredir=allure-results --headless -v'
            }
        }
    }

    post {
        always {
            allure([
                results: [[path: 'allure-results']]
            ])
        }

        Success {jiraSendBuildInfo site: 'azharullamohammed2.atlassian.net'
                echo "Build info sent to jira"}
        failure {jiraSendBuildInfo site: 'azharullamohammed2.atlassian.net'
                echo "Failed build info sent to Jira"}
    }
}