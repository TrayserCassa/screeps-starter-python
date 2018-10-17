# import harvester
# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.
# from defs import *

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.


def main():
    """
    Main game logic loop.
    """

    creep = Game.creeps['Harvester1']
    sources = creep.room.find(FIND_SOURCES)
    if creep.harvest(sources[0]) == ERR_NOT_IN_RANGE:
        creep.moveTo(sources[0])
    

module.exports.loop = main
