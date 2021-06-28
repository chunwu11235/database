### Load database into server
kubectl exec -i <podname> -- mysql -u user -ppassword < mysqlsampledatabase.sql

### Run bash terminal inside pod
kubectl exec -it <podname> -- bash

### Client
kubectl run -it --rm --image=mariadb --restart=Never <podname> -- mysql -h mysql -ppassword
