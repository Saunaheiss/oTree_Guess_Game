from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'group'  # makes oTree to store it in data
    form_fields = ['dictator_decision']  # makes oTree to store it in data

    def is_displayed(self):
        return self.player.role() == 'dictator'


class ResultsWaitPage(WaitPage):
    body_text = "Please wait for Marco. He is slow. Hard decisions to make"

    def after_all_players_arrive(self):
        self.group.set_payoffs() #here we call the function caluclate the number


class Results(Page):
    def vars_for_template(self):
        dictator = self.group.get_player_by_role('dictator')
        receiver = self.group.get_player_by_role('receiver')
        return {'dictator_payoff':dictator.payoff,
            'receiver_payoff':receiver.payoff
        }

class Intro(Page):
    pass


page_sequence = [
    Intro,
    Decision,
    ResultsWaitPage,
    Results
]
