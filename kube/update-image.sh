#!/bin/bash
QUERY=`curl https://api.github.com/repos/seendsouza/acn-bot/actions/runs 2> /dev/null`
# status completed and conclusion success
COMMIT=`echo $QUERY | jq -r '[.workflow_runs[] | select(.status == "completed" and .conclusion == "success").head_sha][0]'`

if [ ${#COMMIT} == 40 ]
then
    TAG="sha-${COMMIT:0:7}"
    echo "Tag: $TAG"
    
    DIR="$(cd "$(dirname "$0")" && pwd)"
    FILE="$DIR/ACN_COMMIT"
    if [ ! -f $FILE ]
    then
        echo "default" > $FILE
    fi
    ACN_COMMIT=$(cat "$FILE")
    
    if [ "$COMMIT" != "$ACN_COMMIT" ]
    then
        echo "Updating acn-bot image."
        echo $COMMIT > $FILE
    
        KUBE_FILE=$DIR/deploy.yaml
    
        sed -i "s/\\(seendsouza\/acn-bot:\\).*/\\1$TAG/" "$KUBE_FILE"
        kubectl apply -f $KUBE_FILE
    fi
else
    echo "Query error"
fi
