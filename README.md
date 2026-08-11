# LaboGroupe3

| Who is who | |
|---|---|
| Dev A | Arnaud Hubert |
| Dev B | Louis Buret |
| Dev C | Mattis Courtin |
| Dev D | Mara Lurkin |
| Dev E | Youssef Ouftallah |

## Start docker image
```bash
docker compose up
```
## Acces docker image shell
```bash
docker compose exec app bash
```
Use it in another shell tab or use ```docker compose up -d``` to hide logs.
## Use the sqlAlchimy.sh
In the docker image shell
(Make sure the .env.local is fill up with the database credentials)
### If never initialized the database
```bash
./sqlAlchemy.sh -i
```
### After every model changes
```bash
./sqlAlchemy.sh -m "migration message"
```
### To apply the changes
```bash
./sqlAlchemy.sh -u
```