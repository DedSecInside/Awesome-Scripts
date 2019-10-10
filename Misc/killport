#!/bin/bash

killport(){
    if [ $# -eq 0 ];then
        echo -e "see killport --help for more info";
        return 1; 
    fi
    portnumber=$1
    if [[ $1 =~ \-h|\-\-help ]];then
        echo "killport <port_number>"
        echo "e.g: killport 8000"
        return 0
    fi
    if [[ $1 =~ ^[0-9]+$ ]];then
        kill $(lsof -t -i:$portnumber) &> /dev/null
        if [ $? -ne 0 ];then
            echo "Port is already free"
        fi
    else
        echo "port should be a valid number"
    fi
}

killport $@
