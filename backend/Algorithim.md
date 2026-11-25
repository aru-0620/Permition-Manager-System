## Permission ID implementation goals

- Keep the incoming `Permission` request model free of an `id`; the frontend should not choose IDs.
- Define a stored/response permission model with a required integer `id`.
- Add a generator that assigns a new, incrementing ID whenever a permission is created.
- Store the ID as part of each permission record so it is returned as a normal field for React to use.
- Return the newly created permission, including its ID, from `POST /permission`.
- Treat the in-memory counter as temporary: it resets when the server restarts. When PostgreSQL storage is added, use a persistent database-generated ID.
