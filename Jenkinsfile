#!/usr/bin/env groovy
 
import hudson.model.*
import hudson.EnvVars
import groovy.json.JsonSlurperClassic
import groovy.json.JsonBuilder
import groovy.json.JsonOutput
import java.net.URL
 
 
 
def workspace = null

  node { 
    stage ('Stage 0 - checkout '){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/eovadia/Forcast-Collector.git']]])
    stage ('Stage 1 - verify '){
        sh 'md5sum --check md5.txt'
    stage ('Stage 2 - exec script '){
        sh 'python forcast_collector.py > data.json'
    stage ('Stage 3 - validate JSON sructure '){ 
        sh 'python -m json.tool data.json'
        milestone()
        echo "Please Validate the Sructure to the example !"
        milestone()
        
    }
    }
    }
    }
}
