# pylightning
Pylightning is my solution to the crap code completion situation with SQLAlchemy. I will try to be reimplementing most of the basic functionality that I'll find useful in my day-to-day use at work and personal projects in the way I want it to be done.
----
`pylightning` works in a very simple, object-oriented way. The main components are `builders`, `objects`, and `executors`. Builders take objects as input and output SQL, objects are the building blocks that represent tables and the data within them, and executors are the connectors that run the SQL returned by builders.