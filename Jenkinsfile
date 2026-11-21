pipeline {
    agent any

    environment {
        JIRA_SITE = 'azharullamohammed2.atlassian.net'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/jas09/Python_Selenium.git'
            }
        }

        stage('Extract Jira Key') {
            steps {
                script {
                    def commitMessage = bat(script: 'git log -1 --pretty=%%B',returnStdout: true).trim()

                    echo "Commit Message: ${commitMessage}"
                    def matcher = commitMessage =~ /([A-Z]+-\d+)/

                    if (matcher.find()) {
                        env.JIRA_ISSUE = matcher.group(1)
                        echo "Jira Issue Found: ${env.JIRA_ISSUE}"
                    } else {
                        error("No Jira issue key found in commit message.")
                    }
                }
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

                bat '''
                python -m pytest ^
                -n 3 ^
                --headless ^
                --alluredir=allure-results ^
                --json-report ^
                --json-report-file=report.json ^
                -v
                '''
            }
        }

        stage('Read Test Metrics') {
            steps {
                script {
                    if (fileExists('report.json')) {

                        def report = readJSON file: 'report.json'

                        env.TOTAL_TESTS =
                                "${report.summary.total ?: 0}"

                        env.PASSED_TESTS =
                                "${report.summary.passed ?: 0}"

                        env.FAILED_TESTS =
                                "${report.summary.failed ?: 0}"

                        env.SKIPPED_TESTS =
                                "${report.summary.skipped ?: 0}"

                        echo """
==================================================
BUILD SUMMARY
==================================================
Total Tests : ${env.TOTAL_TESTS}
Passed      : ${env.PASSED_TESTS}
Failed      : ${env.FAILED_TESTS}
Skipped     : ${env.SKIPPED_TESTS}
==================================================
"""
                    }
                }
            }
        }
    }

    post {
        always {
            allure([results: [[path: 'allure-results']]])
            archiveArtifacts(artifacts: 'allure-results/**/*',allowEmptyArchive: true)
            jiraSendBuildInfo(site: "${JIRA_SITE}")
        }

        success {
            script {
                def jiraComment = """
Build #${env.BUILD_NUMBER} Completed Successfully

✅ Passed : ${env.PASSED_TESTS}
❌ Failed : ${env.FAILED_TESTS}
⏭ Skipped : ${env.SKIPPED_TESTS}
📊 Total  : ${env.TOTAL_TESTS}

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