import client
from workflows.temperature_campaign_workflow import TemperatureCampaignWorkflow


TemperatureCampaignWorkflow(days=30, min_temp=45, min_rep=3,city='Seattle,US', email_recipients=['yann@zenaton.com']).dispatch()