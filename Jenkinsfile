// here is the production-ready Jenkins file that:
// Extracts Jira issue from commit message
// Runs Pytest
// Generates Allure
// Reads test metrics
// Sends Build Info to Jira
// Posts a Jira comment containing:
// Passed
// Failed
// Skipped
// Total
// Jenkins URL
// Allure URL
//
//
// Required Jenkins Plugins:
// Atlassian Jira Software Cloud
// Allure Jenkins Plugin
// Pipeline Utility Steps
//
// Required Python Package:
// pip install pytest-json-report

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

                    def commitMessage = bat(
                        script: 'git log -1 --pretty^=%%B',
                        returnStdout: true
                    ).trim()

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
                -n 5 ^
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

            allure([
                results: [[path: 'allure-results']]
            ])

            archiveArtifacts(
                artifacts: 'allure-results/**/*',
                allowEmptyArchive: true
            )

            jiraSendBuildInfo(
                site: "${JIRA_SITE}"
            )
        }


success {
    script {
        def jiraComment = """\
Build #${env.BUILD_NUMBER} Completed Successfully

✅ Passed : ${env.PASSED_TESTS}
❌ Failed : ${env.FAILED_TESTS}
⏭ Skipped : ${env.SKIPPED_TESTS}
📊 Total : ${env.TOTAL_TESTS}

Jenkins:
${env.BUILD_URL}

Allure:
${env.BUILD_URL}allure
"""

        writeFile(
            file: 'jira-comment.txt',
            text: jiraComment,
            encoding: 'UTF-8'
        )

        withCredentials([
            usernamePassword(
                credentialsId: 'jira-api-creds',
                usernameVariable: 'JIRA_USER',
                passwordVariable: 'JIRA_TOKEN'
            )
        ]) {
            withEnv([
                "CURRENT_JIRA=${env.JIRA_ISSUE}",
                "CURRENT_SITE=${JIRA_SITE}"
            ]) {
                powershell '''
                    $ErrorActionPreference = "Stop"

                    $issueKey = $env:CURRENT_JIRA
                    $site = $env:CURRENT_SITE.Trim()

                    Write-Host "Preparing Jira comment for $issueKey"

                    # Authentication
                    $pair = $env:JIRA_USER + ":" + $env:JIRA_TOKEN
                    $bytes = [System.Text.Encoding]::UTF8.GetBytes($pair)
                    $base64 = [System.Convert]::ToBase64String($bytes)

                    $headers = @{
                        Authorization = "Basic $base64"
                        Accept       = "application/json"
                    }

                    # Read comment using UTF-8
                    $commentText = Get-Content `
                        -Path "jira-comment.txt" `
                        -Raw `
                        -Encoding UTF8

                    # Convert multiline comment into ADF paragraphs
                    $lines = $commentText -split "\\r?\\n"

                    $paragraphs = @(
                        foreach ($line in $lines) {
                            if ([string]::IsNullOrWhiteSpace($line)) {
                                @{
                                    type    = "paragraph"
                                    content = @()
                                }
                            }
                            else {
                                @{
                                    type = "paragraph"
                                    content = @(
                                        @{
                                            type = "text"
                                            text = $line
                                        }
                                    )
                                }
                            }
                        }
                    )

                    # Jira Atlassian Document Format
                    $bodyObject = @{
                        body = @{
                            type    = "doc"
                            version = 1
                            content = $paragraphs
                        }
                    }

                    $jsonBody = $bodyObject | ConvertTo-Json -Depth 20

                    # Explicit UTF-8 request body
                    $utf8Body = [System.Text.Encoding]::UTF8.GetBytes($jsonBody)

                    $uri = "https://$site/rest/api/3/issue/$issueKey/comment"

                    Write-Host "Posting comment to Jira..."
                    Write-Host "Payload size: $($utf8Body.Length) bytes"

                    try {
                        $response = Invoke-RestMethod `
                            -Uri $uri `
                            -Method POST `
                            -Headers $headers `
                            -ContentType "application/json; charset=utf-8" `
                            -Body $utf8Body `
                            -TimeoutSec 30

                        Write-Host "Jira comment posted successfully."
                        Write-Host "Comment ID: $($response.id)"
                    }
                    catch {
                        Write-Host "ERROR: Jira comment posting failed."
                        Write-Host "Error details: $($_.Exception.Message)"

                        if ($_.Exception.Response) {
                            Write-Host "HTTP Status: $($_.Exception.Response.StatusCode)"
                        }

                        throw
                    }
                '''
            }
        }
    }
}


        failure {

            script {

                echo "Build failed. Build information sent to Jira."
            }
        }
    }
}