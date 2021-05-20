import goalsster
from goalsster import Goal
from goalsster import Goalsster
from goalsster import RealDayFactory
from goalsster import Spec

def runUI():
    goalsster.DAY_FACTORY = RealDayFactory()
    today = RealDayFactory().get_today()

    goalsster = goalsster()
    run = Goal("run", "Run.", Spec(2, 10), today)
    goalsster.add(run)

    pushups = Goal("push-ups", "Do 100 push ups, 2 minute breaks", Spec(2, 6), today)
    goalsster.add(pushups)

    goalsster.add(Goal("word of the week", "Groovy", Spec(5, 10), today))

    swim = Goal("swim", "Swim.", Spec(3, 365), today)
    goalsster.add(swim)

    goalsster.ui()


runUI()
