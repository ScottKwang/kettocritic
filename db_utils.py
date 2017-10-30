#!bin/python
import os
from peewee import OperationalError

from kettocritic import db, models


def create_tables():
    try:
        db.connect()
        db.create_tables([models.Game,
                          models.Tag,
                          models.GameToTag,
                          models.Team,
                          models.Reviewer,
                          models.Score,
                          models.Review,
                          models.ReviewerToTag])
        db.close()
    except OperationalError:
        pass

def drop_tables():
    try:
        db.connect()
        db.drop_tables([models.Game,
                          models.Tag,
                          models.GameToTag,
                          models.Team,
                          models.Reviewer,
                          models.Score,
                          models.Review,
                          models.ReviewerToTag])
        db.close()
    except OperationalError:
        pass

    models.Game.delete().execute()
    models.Tag.delete().execute()
    models.GameToTag.delete().execute()
    models.Team.delete().execute()
    models.Reviewer.delete().execute()
    models.Score.delete().execute()
    models.Review.delete().execute()
    models.ReviewerToTag.delete().execute()


def create_data():
    # Create Tags
    tag_legacy = models.Tag.create(name="Legacy")
    tag_pc = models.Tag.create(name="PC")
    tag_ps4 = models.Tag.create(name="PS4")
    tag_switch = models.Tag.create(name="Switch")
    tag_wiiu = models.Tag.create(name="Wii U")
    tag_xbox_one = models.Tag.create(name="Xbox One")

    tag_action = models.Tag.create(name="action")
    tag_adventure = models.Tag.create(name="adventure")
    tag_fighting = models.Tag.create(name="fighting")
    tag_fps = models.Tag.create(name="fps")
    tag_platformer = models.Tag.create(name="platformer")
    tag_rts = models.Tag.create(name="rts")
    tag_simulation = models.Tag.create(name="simulation")

    # Create Games
    ac_origins = models.Game.create(name="Assassins Creed Origins")
    cities_skyline = models.Game.create(name="Cities Skylines")
    cuphead = models.Game.create(name="Cuphead")
    destiny2 = models.Game.create(name="Destiny 2")
    smash4 = models.Game.create(name="Super Smash Bros. for Wii U")
    supermeatboy = models.Game.create(name="Super Meat Boy")

    # Create GameToTags
    models.GameToTag.create(game=ac_origins, tag=tag_pc)
    models.GameToTag.create(game=ac_origins, tag=tag_ps4)
    models.GameToTag.create(game=ac_origins, tag=tag_xbox_one)
    models.GameToTag.create(game=ac_origins, tag=tag_action)
    models.GameToTag.create(game=ac_origins, tag=tag_adventure)

    models.GameToTag.create(game=cities_skyline, tag=tag_pc)
    models.GameToTag.create(game=cities_skyline, tag=tag_ps4)
    models.GameToTag.create(game=cities_skyline, tag=tag_xbox_one)
    models.GameToTag.create(game=cities_skyline, tag=tag_simulation)

    models.GameToTag.create(game=cuphead, tag=tag_pc)
    models.GameToTag.create(game=cuphead, tag=tag_xbox_one)
    models.GameToTag.create(game=cuphead, tag=tag_action)
    models.GameToTag.create(game=cuphead, tag=tag_platformer)

    models.GameToTag.create(game=destiny2, tag=tag_pc)
    models.GameToTag.create(game=destiny2, tag=tag_ps4)
    models.GameToTag.create(game=destiny2, tag=tag_xbox_one)
    models.GameToTag.create(game=destiny2, tag=tag_action)
    models.GameToTag.create(game=destiny2, tag=tag_fps)

    models.GameToTag.create(game=smash4, tag=tag_wiiu)
    models.GameToTag.create(game=smash4, tag=tag_action)
    models.GameToTag.create(game=smash4, tag=tag_fighting)

    models.GameToTag.create(game=supermeatboy, tag=tag_pc)
    models.GameToTag.create(game=supermeatboy, tag=tag_ps4)
    models.GameToTag.create(game=supermeatboy, tag=tag_wiiu)
    models.GameToTag.create(game=supermeatboy, tag=tag_legacy)
    models.GameToTag.create(game=supermeatboy, tag=tag_action)
    models.GameToTag.create(game=supermeatboy, tag=tag_platformer)

    # Create Teams
    ign = models.Team.create(name="IGN", website="https://www.ign.com/")
    metacritic = models.Team.create(name="metacritic", website="http://www.metacritic.com")
    pcgamer = models.Team.create(name="PCGamer", website="http://www.pcgamer.com")

    # Create Reviewers
    ign_john = models.Reviewer.create(name="John Wall", team=ign)
    ign_bradley = models.Reviewer.create(name="Bradley Beal", team=ign)
    ign_mike = models.Reviewer.create(name="Mike Scott", team=ign)

    mc_curry = models.Reviewer.create(name="Stephen Curry", team=metacritic)
    mc_kevin = models.Reviewer.create(name="Kevin Durant", team=metacritic)
    mc_klay = models.Reviewer.create(name="Klay Thompson", team=metacritic)
    mc_draymond = models.Reviewer.create(name="Draymond Green", team=metacritic)

    pc_lebron = models.Reviewer.create(name="LeBron James", team=pcgamer)
    pc_derrick = models.Reviewer.create(name="Derrick Rose", team=pcgamer)
    pc_dwyane = models.Reviewer.create(name="Dwyane Wade", team=pcgamer)

    # Create ReviewerToTags

    # Create Scores

    # Create Reviews

