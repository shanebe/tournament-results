#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import sys
import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect('dbname=tournament')

def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches;")
    DB.commit()
    DB.close()
    return DB

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players;")
    DB.commit()
    DB.close()
    return DB

def countPlayers():
    """Returns the number of players currently registered."""   
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(id) from players;")
    data = c.fetchall()
    DB.close()
    assert len(data) == 1
    return int(data[0][0])

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()
    return DB
    
def playerStandings():
    """ Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = """
    select players.id, name, count(matches.id) as {group}
        from players left join matches
            on players.id = {name}
        group by players.id
        order by {group} desc 
    """

    wins = query.format(name='winner', group='wins')
    losses = query.format(name='loser', group='losses')
    join = """
    select winners.id, winners.name, wins, wins+losses as matches
        from ({wins}) as winners left join ({losses}) as losers
            on winners.id = losers.id;
    """.format(wins=wins, losses=losses)

    DB = connect()
    c = DB.cursor()
    c.execute(join + ';')
    results = c.fetchall()
    DB.close()
    return results

def reportMatch(winner, loser):
    """
    Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches (winner,loser) VALUES (%s, %s)", (winner, loser,))
    DB.commit()
    DB.close()
    return DB
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = [(data[0], data[1]) for data in playerStandings()]
    #if len(standings) < 2:
    #    raise KeyError("Looks like we dont have enough players, bring someone on board.")
    left = standings[0::2]
    right = standings[1::2]
    pairings = zip(left, right)

    # flatten the pairings and convert back to a tuple
    results = [tuple(list(sum(pairing, ()))) for pairing in pairings]

    return results
