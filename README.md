# kettocritic (Video Game Review Aggregator)

## Setup

Run the following script:

```
source setup.sh
source bin/activate
```

## Debugging an API Challenge

https://sites.google.com/a/zanbato.com/zanbato-internal/interviewing/evaluation/10-factor-assessment
1. Problem Solving
    1. resourcefulness
    2. google and debugging

#### ORM libraries
* Javascript - [Sequelize](http://docs.sequelizejs.com/)
* Java - [OrmLite](http://ormlite.com/sqlite_java_android_orm.shtml)
* Python - [Pewee](http://docs.peewee-orm.com/en/latest/)

#### Bugs/Tests
1. GET
    1. Missing properties
    2. Incorrect calculated properties (Game, Reviewer, 1 level deep)
        1. Calculated incorrectly
        2. Incorrect query
    3. Filtering by calculated property
    4. Incorrect calculated properties (Team, 2 levels deep)
    5. 1 bad test
2. POST


### Models:

#### Tag
- Title
- Reviewers *(M-M)*
- Games *(M-M)*

#### Game
- Name
- Tags *(M-M)*

#### Team
- Name
- Website

#### Score
- Type (enum)
    - Letter (A-F)
        - A=5, B=4, C=3, D=2, F=1
    - Percentage
        - 0-100
    - Stars
        - 0-5
- Score (Number)
- Dict maps Type to allowed values?

#### Reviewer
- Name
- Team *(FK)*
- Tags *(M-M)*

#### Review
- Score *(1-1)*
- Game *(FK)*
- Reviewer *(FK)*
- Title
- Date
- Description

### Views/Serializers:

#### Game
- Calculated Properties
    - Aggregate Score
        - Through Reviews
- Filters
    - Reviewer ID
    - Team ID
        - Through Reviewer
    - Aggregate Score (calculated)
- Sort Fields
    - Aggregate Score (calculated)
    - Reviewer Name
        - Through Reviewer
    - Team Name
        - Through Reviewer-->Team

#### Team
- Calculated Properties
    - Average Score
        - Through Reviewers-->Reviews
- Filters
    - Average Score (calculated)
- Sort Fields
    - Average Score (calculated)

#### Review
- Filters
    - Reviewer ID
    - Team ID
        - Through Reviewer
    - Game
- Sort Fields
    - Score
    - Game Name
        - Through Game
    - Reviewer Name
        - Through Reviewer
    - Team Name
        - Through Reviewer-->Team

#### Reviewer
- Calculated Properties
    - Average Score
        - Through Reviews
- Filters
    - Game ID
        - Through Review
    - Team ID
    - Aggregate Score
- Sort Fields
    - Average Score (calculated)
    - Team Name
        - Through Team
    - Game Name
        - Through Review-->Game

#### Tag
- Calculated Properties
    - Aggregate Score
        - Through Game Aggregate Score (calculated)
- Filters
    - Game ID
    - Reviewer ID

### Tests/Bugs:

Run the following script to run the test suite:

```
python test.py
```

### Interactive Shell

Run the interactive shell with the following arugments to play around:

```
python -i run.py
``` 
