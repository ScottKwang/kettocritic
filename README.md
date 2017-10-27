# kettocritic (Video Game Review Aggregator)

## Setup

Run the following script:

```
source setup.sh
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
- Filters
    - Reviewer
    - Team (through Reviewer)
    - Tag
    - Aggregate Score
- Sort Fields
    - Aggregate Score (highest/lowest)
    - Reviewer (name)
    - Team (name)
- Calculated Properties
    - Aggregate Score

#### Review
- Filters
    - Reviewer
    - Team (through Reviewer)
    - Game
- Sort Fields
    - Game (name)
    - Reviewer (name)
    - Team (name)
    - Score (highest/lowest)

#### Reviewer
- Filters
    - Game (through Review)
    - Review
    - Team
    - Tag
    - Aggregate Score
- Sort Fields
    - Aggregate Score (highest/lowest)
    - Reviews (highest/lowest)
    - Game (name)
    - Team (name)
- Calculated Properties
    - Aggregate Score

#### Team
- Filters
    - Reviewers aggregate Score
- Calculated Properties
    - Reviewers aggregate Score

#### Tag
- Filters
    - Game
    - Reviewer
- Calculated Properties
    - Aggregate Score (through Game Aggregate Score)

### Tests/Bugs:
TODO
