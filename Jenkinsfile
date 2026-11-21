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

        stage('Debug') {
            steps {
                bat 'dir'
                bat 'dir pageObjects'
                bat 'dir Utilities'
            }
        }

        stage('Run Tests') {
            steps {
                //bat 'python -m pytest --alluredir=allure-results --browser_name=chrome --url_key=MOBILE_SHOP --headless'
                bat 'python -m pytest -n 2 --alluredir=allure-results -v'
            }
        }
    }

    post {
        always {
            allure([
                results: [[path: 'allure-results']]
            ])
        }
    }
}