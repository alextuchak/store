# store

## 

## How to start project?

- pull repository

```

https://github.com/alextuchak/store.git

```

- open terminal and run :

```

docker-compose up -d

```

- when docker create container run commands one by one for restoring db:

```

docker exec -i deploy-postgres-1 psql -U products_owner -d products < /deploy/postgres/categories_dump.sql

```

```

docker exec -i store-postgres-1 psql -U products_owner -d products < deploy/postgres/products_dump.sql

```

```

docker exec -i store-postgres-1 psql -U products_owner -d products < deploy/postgres/products_dump.sql

```

- [check project](http://stepik-store.localhost/)