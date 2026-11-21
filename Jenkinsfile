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

            archiveArtifacts(
                artifacts: 'allure-results/**/*',
                allowEmptyArchive: true
            )

            echo """
====================================
BUILD SUMMARY
====================================
Total Tests : ${env.TOTAL_TESTS}
Passed      : ${env.PASSED_TESTS}
Failed      : ${env.FAILED_TESTS}
Skipped     : ${env.SKIPPED_TESTS}
====================================

Jenkins:
${env.BUILD_URL}

Allure:
${env.BUILD_URL}allure
"""
        }

        success {

            jiraSendBuildInfo(
                site: "${JIRA_SITE}"
            )

            echo "Build info sent to Jira"
        }

        failure {

            jiraSendBuildInfo(
                site: "${JIRA_SITE}"
            )

            echo "Failed build info sent to Jira"
        }
    }
}