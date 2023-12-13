# change the name when developing outside local
# db or dbdrop
for f in ../backend/migrations/*.sql;
do
    psql -h localhost -U admin -f "$f"
done
