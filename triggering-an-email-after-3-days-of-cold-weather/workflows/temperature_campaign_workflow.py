from tasks.task_check_temperature import TaskCheckTemperature
from tasks.task_send_email_campaign import TaskSendEmailCampaign

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable
from zenaton.tasks.wait import Wait


class TemperatureCampaignWorkflow(Workflow, Zenatonable):

    def __init__(self, days, min_temp, min_rep, city, email_recipients):
        self.days = days
        self.min_temp = min_temp
        self.min_rep = min_rep
        self.city = city
        self.email_recipients = email_recipients

    def handle(self):
        rep_count = 0
        for _ in range(self.days):
            # Checks the temperature
            if TaskCheckTemperature(city=self.city).execute() < self.min_temp:
                rep_count += 1
            else:
                rep_count = 0
            if rep_count == self.min_rep:
                # Sends email campaign, when conditions are met
                TaskSendEmailCampaign(self.email_recipients, self.city).execute()
                break
            # Waits for one day
            Wait().days(1).execute()
        else:
            # Send another campaign, when conditions are never met?
            pass

