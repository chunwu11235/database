### Load database into server
kubectl exec -i mysql-74d8957988-5zng6 -- mysql -u user -ppassword < mysqlsampledatabase.sql

### Client
kubectl run -it --rm --image=mariadb --restart=Never mysql-client -- mysql -h mysql -ppassword