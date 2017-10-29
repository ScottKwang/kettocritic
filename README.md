# kettocritic (Video Game Review Aggregator)

Setup
-----

Run the following script:

```
source setup.sh
```

Debugging an API
----------------

https://sites.google.com/a/zanbato.com/zanbato-internal/interviewing/evaluation/10-factor-assessment
1. Problem Solving
    1. resourcefulness
    2. google and debugging

ORM libraries
* Javascript - [Sequelize](http://docs.sequelizejs.com/)
* Java - [OrmLite](http://ormlite.com/sqlite_java_android_orm.shtml)
* Python - [Pewee](http://docs.peewee-orm.com/en/latest/)

Bugs/Tests
1. GET
    1. Missing properties
    2. Incorrect calculated properties (Game, Reviewer, 1 level deep)
        1. Calculated incorrectly
        2. Incorrect query
    3. Filtering by calculated property
    4. Incorrect calculated properties (Team, 2 levels deep)
    5. 1 bad test
2. POST


Models:
-------

Tag
- Title
- Many-Many Reviewers
- Many-Many Games

Game
- Name
- Console(s)
- Many-Many Tags

Score
- Type (enum)
    - Letter (A-F) (stored as 5-1)
    - Percentage (1-100)
    - Stars (1-5, 1-10)
    - Other (1-40, 1-50, etc)
- Score
    - Number
- Dict maps Type to Max allowed value

Team
- Name
- Website

Reviewer
- Name
- FK Team
- Many-Many Tags

Review
- 1-1 Score
- FK Game
- FK Reviewer
- Description
- Date
- Title

Views/Serializers:
------------------

Game
- Filters: Team, Tag, Aggregate score
- Calculated Properties: Aggregate Score

Review

Reviewer
- Filters: Team, Tag, Aggregate score
- Calculated Properties: Aggregate Score

Team
- Filters: Aggregate score (of all reviewers)
- Calculated Properties: Aggregate score (of all reviewers)

Tag

Tests/Bugs:
----------
TODO


