while true; do 
  curl -X GET "http://127.0.0.1:59096/"
done


.\ab -n 300 -c 10 http://127.0.0.1:59096/



kubectl scale deployment admin-deployment --replicas=3
