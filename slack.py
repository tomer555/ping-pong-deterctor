
from slack_sdk.webhook import WebhookClient

url = "https://hooks.slack.com/services/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"
webhook = WebhookClient(url)

def sendSlackMessage (status):
	webhook.send(
		text=f"Ping Pong Room Status: {status}",
		blocks=[
			{
				"type": "header",
				"text": {
					"type": "plain_text",
					"text": ":table_tennis_paddle_and_ball: Ping Pong Room Status :table_tennis_paddle_and_ball:"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": f'*status:* {status}'
				}
			}
		]
	)
	print(f'slack message sent')